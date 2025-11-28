import React, { useState } from 'react';
import { Zap, Search, User, X, Loader } from 'lucide-react';

// --- DADOS SIMULADOS ---
const MOCK_RECIPIENTS = {
  'amigo@email.com': { name: 'João Silva', document: '***.123.456-**', bank: 'Banco Digital S.A.' },
  '12345678901': { name: 'Maria Oliveira', document: '***.987.654-**', bank: 'Banco Nacional' },
  'a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d': { name: 'Comércio Varejista Ltda', document: '**.123.456/0001-**', bank: 'Banco Comercial' },
};

const PixService = () => {
  const [pixKey, setPixKey] = useState('');
  const [recipient, setRecipient] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleKeyLookup = () => {
    if (!pixKey) return;
    setIsLoading(true);
    setError(null);
    setRecipient(null);

    // Simula uma chamada de API (rede)
    setTimeout(() => {
      const foundRecipient = MOCK_RECIPIENTS[pixKey];
      if (foundRecipient) {
        setRecipient(foundRecipient);
      } else {
        setError('Chave PIX não encontrada. Verifique os dados e tente novamente.');
      }
      setIsLoading(false);
    }, 1500); // Atraso de 1.5s para simular a realidade
  };

  const resetState = () => {
    setPixKey('');
    setRecipient(null);
    setError(null);
    setIsLoading(false);
  }

  return (
    <div className="animate-fade-in p-6 bg-white dark:bg-zinc-800 rounded-3xl shadow-sm border border-gray-100 dark:border-zinc-700">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold flex items-center gap-2">
          <Zap className="text-yellow-500" /> Simular PIX
        </h2>
        {(recipient || error) && (
            <button onClick={resetState} className="p-1.5 rounded-full hover:bg-gray-100 dark:hover:bg-zinc-700">
                <X size={20} className="text-gray-500"/>
            </button>
        )}
      </div>

      {!recipient && (
        <div className="mt-4">
          <p className="text-sm text-gray-600 dark:text-gray-300 mb-2">Digite uma chave PIX para simular a busca:</p>
          <div className="flex gap-2">
            <input 
              type="text"
              value={pixKey}
              onChange={(e) => setPixKey(e.target.value)}
              placeholder='Email, CPF/CNPJ ou Chave Aleatória'
              className="flex-grow p-3 text-lg bg-gray-50 dark:bg-zinc-700 border border-gray-200 dark:border-zinc-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-500"
            />
            <button 
              onClick={handleKeyLookup}
              disabled={isLoading}
              className="p-3 bg-slate-900 dark:bg-slate-700 text-white rounded-xl flex items-center justify-center w-14 h-14 disabled:opacity-50"
            >
              {isLoading ? <Loader size={20} className="animate-spin" /> : <Search size={20} />}
            </button>
          </div>
          <div className="mt-2 text-xs text-gray-400 dark:text-gray-500">
            <p className="font-medium">Chaves para teste:</p>
            <ul className="list-disc list-inside">
              <li>amigo@email.com</li>
              <li>12345678901</li>
              <li>a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d</li>
            </ul>
          </div>
        </div>
      )}

      {isLoading && (
        <div className="text-center p-8">
          <Loader className="animate-spin inline-block text-gray-400" />
          <p className="text-sm mt-2 text-gray-500">Buscando...</p>
        </div>
      )}

      {error && (
        <div className="mt-4 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl text-center">
            <p className="text-sm text-red-600 dark:text-red-300">{error}</p>
        </div>
      )}

      {recipient && (
        <div className="mt-6 animate-fade-in">
            <h3 className="text-sm text-gray-500 dark:text-gray-400">Destinatário Encontrado:</h3>
            <div className="p-4 mt-2 bg-gray-50 dark:bg-zinc-700 rounded-xl border dark:border-zinc-600">
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-full bg-gray-200 dark:bg-zinc-600 flex items-center justify-center">
                        <User className="text-gray-500 dark:text-gray-300"/>
                    </div>
                    <div>
                        <p className="text-lg font-bold text-gray-900 dark:text-gray-100">{recipient.name}</p>
                        <p className="text-sm text-gray-600 dark:text-gray-400">{recipient.document}</p>
                    </div>
                </div>
                <p className="text-xs text-right text-gray-500 dark:text-gray-400 mt-2">Banco: {recipient.bank}</p>
            </div>

            <div className="mt-4">
                <input type="number" placeholder="Digite o valor a pagar" className="w-full p-3 text-2xl font-bold bg-transparent border-b-2 border-gray-200 dark:border-zinc-600 focus:outline-none focus:border-yellow-500 transition-colors" />
                <button className="mt-4 w-full bg-yellow-500 text-slate-900 font-bold py-4 rounded-xl hover:bg-yellow-600 transition-colors">Pagar</button>
            </div>
        </div>
      )}
    </div>
  );
};

export default PixService;
