import React, { useState } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";

function DocumentUpload() {
  const { t } = useTranslation();
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    await axios.post("http://localhost:5000/upload", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    alert("File uploaded successfully!");
  };

  return (
    <div className="bg-white p-4 shadow rounded-2xl">
      <h2 className="text-xl font-semibold mb-2">{t("upload")}</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button
        onClick={handleUpload}
        className="ml-2 px-4 py-2 bg-blue-600 text-white rounded-lg"
      >
        {t("upload")}
      </button>
    </div>
  );
}

export default DocumentUpload;
