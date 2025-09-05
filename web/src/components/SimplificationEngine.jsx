import React, { useState } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";

function SimplificationEngine() {
  const { t } = useTranslation();
  const [text, setText] = useState("");
  const [simplified, setSimplified] = useState("");

  const handleSimplify = async () => {
    const res = await axios.post("http://localhost:5000/simplify", { text });
    setSimplified(res.data.simplified_text);
  };

  return (
    <div className="bg-white p-4 shadow rounded-2xl">
      <h2 className="text-xl font-semibold mb-2">{t("simplify")}</h2>
      <textarea
        className="w-full border rounded p-2 mb-2"
        rows="4"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste legal text here..."
      />
      <button
        onClick={handleSimplify}
        className="px-4 py-2 bg-green-600 text-white rounded-lg"
      >
        {t("simplify")}
      </button>
      {simplified && <p className="mt-2 text-gray-700">{simplified}</p>}
    </div>
  );
}

export default SimplificationEngine;
