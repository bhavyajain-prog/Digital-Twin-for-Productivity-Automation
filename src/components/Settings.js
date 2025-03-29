import React, { useState } from "react";

const Settings = () => {
  const [apiKey, setApiKey] = useState("");

  const handleSave = () => {
    chrome.storage.sync.set({ apiKey }, () => alert("API Key Saved!"));
  };

  return (
    <div className="settings-container">
      <h2>Settings</h2>
      <input
        type="text"
        value={apiKey}
        onChange={(e) => setApiKey(e.target.value)}
        placeholder="Enter API Key"
      />
      <button onClick={handleSave}>Save</button>
    </div>
  );
};

export default Settings;
