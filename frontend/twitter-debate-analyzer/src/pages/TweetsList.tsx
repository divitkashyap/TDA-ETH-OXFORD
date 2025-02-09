import { useEffect, useState } from "react";

type Tweet = {
  Handle: string;
  Followers: number;
  Likes: number;
  Retweets: number;
  Tweet: string;
  "Date Posted": string;
};

const TweetsList = () => {
  const [tweets, setTweets] = useState<Tweet[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/tweets")
      .then((response) => response.json())
      .then((data) => {
        setTweets(data.tweets);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching tweets:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading tweets...</p>;

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h2 className="text-xl font-bold mb-4">🔥 Crypto Twitter Debates 🔥</h2>
      {tweets.length === 0 ? (
        <p>No tweets found.</p>
      ) : (
        <div className="space-y-4">
          {tweets.map((tweet, index) => (
            <div
              key={index}
              className="border border-gray-300 p-4 rounded-lg shadow-md bg-white"
            >
              <p className="font-bold">@{tweet.Handle}</p>
              <p className="text-sm text-gray-500">Followers: {tweet.Followers}</p>
              <p className="mt-2">{tweet.Tweet}</p>
              <p className="text-sm mt-2 text-gray-400">
                Likes: {tweet.Likes} | Retweets: {tweet.Retweets}
              </p>
              <p className="text-xs text-gray-500">📅 {new Date(tweet["Date Posted"]).toLocaleString()}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default TweetsList;
