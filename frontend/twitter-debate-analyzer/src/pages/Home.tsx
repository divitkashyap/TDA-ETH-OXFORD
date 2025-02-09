import React, { useEffect, useState } from "react";
import axios from "axios";
import { CTweep, BodyWrapper, PunchWrap, Desc, BigWrapper, Logo, SongCard, CardContainer, Footer, TeamList, TeamMember, Summarian } from "../styles/Home.modules";
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
  const [influentialTweets, setInfluentialTweets] = useState<Tweet[]>([]);
  const [normalTweets, setNormalTweets] = useState<Tweet[]>([]);
  const [loading, setLoading] = useState(true);
  const [summary, setSummary] = useState<string>("");
  const [plotUrls, setPlotUrls] = useState<{ plot1: string; plot2: string }>({ plot1: "", plot2: "" });

  useEffect(() => {
    // Fetch summary
    axios.get("http://127.0.0.1:8000/summary")
      .then((response) => setSummary(response.data.summary))
      .catch((error) => console.error("Error fetching summary:", error));

    // Set static plot URLs
    setPlotUrls({
      plot1: "http://127.0.0.1:8000/static/plot1.png",
      plot2: "http://127.0.0.1:8000/static/plot2.png",
    });

// Fetch influential tweets
axios.get("http://127.0.0.1:8000/influential")
  .then((response) => {
    if (Array.isArray(response.data.important)) {
      setInfluentialTweets(response.data.important.slice(0, 4));
    } else {
      console.error("Unexpected format for influential tweets:", response.data.important);
    }
  })
  .catch((error) => console.error("Error fetching influential tweets:", error));


    // Fetch normal tweets
    axios.get("http://127.0.0.1:8000/tweets")
      .then((response) => {
        const sortedTweets = response.data.tweets
          .sort((a: Tweet, b: Tweet) => (b.Likes + b.Retweets) - (a.Likes + a.Retweets));
        setNormalTweets(sortedTweets);
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
            <>
              <h2 style={{ textAlign: "center", color: "white" }}>🔥 Influential Tweets</h2>
              <CardContainer>
                {influentialTweets.map((tweet, index) => (
                  <SongCard key={index}>
                    <h1>{tweet.Tweet}</h1>
                    <h3>@{tweet.Handle} | ❤️ {tweet.Likes} | 🔄 {tweet.Retweets}</h3>
                  </SongCard>
                ))}
              </CardContainer>

              {/* Summary Section */}
              <Summarian>
                <div style={{ marginTop: "20px", padding: "20px", backgroundColor: "rgba(255, 255, 255, 0.1)", borderRadius: "10px", color: "white" }}>
                  <h2>Trending Crypto Summary</h2>
                  <p>{summary || "Loading summary..."}</p>
                </div>

                {/* Sentiment Plots */}
                <div style={{ marginTop: "20px", textAlign: "center" }}>
                  <h2>Crypto Twitter Sentiment Breakdown</h2>
                  {plotUrls.plot1 && (
                    <img
                      src={plotUrls.plot1}
                      alt="Sentiment Breakdown"
                      style={{
                        width: "60%",
                        maxWidth: "500px",
                        height: "auto",
                        borderRadius: "10px",
                        padding: "10px"
                      }}
                    />
                  )}
                  {plotUrls.plot2 && (
                    <img
                      src={plotUrls.plot2}
                      alt="Likes Breakdown"
                      style={{
                        width: "60%",
                        maxWidth: "500px",
                        height: "auto",
                        borderRadius: "10px",
                        padding: "10px",
                        marginTop: "10px"
                      }}
                    />
                  )}
                </div>
              </Summarian>

              {/* Normal Tweets After Summary */}
              <h2 style={{ textAlign: "center", color: "white", marginTop: "2rem" }}>💬 Other Crypto Tweets</h2>
              <CardContainer>
  {normalTweets.length > 0 ? (
    normalTweets.map((tweet, index) => (
      <SongCard key={index}>
        <h1>{tweet.Tweet}</h1>
        <h3>@{tweet.Handle} | ❤️ {tweet.Likes} | 🔄 {tweet.Retweets}</h3>
      </SongCard>
    ))
  ) : (
    <p style={{ color: "white", textAlign: "center" }}>No regular tweets available.</p>
  )}
</CardContainer>

            </>
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
