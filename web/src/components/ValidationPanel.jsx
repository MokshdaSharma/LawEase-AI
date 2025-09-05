import React, { useState } from "react";
import { useTranslation } from "react-i18next";

function ValidationPanel() {
  const { t } = useTranslation();
  const [valid, setValid] = useState(null);

  const handleValidate = () => {
    // Placeholder: integrate validation logic with API
    setValid(true);
  };

  return (
    <div className="bg-white p-4 shadow rounded-2xl">
      <h2 className="text-xl font-semibold mb-2">{t("validate")}</h2>
      <button
        onClick={handleValidate}
        className="px-4 py-2 bg-purple-600 text-white rounded-lg"
      >
        {t("validate")}
      </button>
      {valid !== null && (
        <p className="mt-2">
          {valid ? "✅ Document is valid" : "❌ Document has issues"}
        </p>
      )}
    </div>
  );
}

export default ValidationPanel;
