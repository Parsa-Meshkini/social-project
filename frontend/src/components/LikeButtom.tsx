import { useState } from "react";

export default function LikeButton({ post, reload }: any) {
  const [loading, setLoading] = useState(false);

  async function likeUnlike() {
    setLoading(true);
    const token = localStorage.getItem("access");

    await fetch(`http://127.0.0.1:8000/api/posts/${post.id}/like/`, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
    });

    setLoading(false);
    reload();
  }

  return (
    <button
      onClick={likeUnlike}
      disabled={loading}
      className="mt-3 text-sm text-blue-600 font-medium"
    >
      ❤️ {post.likes_count} Likes
    </button>
  );
}
