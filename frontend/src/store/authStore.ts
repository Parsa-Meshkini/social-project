import { create } from "zustand";

interface AuthState {
  user: any | null;
  access: string | null;
  refresh: string | null;
  setTokens: (access: string, refresh: string) => void;
  setUser: (user: any) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  access: null,
  refresh: null,

  setTokens: (access, refresh) => set({ access, refresh }),
  setUser: (user) => set({ user }),

  logout: () => set({ user: null, access: null, refresh: null }),
}));
