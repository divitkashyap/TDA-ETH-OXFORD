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
                                Your Power
                            </h1>
                            <h3>
                                Billie Eilish
                            </h3>
                        </SongCard>

                        <SongCard>
                            <h1 className="cardSong">
                                Perfect
                            </h1>
                            <h3 className="cardArtist">
                                Ed Sheeran
                            </h3>
                        </SongCard>

                        <SongCard>
                            <h1 className="cardSong">
                                Sparks
                            </h1>
                            <h3 className="cardArtist">
                                Coldplay
                            </h3>
                        </SongCard>

                        <SongCard>
                            <h1 className="cardSong">
                                Tush
                            </h1>
                            <h3 className="cardArtist">
                                Fandango!
                            </h3>
                        </SongCard>
                    </CardContainer>
    </BodyWrapper>
    </BigWrapper>
    </>

  )
};

export default Home;