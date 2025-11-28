import React from 'react';
import { Car, UtensilsCrossed, ShoppingBag, HeartPulse, Home, Film, Zap, CircleDollarSign, ArrowDownLeft } from 'lucide-react';

const categoryDetails = {
  Transporte: { icon: Car, color: 'blue', friendlyName: 'Transporte' },
  Alimentação: { icon: UtensilsCrossed, color: 'orange', friendlyName: 'Alimentação' },
  Compras: { icon: ShoppingBag, color: 'purple', friendlyName: 'Compras' },
  Saúde: { icon: HeartPulse, color: 'pink', friendlyName: 'Saúde' },
  Moradia: { icon: Home, color: 'red', friendlyName: 'Moradia' },
  Lazer: { icon: Film, color: 'yellow', friendlyName: 'Lazer' },
  Pix: { icon: Zap, color: 'green', friendlyName: 'Pix' },
  Outros: { icon: CircleDollarSign, color: 'gray', friendlyName: 'Outros' },
  Entrada: { icon: ArrowDownLeft, color: 'green', friendlyName: 'Entrada' },
};

export const getCategoryDetails = (category, type) => {
  if (type === 'in') return categoryDetails.Entrada;
  return categoryDetails[category] || categoryDetails.Outros;
};

const DynamicIcon = ({ name, ...props }) => {
  const IconComponent = name;
  return IconComponent ? <IconComponent {...props} /> : null;
};

export const TransactionItem = ({ transaction, categoryDetails, style }) => {
  // The `processed` prop has been removed.
  // `categoryDetails` is reliably passed from `app.jsx` based on `transaction.category`.
  const details = categoryDetails || getCategoryDetails(transaction.category, transaction.type);
  
  // Use the `clean_description` from the transaction object, with a fallback.
  const cleanDescription = transaction.clean_description || 'Processando...';
  
  const dateObj = new Date(transaction.date);
  const formattedDate = dateObj.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });

  const amountColor = transaction.type === 'in' ? 'text-green-500' : 'text-gray-900 dark:text-gray-100';
  const amountSign = transaction.type === 'in' ? '+' : '-';

  return (
    <div className="flex items-center justify-between p-3 -mx-3 rounded-2xl hover:bg-gray-100 dark:hover:bg-zinc-800 transition-colors duration-200 animate-fade-in-up" style={style}>
      <div className="flex items-center gap-4">
        <div className={`h-11 w-11 rounded-full flex items-center justify-center bg-${details.color}-100 dark:bg-${details.color}-500/10`}>
          <DynamicIcon name={details.icon} size={20} className={`text-${details.color}-500`} />
        </div>
        <div>
          <p className="font-bold text-base">{cleanDescription}</p>
          <p className="text-sm text-gray-500 dark:text-zinc-400">{details.friendlyName} • {formattedDate}</p>
        </div>
      </div>
      <span className={`font-bold text-base ${amountColor}`}>
        {amountSign} R$ {Math.abs(transaction.amount).toFixed(2).replace('.', ',')}
      </span>
    </div>
  );
};
