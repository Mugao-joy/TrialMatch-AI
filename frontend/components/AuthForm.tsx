export default function AuthForm({ type }: { type: "login" | "signup" }) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-slate-50">
        <div className="bg-white p-10 rounded-2xl shadow-xl w-full max-w-md">
          <h2 className="text-3xl font-bold text-slate-900 capitalize">{type}</h2>
  
          <input
            type="email"
            placeholder="Email"
            className="w-full mt-6 border rounded-lg p-3"
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full mt-4 border rounded-lg p-3"
          />
  
          <button className="w-full mt-6 bg-teal-600 text-white py-3 rounded-lg">
            {type === "login" ? "Login" : "Create Account"}
          </button>
        </div>
      </main>
    );
  }