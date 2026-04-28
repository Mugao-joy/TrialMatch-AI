"use client";

export default function UploadCard() {
  return (
    <div className="bg-white shadow-xl rounded-2xl p-10 w-full max-w-xl">
      <h2 className="text-3xl font-bold text-slate-900">Upload Medical Records</h2>
      <p className="text-slate-500 mt-2">
        PDF, DOCX, or image files supported.
      </p>

      <input
        type="file"
        className="mt-6 block w-full border border-gray-300 rounded-lg p-3"
      />

      <button className="w-full mt-6 bg-teal-600 text-white py-3 rounded-lg">
        Upload & Analyze
      </button>
    </div>
  );
}