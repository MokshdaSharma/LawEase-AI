import React from "react";
import DocumentUpload from "./components/DocumentUpload";
import SimplificationEngine from "./components/SimplificationEngine";
import ValidationPanel from "./components/ValidationPanel";
import InteractiveAssistant from "./components/InteractiveAssistant";
import { useTranslation } from "react-i18next";

function App() {
  const { t, i18n } = useTranslation();

  const switchLang = (lang) => {
    i18n.changeLanguage(lang);
  };

  return (
    <div className="p-6 space-y-6">
      <header className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">{t("appTitle")}</h1>
        <div>
          <button
            onClick={() => switchLang("en")}
            className="px-3 py-1 border rounded mr-2"
          >
            EN
          </button>
          <button
            onClick={() => switchLang("hi")}
            className="px-3 py-1 border rounded mr-2"
          >
            हिंदी
          </button>
          <button
            onClick={() => switchLang("ta")}
            className="px-3 py-1 border rounded"
          >
            தமிழ்
          </button>
        </div>
      </header>

      <DocumentUpload />
      <SimplificationEngine />
      <ValidationPanel />
      <InteractiveAssistant />
    </div>
  );
}

export default App;
