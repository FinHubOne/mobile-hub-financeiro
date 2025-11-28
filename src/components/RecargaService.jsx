import React, { useState } from 'react';
import { Smartphone, ArrowRight, CheckCircle } from 'lucide-react';

const operators = [
  { name: 'Vivo', logo: '/vivo.png', sizeClass: 'h-14' },
  { name: 'Claro', logo: '/claro.png', sizeClass: 'h-12' },
  { name: 'TIM', logo: '/tim.png', sizeClass: 'h-14' },
  { name: 'Oi', logo: '/oi.png', sizeClass: 'h-12' },
];

const rechargeValues = [15, 20, 30, 50, 100];

const RecargaService = () => {
  const [phone, setPhone] = useState('');
  const [selectedOperator, setSelectedOperator] = useState(null);
  const [selectedValue, setSelectedValue] = useState(null);
  const [isCompleted, setIsCompleted] = useState(false);

  const handleRecharge = () => {
    if (phone && selectedOperator && selectedValue) {
      setIsCompleted(true);
    }
  };

  if (isCompleted) {
    return (
      <div className="bg-white dark:bg-zinc-800 p-6 rounded-2xl shadow-lg border border-gray-200 dark:border-zinc-700 text-center">
        <CheckCircle className="text-green-500 mx-auto mb-4" size={48} />
        <h3 className="text-lg font-bold mb-2">Recarga Realizada!</h3>
        <p className="text-gray-600 dark:text-zinc-300">
          A recarga de R$ {selectedValue},00 para o número {phone} foi efetuada com sucesso.
        </p>
        <button onClick={() => setIsCompleted(false)} className="mt-6 bg-blue-600 text-white py-2 px-4 rounded-lg w-full hover:bg-blue-700 transition-colors">
          Fazer Nova Recarga
        </button>
      </div>
    )
  }

  return (
    <div className="bg-white dark:bg-zinc-800 p-6 rounded-2xl shadow-lg border border-gray-200 dark:border-zinc-700">
      <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
        <Smartphone size={22} /> Recarga de Celular
      </h3>

      <div className="mb-4">
        <label className="font-semibold text-sm mb-2 block">Número com DDD</label>
        <input 
          type="tel" 
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
          placeholder="(11) 99999-9999"
          className="w-full p-3 rounded-lg bg-gray-100 dark:bg-zinc-700 focus:ring-2 focus:ring-blue-500 outline-none transition-shadow"
        />
      </div>

      <div className="mb-4">
        <label className="font-semibold text-sm mb-2 block">Operadora</label>
        <div className="grid grid-cols-4 gap-2">
          {operators.map(op => (
            <button 
              key={op.name}
              onClick={() => setSelectedOperator(op.name)}
              className={`p-3 rounded-lg border-2 flex items-center justify-center transition-all ${selectedOperator === op.name ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/30' : 'border-gray-200 dark:border-zinc-700'}`}>
              <img src={op.logo} alt={op.name} className={`${op.sizeClass} mx-auto object-contain`} />
            </button>
          ))}
        </div>
      </div>

      <div className="mb-6">
        <label className="font-semibold text-sm mb-2 block">Valor da Recarga</label>
        <div className="grid grid-cols-3 gap-2">
          {rechargeValues.map(val => (
            <button 
              key={val}
              onClick={() => setSelectedValue(val)}
              className={`p-3 rounded-lg border-2 font-bold flex items-center justify-center transition-all ${selectedValue === val ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-300' : 'border-gray-200 dark:border-zinc-700'}`}>
              R${val}
            </button>
          ))}
        </div>
      </div>

      <button 
        onClick={handleRecharge}
        disabled={!phone || !selectedOperator || !selectedValue}
        className="w-full bg-blue-600 text-white font-bold py-4 rounded-lg hover:bg-blue-700 transition-all flex items-center justify-center gap-2 disabled:bg-gray-300 disabled:dark:bg-zinc-700 disabled:cursor-not-allowed"
      >
        Recarregar <ArrowRight size={20} />
      </button>
    </div>
  );
};

export default RecargaService;
