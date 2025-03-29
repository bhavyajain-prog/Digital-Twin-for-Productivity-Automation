import React, { useState } from "react";
import axios from "axios";
import "../styles/styles.css";

const Popup = () => {
  const [output, setOutput] = useState("");

  const handleSummarize = () => {
    setOutput("Summarized email content...");
  };

  const handleGenerateReply = () => {
    setOutput("Generated reply text...");
  };

  return (
    <div className="popup-container">
      <h2>AI Email Assistant</h2>
      <button onClick={handleSummarize}>Summarize Email</button>
      <button onClick={handleGenerateReply}>Generate Reply</button>
      <textarea value={output} placeholder="Generated text appears here..." readOnly />
      <div className="footer">
        <button onClick={() => chrome.runtime.openOptionsPage()}>⚙️ Settings</button>
      </div>
    </div>
  );
};

export default Popup;
