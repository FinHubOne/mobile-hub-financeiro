
import React from 'react';
import { Shield } from 'lucide-react';

const InsuranceService = () => (
  <button className="service-item">
    <div className="service-icon-wrapper insurance-icon">
      <Shield />
    </div>
    <span className="service-label">Seguros</span>
  </button>
);

export default InsuranceService;
