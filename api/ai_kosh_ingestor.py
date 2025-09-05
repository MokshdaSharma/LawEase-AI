from datasets import load_dataset
import faiss
import numpy as np
from langchain.embeddings import OpenAIEmbeddings

def ingest_ai_kosh(dataset_name="ai4bharat/indic-legal-parallel", src_lang="src_hi", tgt_lang="tgt_ta"):
    print("Downloading dataset from Hugging Face...")

    ds = load_dataset(dataset_name, split="train")

    # Extract texts
    src_texts = [ex[src_lang] for ex in ds]
    tgt_texts = [ex[tgt_lang] for ex in ds]

    print(f"Loaded {len(src_texts)} sentence pairs ({src_lang} → {tgt_lang})")

    # Embed using OpenAI (or local sentence-transformers)
    embedder = OpenAIEmbeddings()
    embeddings = embedder.embed_documents(src_texts)

    # Build FAISS index
    embeddings = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, f"datasets/{dataset_name.replace('/', '_')}_{src_lang}_{tgt_lang}.index")

    print("Ingestion complete. Index stored.")
