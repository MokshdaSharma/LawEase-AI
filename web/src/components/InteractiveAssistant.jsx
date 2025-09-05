import React, { useState, useRef } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";

function InteractiveAssistant() {
  const { t } = useTranslation();
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [recording, setRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState(null);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new MediaRecorder(stream);
    mediaRecorderRef.current.start();
    setRecording(true);

    mediaRecorderRef.current.ondataavailable = (event) => {
      audioChunksRef.current.push(event.data);
    };

    mediaRecorderRef.current.onstop = async () => {
      const blob = new Blob(audioChunksRef.current, { type: "audio/wav" });
      audioChunksRef.current = [];
      const formData = new FormData();
      formData.append("file", blob, "voice.wav");

      const sttRes = await axios.post("http://localhost:5000/voice/stt", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setQuery(sttRes.data.transcript);
    };
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  const handleAsk = async () => {
    const res = await axios.post("http://localhost:5000/assistant", { query });
    setResponse(res.data.answer);

    const ttsRes = await axios.post("http://localhost:5000/voice/tts", {
      text: res.data.answer,
    });

    setAudioUrl(`http://localhost:5000/${ttsRes.data.audio_file}`);
  };

  return (
    <div className="bg-white p-4 shadow rounded-2xl">
      <h2 className="text-xl font-semibold mb-2">{t("assistant")}</h2>

      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="w-full border rounded p-2 mb-2"
        placeholder="Ask a legal question..."
      />

      <div className="flex gap-2 mb-2">
        {!recording ? (
          <button
            onClick={startRecording}
            className="px-4 py-2 bg-red-600 text-white rounded-lg"
          >
            🎤 Start
          </button>
        ) : (
          <button
            onClick={stopRecording}
            className="px-4 py-2 bg-gray-600 text-white rounded-lg"
          >
            ⏹ Stop
          </button>
        )}
      </div>

      <button
        onClick={handleAsk}
        className="px-4 py-2 bg-indigo-600 text-white rounded-lg"
      >
        Ask
      </button>

      {response && <p className="mt-2 text-gray-700">{response}</p>}

      {audioUrl && (
        <audio controls className="mt-2">
          <source src={audioUrl} type="audio/mpeg" />
        </audio>
      )}
    </div>
  );
}

export default InteractiveAssistant;
