import React, { useEffect, useRef } from "react";
import styled from "styled-components";

// Styled component for full-page canvas
const CanvasBackground = styled.canvas`
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1; /* Ensures it stays behind content */
`;

const BackgroundAnimation: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return; // ✅ Check if canvas exists

    const ctx = canvas.getContext("2d");
    if (!ctx) return; // ✅ Check if context is available

    // Function to resize canvas dynamically
    const resizeCanvas = () => {
      if (!canvas) return;
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    resizeCanvas(); // ✅ Initial setup
    window.addEventListener("resize", resizeCanvas);

    let particles: Particle[] = [];
    const particleCount = 50;

    class Particle {
      x: number;
      y: number;
      radius: number;
      speedX: number;
      speedY: number;

      constructor() {
        this.x = Math.random() * (canvas?.width || 0);
        this.y = Math.random() * (canvas?.height || 0);
        this.radius = Math.random() * 3 + 1;
        this.speedX = Math.random() * 2 - 1;
        this.speedY = Math.random() * 2 - 1;
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        // Bounce inside the canvas
        if (canvas && (this.x > canvas.width || this.x < 0)) this.speedX *= -1;
        if (canvas && (this.y > canvas.height || this.y < 0)) this.speedY *= -1;
      }

      draw() {
        if (!ctx) return; // ✅ Ensure ctx is available
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(255, 255, 255, 0.5)"; // ✅ Glow effect
        ctx.fill();
      }
    }

    // Create particles
    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    // Animation loop
    const animate = () => {
      if (!ctx || !canvas) return;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach((particle) => {
        particle.update();
        particle.draw();
      });

      requestAnimationFrame(animate);
    };

    animate();

    // Cleanup function
    return () => {
      window.removeEventListener("resize", resizeCanvas);
    };
  }, []);

  return <CanvasBackground ref={canvasRef} />;
};

export default BackgroundAnimation;
