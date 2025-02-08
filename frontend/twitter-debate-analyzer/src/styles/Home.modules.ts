import styled from "styled-components"

export const BigWrapper = styled.div`
position: relative;
`
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
    position: absolute;
    font-family: 'newake';
    justify-content: center;
    top: 120px;
    left: 0;
    right: 0;
    `

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
  justify-content: center;
  gap: 1rem;
`;

export const Footer = styled.footer`
font-family: 'Madeleina Sans';
font-size: 1.8rem;
  text-align: center;
  margin-top: 40rem;
  margin-bottom: 0;
  padding: 2rem;
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border-radius: 10px;
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
    width: 350px;
    transition: transform 0.3s ease;
    cursor: pointer;
    color: white;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1), 0 5px 22px rgba(150, 160, 174, 0.6);
    text-align: center;
    height: 150px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    word-wrap: break-word;

    h1 {
        font-size: 1.2rem; /* Adjust tweet text size */
        font-weight: bold;
        text-overflow: ellipsis;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 3; /* Limit to 3 lines */
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
    width: 300px;
  }
`;