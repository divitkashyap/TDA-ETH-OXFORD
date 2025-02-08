import React, { useEffect, useState } from "react";
import styled from "styled-components";
import axios from "axios";
import { CTweep, BodyWrapper, PunchWrap, Desc, BigWrapper, Logo, SongCard, CardContainer } from "../styles/Home.modules";
import rugpullcoin42 from "../assets/rugpullcoin42.webp";

function Home() {
  return (
    <>
    <BigWrapper>
    <div>
    <Logo src={rugpullcoin42} alt="RugPullCoin42 Logo" />
    <CTweep>CrypTweep🚀</CTweep>
    </div>
    <BodyWrapper>
        <PunchWrap>Crypto Twitter is chaos—we make sense of it.</PunchWrap>
        <Desc>CrypTweep tracks and analyzes the hottest debates between top crypto influencers, breaking down the arguments, key players, and hidden narratives behind every clash.</Desc>
        <CardContainer>
                        <SongCard>
                            <h1>
                                Tweet 1
                            </h1>
                            <h3>
                                Elon's Musk
                            </h3>
                        </SongCard>

                        <SongCard>
                            <h1 className="cardSong">
                                Tweet 2
                            </h1>
                            <h3 className="cardArtist">
                                Kanye's West
                            </h3>
                        </SongCard>

                        <SongCard>
                            <h1 className="cardSong">
                                Tweet 3
                            </h1>
                            <h3 className="cardArtist">
                                Bill's Gates
                            </h3>
                        </SongCard>

                        <SongCard>
                            <h1 className="cardSong">
                                Tweet 4
                            </h1>
                            <h3 className="cardArtist">
                                Steve's Jobs
                            </h3>
                        </SongCard>
                    </CardContainer>
    </BodyWrapper>
    </BigWrapper>
    </>

  )
};

export default Home;