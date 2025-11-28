import { useEffect, useState } from "react";

interface Post {
  id: number;
  author: {
    id: number;
    username: string;
    avatar: string | null;
  };
  content: string;
  image: string | null;
  likes_count: number;
}

export default function Feed() {
  const [posts, setPosts] = useState<Post[]>([]);

  async function loadPosts() {
    const res = await fetch("http://127.0.0.1:8000/api/posts/");
    const data = await res.json();
    setPosts(data);
  }

  useEffect(() => {
    loadPosts();
  }, []);

  return (
    <div className="max-w-xl mx-auto mt-10 space-y-5">
      {posts.map((post) => (
        <div
          key={post.id}
          className="bg-white p-4 rounded-xl shadow border border-gray-200"
        >
          <div className="flex items-center gap-3 mb-2">
            <img
              src={post.author.avatar || "/default-avatar.png"}
              className="w-10 h-10 rounded-full object-cover"
            />
            <span className="font-semibold">{post.author.username}</span>
          </div>

          <p className="text-gray-800">{post.content}</p>

          {post.image && (
            <img
              src={post.image}
              className="mt-2 rounded-xl"
              alt="Post"
            />
          )}

          <LikeButton post={post} reload={loadPosts} />
          <CommentsSection postId={post.id} />
        </div>
      ))}
    </div>
  );
}
