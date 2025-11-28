import React, { useState, useMemo } from 'react';
import { Shield, Briefcase, Smartphone, Plane, Sparkles } from 'lucide-react';

// Um pequeno componente de Switch (interruptor) para o toggle
const Switch = ({ checked, onChange }) => (
  <button
    type="button"
    className={`${checked ? 'bg-blue-600' : 'bg-gray-200 dark:bg-gray-600'} relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2`}
    onClick={onChange}
  >
    <span
      className={`${checked ? 'translate-x-5' : 'translate-x-0'} pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out`}
    />
  </button>
);

const InsuranceItem = ({ icon, title, description, isEnabled, onToggle }) => (
  <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700/[.5] rounded-xl">
    <div className="flex items-center gap-4">
      <div className="p-3 bg-white dark:bg-gray-600 rounded-full shadow-sm">
        {icon}
      </div>
      <div>
        <h3 className="font-bold text-gray-800 dark:text-gray-200">{title}</h3>
        <p className="text-xs text-gray-500 dark:text-gray-400">{description}</p>
      </div>
    </div>
    <Switch checked={isEnabled} onChange={onToggle} />
  </div>
);


// O componente principal do serviço de Seguros
const InsuranceService = ({ transactions, processedTransactions }) => {
  const [enabledInsurances, setEnabledInsurances] = useState({ 
    celular: false,
    transacoes: true, // Começa ativo por padrão
    bolsa: false,
  });

  const handleToggle = (insurance) => {
    setEnabledInsurances(prev => ({ ...prev, [insurance]: !prev[insurance] }));
  };

  // --- A "INTELIGÊNCIA" DO COMPONENTE ---
  // Analisa as transações para encontrar sugestões relevantes.
  const suggestedInsurance = useMemo(() => {
    const travelKeywords = ['latam', 'gol', 'azul', 'decolar', 'booking', 'hotel', 'passagem'];
    const phoneKeywords = ['apple', 'samsung', 'motorola', 'xiaomi', 'vivo', 'claro', 'tim'];

    for (const tx of transactions) {
      const processed = processedTransactions[tx.id];
      if (!processed) continue;

      const lowerDesc = processed.cleanDescription.toLowerCase();

      if (travelKeywords.some(keyword => lowerDesc.includes(keyword))) {
        return {
          key: 'viagem',
          icon: <Plane className="text-cyan-500" />,
          title: 'Seguro Viagem Detectado',
          description: `Vimos sua compra em "${processed.cleanDescription}". Que tal ativar uma proteção para sua viagem?`,
        };
      }
      if (phoneKeywords.some(keyword => lowerDesc.includes(keyword))) {
        return {
          key: 'celular_compra',
          icon: <Smartphone className="text-purple-500" />,
          title: 'Proteção para Celular Sugerida',
          description: `Acabou de comprar em "${processed.cleanDescription}". Proteja seu novo aparelho!`,
        };
      }
    }
    return null; // Nenhuma sugestão encontrada
  }, [transactions, processedTransactions]);


  return (
    <div className="animate-fade-in p-6 bg-white dark:bg-gray-800 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-700">
      <h2 className="text-xl font-bold mb-6 flex items-center gap-2 text-gray-800 dark:text-gray-200">
        <Shield className="text-blue-500" /> Seguro On-Demand
      </h2>

      {/* Seção de Sugestões (A Mágica Acontece Aqui) */}
      {suggestedInsurance && (
        <div className="mb-8 animate-fade-in">
            <h3 className="text-sm font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400 mb-3 flex items-center gap-2">
                <Sparkles size={16} /> Sugestão para você
            </h3>
            <div className="p-4 border-2 border-blue-400 bg-blue-50 dark:bg-blue-900/[.2] rounded-2xl">
                <div className="flex justify-between items-center mb-2">
                <h3 className="font-bold text-blue-900 dark:text-blue-200 flex items-center gap-3">
                    {suggestedInsurance.icon} {suggestedInsurance.title}
                </h3>
                </div>
                <p className="text-sm text-blue-800 dark:text-blue-300 mb-4">{suggestedInsurance.description}</p>
                <button className="w-full text-center bg-blue-500 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors">
                    Ativar Proteção de Viagem
                </button>
            </div>
        </div>
      )}

      {/* Seção de Outras Proteções */}
      <div className="space-y-3">
         <h3 className="text-sm font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-3">Outras Proteções</h3>
        <InsuranceItem 
          icon={<Smartphone className="text-purple-500" />}
          title="Proteção de Celular"
          description="Cobertura para roubo e danos"
          isEnabled={enabledInsurances.celular}
          onToggle={() => handleToggle('celular')}
        />
        <InsuranceItem 
          icon={<Shield className="text-green-500" />}
          title="Proteção de Transações"
          description="Segurança extra para seu PIX"
          isEnabled={enabledInsurances.transacoes}
          onToggle={() => handleToggle('transacoes')}
        />
        <InsuranceItem 
          icon={<Briefcase className="text-orange-500" />}
          title="Bolsa Protegida"
          description="Seus pertences seguros fora de casa"
          isEnabled={enabledInsurances.bolsa}
          onToggle={() => handleToggle('bolsa')}
        />
      </div>
    </div>
  );
};

export default InsuranceService;
