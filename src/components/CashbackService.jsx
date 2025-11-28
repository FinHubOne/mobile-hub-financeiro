import React, { useState, useMemo } from 'react';
import { Target, Edit3, Check } from 'lucide-react';

const CashbackService = ({ savings }) => {
  const [goalName, setGoalName] = useState('Viagem de Férias');
  const [goalAmount, setGoalAmount] = useState(1000);
  const [isEditing, setIsEditing] = useState(false);

  const progress = useMemo(() => {
    if (goalAmount === 0) return 0;
    return Math.min((savings / goalAmount) * 100, 100); // Garante que não passe de 100%
  }, [savings, goalAmount]);

  const getMotivationalMessage = () => {
    if (progress >= 100) return { text: 'Parabéns! Meta alcançada! 🚀', color: 'text-green-600 dark:text-green-400' };
    if (progress > 75) return { text: 'Você está quase lá! Continue assim!', color: 'text-blue-600 dark:text-blue-400' };
    if (progress > 25) return { text: 'Ótimo começo! Cada passo conta.', color: 'text-indigo-600 dark:text-indigo-400' };
    return { text: 'Defina sua meta e comece a economizar!', color: 'text-gray-500' };
  };

  const message = getMotivationalMessage();

  return (
    <div className="animate-fade-in p-6 bg-white dark:bg-gray-800 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-700">
      <div className="flex justify-between items-start mb-4">
        <h2 className="text-xl font-bold flex items-center gap-2 text-gray-800 dark:text-gray-200">
          <Target className="text-purple-500 dark:text-purple-400" /> Cashback com Propósito
        </h2>
        <button onClick={() => setIsEditing(!isEditing)} className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
          {isEditing ? <Check size={18} className="text-green-500" /> : <Edit3 size={18} className="text-gray-500" />}
        </button>
      </div>

      {isEditing ? (
        <div className="space-y-3 mb-4 animate-fade-in">
          <div>
            <label className="text-xs font-medium text-gray-500 dark:text-gray-400">Nome da Meta</label>
            <input 
              type="text"
              value={goalName}
              onChange={(e) => setGoalName(e.target.value)}
              className="w-full p-2 mt-1 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
            />
          </div>
          <div>
            <label className="text-xs font-medium text-gray-500 dark:text-gray-400">Valor da Meta (R$)</label>
            <input 
              type="number"
              value={goalAmount}
              onChange={(e) => setGoalAmount(Number(e.target.value))}
              className="w-full p-2 mt-1 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 outline-none"
            />
          </div>
        </div>
      ) : (
        <div className="mb-4">
          <p className="text-2xl font-bold text-purple-800 dark:text-purple-300">{goalName}</p>
        </div>
      )}

      <div>
        <div className="flex justify-between items-end mb-1">
            <p className="text-sm font-medium text-gray-600 dark:text-gray-300">Progresso</p>
            <p className="text-sm font-bold text-purple-800 dark:text-purple-300">R$ {savings.toFixed(2)} / R$ {goalAmount.toFixed(2)}</p>
        </div>
        <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-4 overflow-hidden">
          <div 
            className="bg-purple-500 h-4 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${progress}%` }}
          ></div>
        </div>
        <p className={`text-center text-sm font-semibold mt-3 ${message.color}`}>{message.text}</p>
      </div>

    </div>
  );
};

export default CashbackService;
