import { useState } from "react";
import Input from "../components/Input";
import Button from "../components/Button";
import { registerUser } from "../api/auth";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail]       = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  async function handleRegister(e: React.FormEvent) {
    e.preventDefault();
    const result = await registerUser(username, email, password);

    if (result.ok) {
      alert("Account created!");
      navigate("/");
    } else {
      alert(result.error);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form
        onSubmit={handleRegister}
        className="bg-white text-black p-6 rounded-md w-80 flex flex-col gap-4"
      >
        <h1 className="text-xl font-bold">Register</h1>

        <Input label="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <Input label="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <Input
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <Button type="submit">Register</Button>

        <p className="text-sm text-center mt-2">
          Already have an account?{" "}
          <a href="/" className="text-blue-600 underline">
            Login
          </a>
        </p>
      </form>
    </div>
  );
}
