import React, { useRef, useState } from 'react';

const Draggable = ({ children }) => {
  const containerRef = useRef(null);
  const [isDown, setIsDown] = useState(false);
  const [startX, setStartX] = useState(0);
  const [scrollLeft, setScrollLeft] = useState(0);

  const handleMouseDown = (e) => {
    const container = containerRef.current;
    if (!container) return;

    setIsDown(true);
    container.classList.add('cursor-grabbing');
    setStartX(e.pageX - container.offsetLeft);
    setScrollLeft(container.scrollLeft);
  };

  const handleMouseLeave = () => {
    const container = containerRef.current;
    if (!container) return;

    setIsDown(false);
    container.classList.remove('cursor-grabbing');
  };

  const handleMouseUp = () => {
    const container = containerRef.current;
    if (!container) return;

    setIsDown(false);
    container.classList.remove('cursor-grabbing');
  };

  const handleMouseMove = (e) => {
    if (!isDown || !containerRef.current) return;
    e.preventDefault();
    const x = e.pageX - containerRef.current.offsetLeft;
    const walk = (x - startX) * 2; // O multiplicador * 2 acelera o scroll
    containerRef.current.scrollLeft = scrollLeft - walk;
  };

  return (
    <div
      ref={containerRef}
      className="flex overflow-x-auto space-x-4 cursor-grab select-none scrollbar-hide"
      onMouseDown={handleMouseDown}
      onMouseLeave={handleMouseLeave}
      onMouseUp={handleMouseUp}
      onMouseMove={handleMouseMove}
    >
      {children}
    </div>
  );
};

export default Draggable;
