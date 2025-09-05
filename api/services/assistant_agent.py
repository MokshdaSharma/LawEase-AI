import faiss
import numpy as np
from datasets import load_dataset
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langdetect import detect
from api.config import settings
from api.services.legal_term_db import get_term_definition
from langchain.embeddings import OpenAIEmbeddings
import os

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    openai_api_key=settings.OPENAI_API_KEY
)

# Embeddings for FAISS search
embedder = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

# Paths for FAISS index + cached dataset
INDEX_PATH = "datasets/ai4bharat_indic-legal.index"
DATA_CACHE = "datasets/ai4bharat_legal.npy"

# Keep dataset in memory for retrieval
dataset_texts = None

def build_faiss_index(dataset_name="ai4bharat/indic-legal-parallel", src_lang="src_hi", tgt_lang="tgt_ta"):
    """
    Build FAISS index from Hugging Face dataset if not already built.
    """
    global dataset_texts

    if os.path.exists(INDEX_PATH) and os.path.exists(DATA_CACHE):
        dataset_texts = np.load(DATA_CACHE, allow_pickle=True).tolist()
        return

    print("Building FAISS index from Hugging Face dataset...")

    ds = load_dataset(dataset_name, split="train")

    src_texts = [ex[src_lang] for ex in ds]
    tgt_texts = [ex[tgt_lang] for ex in ds]

    dataset_texts = list(zip(src_texts, tgt_texts))

    embeddings = embedder.embed_documents(src_texts)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs("datasets", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    np.save(DATA_CACHE, dataset_texts)

    print(f"✅ FAISS index built with {len(src_texts)} entries.")

def search_ai_kosh(query: str, k: int = 3):
    """
    Search FAISS index for nearest legal translations.
    """
    global dataset_texts

    if not os.path.exists(INDEX_PATH):
        build_faiss_index()

    if dataset_texts is None:
        dataset_texts = np.load(DATA_CACHE, allow_pickle=True).tolist()

    index = faiss.read_index(INDEX_PATH)
    query_vec = np.array([embedder.embed_query(query)], dtype="float32")

    D, I = index.search(query_vec, k)

    results = []
    for idx, score in zip(I[0], D[0]):
        if 0 <= idx < len(dataset_texts):
            src, tgt = dataset_texts[idx]
            results.append({
                "score": float(score),
                "src_hi": src,
                "tgt_lang": tgt
            })

    return results

def run_assistant(query: str, lang: str = None) -> str:
    """
    Multilingual AI Assistant with Hybrid Retrieval:
    1. Try FAISS search from AI Kosh dataset (return similar Hindi + translation)
    2. Fallback to local legal term DB
    3. Fallback to LLM response
    """
    if not lang:
        try:
            lang = detect(query)
        except Exception:
            lang = "en"

    # 1️⃣ Try AI Kosh FAISS retrieval
    try:
        results = search_ai_kosh(query, k=3)
        if results:
            response_text = "📖 Based on AI Kosh dataset, here are similar legal references:\n\n"
            for r in results:
                response_text += f"- **Hindi**: {r['src_hi']}\n- **Translation**: {r['tgt_lang']}\n\n"
            return response_text.strip()
    except Exception as e:
        print(f"AI Kosh search failed: {e}")

    # 2️⃣ Try Local Legal Term DB
    definition = get_term_definition(query)
    if definition != "Definition not found.":
        return definition

    # 3️⃣ Fallback to LLM
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a multilingual legal assistant. Explain clearly, in simple words."),
        ("user", f"({lang}) {query}")
    ])

    response = llm.invoke(prompt.format_messages())
    return response.content
