export async function loginUser(email: string, password: string) {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/auth/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!res.ok) return { ok: false, error: "Invalid credentials" };

    const data = await res.json();
    return { ok: true, access: data.access, refresh: data.refresh };
  } catch {
    return { ok: false, error: "Network error" };
  }
}

export async function registerUser(username: string, email: string, password: string) {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/auth/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password }),
    });

    if (!res.ok) {
      const err = await res.json();
      return { ok: false, error: err.detail || "Register failed" };
    }

    return { ok: true };
  } catch {
    return { ok: false, error: "Network error" };
  }
}
