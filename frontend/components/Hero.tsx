import Link from "next/link";

export default function Hero() {
  return (
    <section className="min-h-screen flex items-center justify-center bg-white px-6">
      <div className="max-w-5xl text-center">
        <h1 className="text-6xl font-bold text-slate-900 leading-tight">
          Find the Right Clinical Trial Faster
        </h1>
        <p className="mt-6 text-xl text-slate-600">
          Upload medical records and let AI match patients to relevant clinical trials in minutes.
        </p>

        <div className="mt-8 flex justify-center gap-4">
          <Link
            href="/upload"
            className="bg-teal-600 text-white px-6 py-3 rounded-xl"
          >
            Get Started
          </Link>
          <Link
            href="/signup"
            className="border border-slate-300 px-6 py-3 rounded-xl"
          >
            Create Account
          </Link>
        </div>
      </div>
    </section>
  );
}