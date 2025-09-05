from fastapi import APIRouter, UploadFile, File, Form
import speech_recognition as sr
from gtts import gTTS
import uuid
import os
from config import settings

router = APIRouter()
os.makedirs(settings.VOICE_OUTPUT_PATH, exist_ok=True)

@router.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    recognizer = sr.Recognizer()
    temp_path = "temp_audio.wav"

    with open(temp_path, "wb") as f:
        f.write(await file.read())

    with sr.AudioFile(temp_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    return {"transcript": text}

@router.post("/tts")
async def text_to_speech(text: str = Form(...), lang: str = "en"):
    tts = gTTS(text=text, lang=lang)
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(settings.VOICE_OUTPUT_PATH, filename)
    tts.save(file_path)
    return {"audio_file": f"voice_outputs/{filename}"}
