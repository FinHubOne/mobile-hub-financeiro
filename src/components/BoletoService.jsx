import React, { useState } from 'react';
import { Search, Loader } from 'lucide-react';

const BoletoService = () => {
  const [document, setDocument] = useState('');
  const [loading, setLoading] = useState(false);
  const [boletos, setBoletos] = useState([]);

  const handleSearch = () => {
    if (!document) return;
    setLoading(true);
    // Simulação de busca de boletos
    setTimeout(() => {
      setBoletos([
        { id: 1, name: 'Conta de Luz - Eletropaulo', value: '150,00', dueDate: '10/12/2023' },
        { id: 2, name: 'Aluguel - Imobiliária Central', value: '1.200,00', dueDate: '15/12/2023' },
      ]);
      setLoading(false);
    }, 1500);
  };

  return (
    <div className="bg-white dark:bg-zinc-800 p-6 rounded-2xl shadow-lg border border-gray-200 dark:border-zinc-700">
      <h3 className="text-lg font-bold mb-4">Buscar Boletos (DDA)</h3>
      <p className="text-sm text-gray-500 dark:text-zinc-400 mb-4">
        Consulte e pague os boletos registrados no seu CPF ou CNPJ de forma automática.
      </p>
      
      <div className="flex items-center gap-2 mb-4">
        <input 
          type="text" 
          value={document}
          onChange={(e) => setDocument(e.target.value)}
          placeholder="Digite seu CPF ou CNPJ"
          className="flex-grow p-3 rounded-lg bg-gray-100 dark:bg-zinc-700 focus:ring-2 focus:ring-blue-500 outline-none transition-shadow"
        />
        <button 
          onClick={handleSearch}
          className="bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700 transition-colors flex items-center justify-center h-full aspect-square"
        >
          {loading ? <Loader className="animate-spin" size={20} /> : <Search size={20} />}
        </button>
      </div>

      {boletos.length > 0 && (
        <div className="space-y-3 mt-6">
            <h4 className="font-bold">Boletos Encontrados</h4>
            {boletos.map(boleto => (
                <div key={boleto.id} className="bg-gray-50 dark:bg-zinc-700/50 p-4 rounded-lg flex justify-between items-center">
                    <div>
                        <p className="font-semibold">{boleto.name}</p>
                        <p className="text-sm text-gray-500 dark:text-zinc-400">Vencimento: {boleto.dueDate}</p>
                    </div>
                    <div className="text-right">
                        <p className="font-bold text-lg">R$ {boleto.value}</p>
                        <button className="text-sm text-blue-600 dark:text-blue-400 font-semibold hover:underline">Pagar</button>
                    </div>
                </div>
            ))}
        </div>
      )}
    </div>
  );
};

export default BoletoService;
