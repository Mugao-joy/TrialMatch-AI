import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full border-b border-gray-200 bg-white">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <Link href="/" className="text-2xl font-bold text-slate-900">
          TrialMatch AI
        </Link>

        <div className="flex gap-6">
          <Link href="/upload" className="text-slate-700 hover:text-teal-600">
            Upload
          </Link>
          <Link href="/login" className="text-slate-700 hover:text-teal-600">
            Login
          </Link>
          <Link href="/signup" className="bg-teal-600 text-white px-4 py-2 rounded-lg">
            Sign Up
          </Link>
        </div>
      </div>
    </nav>
  );
}