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
`

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
    font-size: 1.5rem;`

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

export const SongCard = styled.div`
  background-color: ${props => props.theme.cardBg};
  background-color:rgb(127, 143, 189); 
  border-radius: 15px;
  width: 350px;
  transition: transform 0.3s ease;
  cursor: pointer;
  color: white;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1), 0 0 12px rgba(200, 150, 220, 0.6);
  text-align: center;
  height: 210px;
  
  
  &:hover {
    transform: scale(1.05);
  }

  @media (max-width:1160px) {
    
  }
`;


