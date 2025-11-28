type Props = {
  children: React.ReactNode;
  onClick?: () => void;
  type?: "button" | "submit";
};

export default function Button({ children, onClick, type = "button" }: Props) {
  return (
    <button
      type={type}
      onClick={onClick}
      className="bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition"
    >
      {children}
    </button>
  );
}
