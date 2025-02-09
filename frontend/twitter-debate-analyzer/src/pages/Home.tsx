import React, { useEffect, useState } from "react";
import axios from "axios";
import { CTweep, BodyWrapper, PunchWrap, Desc, BigWrapper, Logo, SongCard, CardContainer, Footer, TeamList, TeamMember } from "../styles/Home.modules";
import rugpullcoin42 from "../assets/rugpullcoin42.webp";
import BgAnimation from "./BgAnimation";

type Tweet = {
  Handle: string;
  Followers: number;
  Likes: number;
  Retweets: number;
  Tweet: string;
  "Date Posted": string;
};

const Home: React.FC = () => {
  const [tweets, setTweets] = useState<Tweet[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/tweets")
      .then((response) => {
        console.log("Fetched tweets:", response.data.tweets);
        const sortedTweets = response.data.tweets
          .sort((a: Tweet, b: Tweet) => (b.Likes + b.Retweets) - (a.Likes + a.Retweets))
          .slice(0, 4);
        setTweets(sortedTweets);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching tweets:", error);
        setLoading(false);
      });
  }, []);

  return (
    <>
      <BgAnimation /> {/* Background animation component */}

      <BigWrapper>
        <div>
          <Logo src={rugpullcoin42} alt="RugPullCoin42 Logo" />
          <CTweep>CrypTweep🚀</CTweep>
        </div>
        <BodyWrapper>
          <PunchWrap>Crypto Twitter is chaos—we make sense of it.</PunchWrap>
          <Desc>
            CrypTweep tracks and analyzes the hottest debates between top crypto influencers,
            breaking down the arguments, key players, and hidden narratives behind every clash.
          </Desc>

          {loading ? (
            <p>Loading tweets...</p>
          ) : (
            <CardContainer>
              {tweets.map((tweet, index) => (
                <SongCard key={index}>
                  <h1>{tweet.Tweet.length > 80 ? tweet.Tweet.slice(0, 80) + "..." : tweet.Tweet}</h1>
                  <h3>@{tweet.Handle} | ❤️ {tweet.Likes} | 🔄 {tweet.Retweets}</h3>
                </SongCard>
              ))}
            </CardContainer>
          )}
        </BodyWrapper>
      </BigWrapper>
      <AboutUs />
    </>
  );
};

const AboutUs = () => {
  return (
    <Footer>
      <h2>About Us</h2>
      <p>We are <strong>Team RugPullCoin#42</strong>, participants of <strong>ETH Oxford Hackathon 2025</strong>.  
         Our goal is to analyze and track crypto debates in real-time using AI-powered insights.</p>
      <h3>Meet the Team</h3>
      <TeamList>
        <TeamMember>
          <strong>Divit Kashyap</strong> – <a href="https://github.com/divitkashyap" target="_blank" rel="noopener noreferrer">GitHub</a>
        </TeamMember>
        <TeamMember>
          <strong>Tinaye Samuel Chibanda</strong> – <a href="https://github.com/TinayeSC" target="_blank" rel="noopener noreferrer">GitHub</a>
        </TeamMember>
        <TeamMember>
          <strong>Onett Perrera</strong> – <a href="https://github.com/onettonett" target="_blank" rel="noopener noreferrer">GitHub</a>
        </TeamMember>
      </TeamList>
    </Footer>
  );
};

export default Home;