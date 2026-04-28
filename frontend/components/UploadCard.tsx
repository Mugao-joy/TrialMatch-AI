"use client";

import { useState } from "react";

interface PatientProfile {
  diagnosis?: string;
  age?: string;
  gender?: string;
  biomarkers?: string[];
  mutations?: string[];
  current_medications?: string[];
  location?: string;
}

interface TrialResult {
  trial_title?: string;
  nct_id?: string;
  match_score?: number;
  reason?: string;
}

interface UploadResult {
  session_id?: string;
  patient_profile?: PatientProfile;
  ranked_trials?: TrialResult[];
  explanation?: string;
}

export default function UploadCard() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [chatLoading, setChatLoading] = useState(false);
  const [result, setResult] = useState<UploadResult | null>(null);
  const [chatMessage, setChatMessage] = useState("");
  const [chatReply, setChatReply] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  const handleChat = async () => {
    if (!chatMessage || !result?.session_id) return;

    try {
      setChatLoading(true);
      setChatReply("");

      const response = await fetch("http://127.0.0.1:8000/chat/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          session_id: result.session_id,
          message: chatMessage,
        }),
      });

      const data = await response.json();
      setChatReply(data.reply);
      setChatMessage("");
    } catch (error) {
      console.error("Chat failed:", error);
    } finally {
      setChatLoading(false);
    }
  };

  return (
    <div className="bg-white shadow-xl rounded-2xl p-10 w-full max-w-4xl">
      <h2 className="text-3xl font-bold text-slate-900">
        Upload Medical Records
      </h2>

      <p className="text-slate-500 mt-2">
        Upload PDF, DOCX, or image files for AI-powered analysis.
      </p>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="mt-6 block w-full border border-gray-300 rounded-lg p-3"
      />

      <button
        type="button"
        onClick={handleUpload}
        disabled={loading}
        className="w-full mt-6 bg-teal-600 hover:bg-teal-700 transition text-white py-3 rounded-lg"
      >
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>

      {result && (
        <div className="mt-10 space-y-8">
          {/* Patient Profile */}
          <div className="bg-slate-50 rounded-xl p-6">
            <h3 className="text-2xl font-semibold text-slate-900">
              Patient Profile
            </h3>

            <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-700">
              <div>
                <p className="text-sm text-slate-500">Diagnosis</p>
                <p className="font-medium">
                  {result.patient_profile?.diagnosis || "N/A"}
                </p>
              </div>

              <div>
                <p className="text-sm text-slate-500">Age</p>
                <p className="font-medium">
                  {result.patient_profile?.age || "N/A"}
                </p>
              </div>

              <div>
                <p className="text-sm text-slate-500">Gender</p>
                <p className="font-medium">
                  {result.patient_profile?.gender || "N/A"}
                </p>
              </div>

              <div>
                <p className="text-sm text-slate-500">Location</p>
                <p className="font-medium">
                  {result.patient_profile?.location || "N/A"}
                </p>
              </div>
            </div>

            {/* Biomarkers */}
            <div className="mt-6">
              <p className="text-sm text-slate-500 mb-2">Biomarkers</p>
              <div className="flex flex-wrap gap-2">
                {result.patient_profile?.biomarkers?.length ? (
                  result.patient_profile.biomarkers.map((item, index) => (
                    <span
                      key={index}
                      className="bg-teal-100 text-teal-700 px-3 py-1 rounded-full text-sm"
                    >
                      {item}
                    </span>
                  ))
                ) : (
                  <p className="text-slate-500">N/A</p>
                )}
              </div>
            </div>

            {/* Mutations */}
            <div className="mt-6">
              <p className="text-sm text-slate-500 mb-2">Mutations</p>
              <div className="flex flex-wrap gap-2">
                {result.patient_profile?.mutations?.length ? (
                  result.patient_profile.mutations.map((item, index) => (
                    <span
                      key={index}
                      className="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm"
                    >
                      {item}
                    </span>
                  ))
                ) : (
                  <p className="text-slate-500">N/A</p>
                )}
              </div>
            </div>

            {/* Medications */}
            <div className="mt-6">
              <p className="text-sm text-slate-500 mb-2">
                Current Medications
              </p>
              <div className="flex flex-wrap gap-2">
                {result.patient_profile?.current_medications?.length ? (
                  result.patient_profile.current_medications.map(
                    (item, index) => (
                      <span
                        key={index}
                        className="bg-slate-200 text-slate-700 px-3 py-1 rounded-full text-sm"
                      >
                        {item}
                      </span>
                    )
                  )
                ) : (
                  <p className="text-slate-500">N/A</p>
                )}
              </div>
            </div>
          </div>

          {/* Ranked Trials */}
          <div className="bg-slate-50 rounded-xl p-6">
            <h3 className="text-2xl font-semibold text-slate-900">
              Recommended Trials
            </h3>

            {result.ranked_trials?.length ? (
              <div className="mt-4 space-y-4">
                {result.ranked_trials.map((trial, index) => (
                  <div
                    key={index}
                    className="border rounded-lg p-4 bg-white shadow-sm"
                  >
                    <p className="font-semibold text-slate-900">
                      {trial.trial_title || "Untitled Trial"}
                    </p>

                    <p className="text-sm text-slate-500">
                      {trial.nct_id || "No Trial ID"}
                    </p>

                    <p className="text-teal-600 font-medium mt-2">
                      {trial.match_score || 0}% Match
                    </p>

                    <p className="text-slate-500 text-sm mt-1">
                      {trial.reason || "No explanation available."}
                    </p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="mt-4 text-slate-500">
                No matching trials found.
              </p>
            )}
          </div>

          {/* Explanation */}
          <div className="bg-slate-50 rounded-xl p-6">
            <h3 className="text-2xl font-semibold text-slate-900">
              AI Explanation
            </h3>
            <p className="text-slate-600 mt-4 whitespace-pre-line">
              {result.explanation || "No explanation available."}
            </p>
          </div>

          {/* Chat */}
          <div className="bg-slate-50 rounded-xl p-6">
            <h3 className="text-2xl font-semibold text-slate-900">
              Ask TrialMatch AI
            </h3>

            <input
              type="text"
              placeholder="Why was trial 2 ranked low?"
              value={chatMessage}
              onChange={(e) => setChatMessage(e.target.value)}
              className="mt-4 w-full border border-gray-300 rounded-lg p-3"
            />

            <button
              onClick={handleChat}
              disabled={chatLoading}
              className="mt-4 bg-teal-600 hover:bg-teal-700 text-white px-6 py-3 rounded-lg"
            >
              {chatLoading ? "Thinking..." : "Ask"}
            </button>

            {chatReply && (
              <div className="mt-4 bg-white p-4 rounded-lg shadow-sm">
                <p className="text-slate-700 whitespace-pre-line">
                  {chatReply}
                </p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}