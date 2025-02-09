import styled from "styled-components";

export const Summarian = styled.div`
    font-family: 'Madeleina Sans';
    font-size: 1.6rem;
    background: rgba(255, 255, 255, 0.1); /* Match Footer */
    color: white;
    text-align: center;
    padding: 2rem;
    border-radius: 10px;
    margin-top: 2rem;
`;

export const GradientBG = styled.div`
  width: 100vw;
  height: 100vh;
  position: fixed;
  overflow: hidden;
  background: linear-gradient(40deg, rgb(108, 0, 162), rgb(0, 17, 82));
  top: 0;
  left: 0;
  z-index: -1;

  svg {
    position: fixed;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
  }

  .gradients-container {
    filter: url(#goo) blur(40px);
    width: 100%;
    height: 100%;
  }

  .g1, .g2, .g3, .g4, .g5 {
    position: absolute;
    mix-blend-mode: hard-light;
    width: 80%;
    height: 80%;
    top: 50%;
    left: 50%;
    transform-origin: center center;
    animation: moveInCircle 30s ease infinite;
  }

  .g1 { background: radial-gradient(circle at center, rgba(18, 113, 255, 0.8) 0, rgba(18, 113, 255, 0) 50%); }
  .g2 { background: radial-gradient(circle at center, rgba(221, 74, 255, 0.8) 0, rgba(221, 74, 255, 0) 50%); }
  .g3 { background: radial-gradient(circle at center, rgba(100, 220, 255, 0.8) 0, rgba(100, 220, 255, 0) 50%); }
  .g4 { background: radial-gradient(circle at center, rgba(200, 50, 50, 0.8) 0, rgba(200, 50, 50, 0) 50%); }
  .g5 { background: radial-gradient(circle at center, rgba(180, 180, 50, 0.8) 0, rgba(180, 180, 50, 0) 50%); }

  @keyframes moveInCircle {
    0% { transform: rotate(0deg); }
    50% { transform: rotate(180deg); }
    100% { transform: rotate(360deg); }
  }
`;


export const BigWrapper = styled.div`
 display: flex;
  flex-direction: column;  /* ✅ Stack elements top to bottom */
  align-items: center;  /* ✅ Keep everything centered */
  justify-content: center;
  width: 100%;


  .basedC {
    font-family: 'Newake';
    font-size: 1.8rem;
    color: white;
  }
`;

export const CTweep = styled.div`
    position: absolute;
    top: 0px;
    left: 10%;
    font-family: 'Newake';
    font-size: 5rem;
    color: white;
    text-shadow: 0px 0px 15px rgba(255, 255, 255, 0.5), 
                 0px 0px 10px rgba(255, 255, 255, 0.3);
`;


export const BodyWrapper = styled.div`
    display: flex;
    margin-top: 3.5rem;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 2rem 0;
`;


export const PunchWrap = styled.div`
    font-family: 'Newake';
    font-size: 1.65rem;
    color: white;`

export const Desc = styled.div`
    font-family: 'Madeleina Sans';
    font-size: 1.65rem;`

export const Logo = styled.img`
    position: absolute;
    top: 10px;
    left: 10px;
    width: 80px;  /* Adjust size as needed */
    height: auto;
`;

export const CardContainer = styled.div`
  margin-top: 1rem;
  display: flex;
  flex-wrap: wrap;  /* ✅ Allow wrapping to prevent squishing */
  justify-content: center;
  gap: 1rem;
  max-width: 90%;  /* ✅ Give the container more space */
  margin-left: auto;
  margin-right: auto;
`;


export const Footer = styled.footer`
  font-family: 'Madeleina Sans';
  font-size: 1.8rem;
  text-align: center;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border-radius: 10px;
  width: 100%;
  margin-top: auto;  /* ✅ Push footer to bottom */
`;


export const TeamList = styled.div`
    font-family: 'Madeleina Sans';
    font-size: 1.6rem;
  display: flex;
  justify-content: center;
  gap: 0.2rem;
  /* margin-top: 1rem; */
`;

export const TeamMember = styled.div`
    font-family: 'Abigate Desgo';
  font-size: 1.2rem;
  a {
    color: #00bfff;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
`;


export const SongCard = styled.div`
  font-size: 1rem;
  background-color: rgb(127, 143, 189); 
  border-radius: 15px;
  width: 280px;  /* 🔹 Increased width */
  transition: transform 0.3s ease;
  cursor: pointer;
  color: white;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1), 0 5px 22px rgba(150, 160, 174, 0.6);
  text-align: center;
  height: auto;  /* 🔹 Adjust height dynamically */
  padding: 15px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  word-wrap: break-word;

  h1 {
    font-size: 1rem; /* Adjusted for better fit */
    font-weight: bold;
    text-overflow: ellipsis;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
  }

  h3 {
    font-size: 0.9rem;
    margin-top: auto;
    opacity: 0.9;
  }

  &:hover {
    transform: scale(1.05);
  }

  @media (max-width: 1160px) {
    width: 250px; /* 🔹 Adjusted for responsiveness */
  }
`;


