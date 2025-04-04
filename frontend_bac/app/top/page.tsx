"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import jwtDecode from "jwt-decode";

export default function TopPage() {
  const [user, setUser] = useState<{ username: string } | null>(null);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      router.push("/login");
      return;
    }

    try {
      const decoded: any = jwtDecode(token);
      setUser({ username: decoded.username });
    } catch (error) {
      router.push("/login");  // JWTエラーならログインページへ
    }
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-md">
        <h1 className="text-2xl font-bold">ようこそ、{user?.username} さん！</h1>
        <button
          onClick={() => {
            localStorage.removeItem("token");
            router.push("/login");
          }}
          className="w-full mt-4 px-4 py-2 text-white bg-red-600 rounded-md"
        >
          ログアウト
        </button>
      </div>
    </div>
  );
}
