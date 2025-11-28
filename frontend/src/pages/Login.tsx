import { useState } from "react";
import Input from "../components/Input";
import Button from "../components/Button";
import { loginUser } from "../api/auth";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    const result = await loginUser(email, password);

    if (result.ok) {
      localStorage.setItem("access", result.access);
      localStorage.setItem("refresh", result.refresh);
      navigate("/feed");
    } else {
      alert(result.error);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form
        onSubmit={handleLogin}
        className="bg-white text-black p-6 rounded-md w-80 flex flex-col gap-4"
      >
        <h1 className="text-xl font-bold">Login</h1>

        <Input label="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <Input
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Button type="submit">Login</Button>

        <p className="text-sm text-center mt-2">
          Don't have an account?{" "}
          <a href="/register" className="text-blue-600 underline">
            Register
          </a>
        </p>
      </form>
    </div>
  );
}
