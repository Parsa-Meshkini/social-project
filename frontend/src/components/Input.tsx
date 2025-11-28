import React from "react";

interface Props {
  label: string;
  type?: string;
  value: string;
  onChange: (v: string) => void;
}

export default function Input({ label, type = "text", value, onChange }: Props) {
  return (
    <div className="flex flex-col gap-1">
      <label className="text-sm font-medium">{label}</label>
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="border rounded-lg px-3 py-2 bg-white text-black focus:outline-none focus:ring-2 focus:ring-green-500"
      />
    </div>
  );
}
