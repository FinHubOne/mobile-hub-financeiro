
import React from 'react';
import { Zap } from 'lucide-react';

const PixService = () => (
  <button className="service-item">
    <div className="service-icon-wrapper pix-icon">
      <Zap />
    </div>
    <span className="service-label">Pix</span>
  </button>
);

export default PixService;
