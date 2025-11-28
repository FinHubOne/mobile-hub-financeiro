
import React from 'react';
import { DollarSign } from 'lucide-react';

const CashbackService = () => (
  <button className="service-item">
    <div className="service-icon-wrapper cashback-icon">
      <DollarSign />
    </div>
    <span className="service-label">Cashback</span>
  </button>
);

export default CashbackService;
