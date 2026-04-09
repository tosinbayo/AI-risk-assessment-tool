import "./globals.css";
import NavBar from "@/components/NavBar";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "RiskLens AI",
  description: "Vendor risk assessment frontend starter"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="container-shell">
          <NavBar />
          {children}
        </div>
      </body>
    </html>
  );
}
