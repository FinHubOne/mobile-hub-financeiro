
import React from 'react';
import { Smartphone } from 'lucide-react';

const RecargaService = () => (
  <button className="service-item">
    <div className="service-icon-wrapper recarga-icon">
      <Smartphone />
    </div>
    <span className="service-label">Recarga</span>
  </button>
);

export default RecargaService;
