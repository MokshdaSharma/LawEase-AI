import i18n from "i18next";
import { initReactI18next } from "react-i18next";

const resources = {
  en: {
    translation: {
      appTitle: "Legal Document Simplifier",
      upload: "Upload Document",
      simplify: "Simplify",
      validate: "Validate",
      assistant: "Interactive Assistant",
    },
  },
  hi: {
    translation: {
      appTitle: "कानूनी दस्तावेज़ सरलकर्ता",
      upload: "दस्तावेज़ अपलोड करें",
      simplify: "सरल करें",
      validate: "सत्यापित करें",
      assistant: "इंटरएक्टिव सहायक",
    },
  },
  ta: {
    translation: {
      appTitle: "சட்ட ஆவண எளிமைப்படுத்தி",
      upload: "ஆவணத்தை பதிவேற்றவும்",
      simplify: "எளிதாக்கு",
      validate: "சரிபார்க்கவும்",
      assistant: "இணைய உதவியாளர்",
    },
  },
};

i18n.use(initReactI18next).init({
  resources,
  lng: "en",
  interpolation: { escapeValue: false },
});

export default i18n;
