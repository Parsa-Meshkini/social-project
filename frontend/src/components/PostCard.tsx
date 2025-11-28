interface PostCardProps {
  id: number;
  author: {
    username: string;
    avatar?: string | null;
  };
  content: string;
  image?: string | null;
  likes: number;
}

export default function PostCard({ author, content, image, likes }: PostCardProps) {
  return (
    <div className="bg-white shadow p-4 rounded-xl mb-4">
      {/* Header */}
      <div className="flex items-center gap-3">
        <img
          src={author.avatar || "/default-avatar.png"}
          className="w-10 h-10 rounded-full object-cover"
        />
        <h2 className="font-semibold">{author.username}</h2>
      </div>

      {/* Content */}
      <p className="mt-3">{content}</p>

      {/* Image */}
      {image && (
        <img
          src={image}
          className="mt-3 rounded-lg w-full max-h-[400px] object-cover"
        />
      )}

      {/* Footer */}
      <div className="mt-3 text-sm text-gray-600">
        ❤️ {likes} Likes
      </div>
    </div>
  );
}
