import "./globals.css";
import Navbar from "@/components/Navbar";

export const metadata = {
  title: "TrialMatch AI",
  description: "AI-powered clinical trial matching",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        {children}
      </body>
    </html>
  );
}