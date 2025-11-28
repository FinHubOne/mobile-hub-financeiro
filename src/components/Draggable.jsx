
import React, { useRef, useState, useEffect } from 'react';

const Draggable = ({ children, onPull }) => {
  const containerRef = useRef(null);
  const [isDragging, setIsDragging] = useState(false);
  const [startY, setStartY] = useState(0);
  const [initialScrollTop, setInitialScrollTop] = useState(0);
  const [resistance, setResistance] = useState(0);

  const PULL_THRESHOLD = 70; // How far the user needs to pull down
  const RESISTANCE_FACTOR = 0.6; // How much resistance to apply

  useEffect(() => {
    const node = containerRef.current;
    if (!node) return;

    const handleTouchStart = (e) => {
      if (node.scrollTop === 0) {
        setStartY(e.touches[0].pageY);
        setIsDragging(true);
        setInitialScrollTop(node.scrollTop);
      }
    };

    const handleTouchMove = (e) => {
      if (!isDragging) return;

      const currentY = e.touches[0].pageY;
      let diff = currentY - startY;

      if (diff > 0 && node.scrollTop === 0) {
        e.preventDefault(); // Prevent page scroll
        const newResistance = diff * RESISTANCE_FACTOR;
        setResistance(newResistance);

        // If threshold is met, trigger the action and reset
        if (newResistance > PULL_THRESHOLD) {
          onPull();
          resetState();
        }
      }
    };

    const handleTouchEnd = () => {
      if (isDragging) {
        resetState();
      }
    };

    const resetState = () => {
      setIsDragging(false);
      setStartY(0);
      setResistance(0);
    };

    // Attach event listeners
    node.addEventListener('touchstart', handleTouchStart, { passive: false });
    node.addEventListener('touchmove', handleTouchMove, { passive: false });
    node.addEventListener('touchend', handleTouchEnd);

    // Cleanup
    return () => {
      node.removeEventListener('touchstart', handleTouchStart);
      node.removeEventListener('touchmove', handleTouchMove);
      node.removeEventListener('touchend', handleTouchEnd);
    };

  }, [isDragging, startY, onPull]);

  const style = {
    transform: `translateY(${resistance}px)`,
    transition: isDragging ? 'none' : 'transform 0.3s ease-out',
  };

  return (
    <div ref={containerRef} style={style} className="draggable-container">
      {children}
    </div>
  );
};

export default Draggable;
