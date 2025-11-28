
import React from 'react';
import { FileText } from 'lucide-react';

const BoletoService = () => (
  <button className="service-item">
    <div className="service-icon-wrapper boleto-icon">
      <FileText />
    </div>
    <span className="service-label">Pagar</span>
  </button>
);

export default BoletoService;
