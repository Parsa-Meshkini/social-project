import { useEffect, useState } from "react";

interface Comment {
  id: number;
  text: string;
  author: { username: string };
}

export default function CommentsSection({ postId }: any) {
  const [comments, setComments] = useState<Comment[]>([]);
  const [text, setText] = useState("");

  async function loadComments() {
    const res = await fetch(
      `http://127.0.0.1:8000/api/posts/${postId}/comments/`
    );
    const data = await res.json();
    setComments(data);
  }

  async function addComment() {
    const token = localStorage.getItem("access");

    await fetch(`http://127.0.0.1:8000/api/posts/${postId}/comments/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ text }),
    });

    setText("");
    await loadComments();
  }

  useEffect(() => {
    loadComments();
  }, []);

  return (
    <div className="mt-3">
      <div className="space-y-1">
        {comments.map((c) => (
          <p key={c.id} className="text-sm">
            <span className="font-semibold">{c.author.username}: </span>
            {c.text}
          </p>
        ))}
      </div>

      <div className="flex gap-2 mt-3">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="flex-1 border px-3 py-1 rounded"
          placeholder="Add a comment…"
        />
        <button
          onClick={addComment}
          className="text-blue-600 font-medium"
        >
          Post
        </button>
      </div>
    </div>
  );
}
