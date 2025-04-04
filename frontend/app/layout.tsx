import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from "@/components/ui/Navbar";
import Footer from "@/components/ui/Footer";
import { Container } from "react-bootstrap";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "車両整備管理システム",
  description: "運送業向け車両整備管理システム",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body className={inter.className}>
        <div className="d-flex flex-column min-vh-100">
          <Navbar />
          <Container className="flex-grow-1 mt-4 mb-4">
            {children}
          </Container>
          <Footer />
        </div>
      </body>
    </html>
  );
}