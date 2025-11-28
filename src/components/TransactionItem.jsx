
import React from 'react';
import { Car, UtensilsCrossed, ShoppingBag, HeartPulse, Home, Film, Zap, CircleDollarSign, ArrowDownLeft } from 'lucide-react';

const categoryDetailsMap = {
  Transporte: { icon: Car, className: 'transport' },
  Alimentação: { icon: UtensilsCrossed, className: 'food' },
  Compras: { icon: ShoppingBag, className: 'shopping' },
  Saúde: { icon: HeartPulse, className: 'health' },
  Moradia: { icon: Home, className: 'housing' },
  Lazer: { icon: Film, className: 'leisure' },
  Pix: { icon: Zap, className: 'pix' },
  Outros: { icon: CircleDollarSign, className: 'others' },
  Salário: { icon: ArrowDownLeft, className: 'income' },
};

export const getCategoryDetails = (category, type) => {
  if (type === 'in') return { ...categoryDetailsMap.Salário, friendlyName: 'Salário' };
  const details = categoryDetailsMap[category] || categoryDetailsMap.Outros;
  return { ...details, friendlyName: category };
};

const DynamicIcon = ({ name, ...props }) => {
  const IconComponent = name;
  return IconComponent ? <IconComponent {...props} /> : null;
};

export const TransactionItem = ({ transaction, categoryDetails, style }) => {
  const details = categoryDetails || getCategoryDetails(transaction.category, transaction.type);
  const cleanDescription = transaction.clean_description || 'Processando...';
  
  const dateObj = new Date(transaction.date);
  const formattedDate = dateObj.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });

  const amountClass = `transaction-amount ${transaction.type}`;
  const amountSign = transaction.type === 'in' ? '+' : '-';
  const transactionClass = `transaction-item cat-${details.className}`;

  return (
    <div className={transactionClass} style={style}>
      <div className="transaction-icon">
        <DynamicIcon name={details.icon} size={20} />
      </div>
      <div className="transaction-details">
        <p>{cleanDescription}</p>
        <span>{details.friendlyName} • {formattedDate}</span>
      </div>
      <span className={amountClass}>
        {amountSign} R$ {Math.abs(transaction.amount).toFixed(2).replace('.', ',')}
      </span>
    </div>
  );
};
