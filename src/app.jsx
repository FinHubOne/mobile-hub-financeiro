import React, { useState, useEffect } from 'react';
import { Wallet, PieChart, Shield, Zap, Target, Home, User, Bell, Database, FileText, Smartphone } from 'lucide-react';
import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, collection, doc, onSnapshot, query, writeBatch } from 'firebase/firestore';
import { getFunctions, httpsCallable } from 'firebase/functions';

// Import Service Components
import PixService from './components/PixService.jsx';
import CashbackService from './components/CashbackService.jsx';
import InsuranceService from './components/InsuranceService.jsx';
import BoletoService from './components/BoletoService.jsx';
import RecargaService from './components/RecargaService.jsx';
import ThemeSwitcher from './components/ThemeSwitcher.jsx';
import { TransactionItem, getCategoryDetails } from './components/TransactionItem.jsx';
import ExpenseChart from './components/ExpenseChart.jsx';
import Draggable from './components/Draggable.jsx';

// --- FIREBASE CONFIGURATION ---
const firebaseConfig = {
  apiKey: "AIzaSyAMYMfs-x_BPp7mG2uayAbKGzQk5LUbB0Y",
  authDomain: "financial-wellness-hub-a1da4.firebaseapp.com",
  projectId: "financial-wellness-hub-a1da4",
  storageBucket: "financial-wellness-hub-a1da4.firebasestorage.app",
  messagingSenderId: "1076440428624",
  appId: "1:1076440428624:web:49dd123d374e6862166155",
  measurementId: "G-8RNSJT3MD3"
};

// --- INITIALIZATION ---
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const functions = getFunctions(app, 'southamerica-east1');
const APP_ID = "fluxo-hackathon";

// --- SEED DATA ---
const INITIAL_TRANSACTIONS = [
    { id: '1', raw_description: 'PGTO *UBER DO BRASIL TEC', amount: -24.90, date: new Date().toISOString(), type: 'out' },
    { id: '2', raw_description: 'TRANSF PIX RECEBIDA - JOAO SILVA', amount: 150.00, date: new Date(Date.now() - 86400000).toISOString(), type: 'in' },
    { id: '3', raw_description: 'COMPRA CARTAO - PADARIA ESTRELA', amount: -12.50, date: new Date(Date.now() - 172800000).toISOString(), type: 'out' },
    { id: '4', raw_description: 'PAGAMENTO BOLETO - ALUGUEL IMOB', amount: -1200.00, date: '2023-10-25T10:00:00Z', type: 'out' },
    { id: '5', raw_description: 'COMPRA MKTPLACE - AMAZON SERV', amount: -189.90, date: '2023-10-24T14:30:00Z', type: 'out' },
    { id: '6', raw_description: 'NETFLIX streaming', amount: -39.90, date: '2023-10-23T14:30:00Z', type: 'out' },
    { id: '7', raw_description: 'FARMACIA SAO PAULO', amount: -55.40, date: '2023-10-22T11:30:00Z', type: 'out' },
];

// --- HELPER COMPONENTS ---

const ServiceCard = ({ title, icon, color, onClick, active }) => (
  <button 
    onClick={onClick}
    className={`flex flex-col items-center justify-center p-3 rounded-2xl border transition-all duration-300 w-28 h-28 flex-shrink-0
    ${active ? `bg-${color}-500 text-white shadow-lg shadow-${color}-500/30 border-${color}-600` 
            : 'bg-white dark:bg-zinc-800 border-gray-200 dark:border-zinc-700 hover:bg-gray-50 dark:hover:bg-zinc-700'}`}
  >
    {icon}
    <span className="font-semibold text-sm mt-2 text-center">{title}</span>
  </button>
);

const NavItem = ({ icon, label, active, onClick }) => (
  <button onClick={onClick} className={`flex flex-col items-center justify-center transition-colors duration-200 ${active ? 'text-blue-500' : 'text-gray-400 hover:text-blue-500'}`}>
    {icon}
    <span className="text-xs font-medium mt-1">{label}</span>
  </button>
);

// --- MAIN APP COMPONENT ---

export default function App() {
  const [user, setUser] = useState(null);
  const [activeService, setActiveService] = useState('home');
  const [transactions, setTransactions] = useState([]);
  const [processedTransactions, setProcessedTransactions] = useState({});
  const [balance, setBalance] = useState(0);
  const [loading, setLoading] = useState(true);
  const [authError, setAuthError] = useState(null);
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light');

  const callProcessTransaction = httpsCallable(functions, 'process_transaction_py');

  useEffect(() => {
    const root = window.document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prevTheme => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      if (currentUser) {
        setUser(currentUser);
      } else {
        signInAnonymously(auth).catch((error) => {
          console.error("Anonymous sign-in error:", error);
          setAuthError("Failed to sign in. Check Firebase config.");
        });
      }
    });
    return () => unsubscribe();
  }, []);

  useEffect(() => {
    if (!user) return;

    const txQuery = query(collection(db, 'artifacts', APP_ID, 'users', user.uid, 'transactions'));
    const unsubscribeTx = onSnapshot(txQuery, (snapshot) => {
      let txs = snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
      txs.sort((a, b) => new Date(b.date) - new Date(a.date));
      setTransactions(txs);
      
      const total = txs.reduce((acc, curr) => acc + curr.amount, 3000); 
      setBalance(total);
      setLoading(false);
    }, (error) => {
      console.error("Error reading transactions:", error);
      setLoading(false);
    });

    return () => unsubscribeTx();
  }, [user]);

  useEffect(() => {
    if (transactions.length === 0) return;

    const processAll = async () => {
      const newProcessed = {...processedTransactions};
      for (const t of transactions) {
        if (newProcessed[t.id]) continue;
        try {
          const result = await callProcessTransaction({ raw_description: t.raw_description });
          newProcessed[t.id] = result.data;
        } catch (error) {
          console.error("Error calling Cloud Function:", error);
          newProcessed[t.id] = { category: 'Outros', cleanDescription: t.raw_description.substring(0, 25) };
        }
      }
      setProcessedTransactions(newProcessed);
    };

    processAll();
  }, [transactions]);
  
  const seedDatabase = async () => {
    if (!user) return;
    setLoading(true);
    const batch = writeBatch(db);
    INITIAL_TRANSACTIONS.forEach((tx) => {
      const docRef = doc(collection(db, 'artifacts', APP_ID, 'users', user.uid, 'transactions'));
      batch.set(docRef, { ...tx, amount: Number(tx.amount) });
    });
    try {
      await batch.commit();
    } catch (e) {
      console.error("Error seeding DB:", e);
    }
    setLoading(false);
  };

  const renderActiveService = () => {
    if (activeService === 'home') return null;
    
    const services = {
      pix: <PixService />,
      cashback: <CashbackService savings={120.50} />,
      insurance: <InsuranceService transactions={transactions} processedTransactions={processedTransactions} />,
      boletos: <BoletoService />,
      recargas: <RecargaService />,
    };

    return (
      <div className="mt-6 mb-2 animate-fade-in-up">
        {services[activeService]}
      </div>
    );
  }

  return (
    <>
    <style>
        {`
        .scrollbar-hide::-webkit-scrollbar {
            display: none;
        }
        .scrollbar-hide {
            -ms-overflow-style: none; 
            scrollbar-width: none; 
        }
        `}
    </style>
    <div className="min-h-screen bg-gray-50 dark:bg-zinc-900 font-sans text-gray-900 dark:text-gray-100 flex justify-center">
      <div className="w-full max-w-md bg-white dark:bg-black md:shadow-2xl md:border-x md:border-zinc-200 dark:md:border-zinc-800 relative flex flex-col">
        
        <div className="absolute top-0 left-0 right-0 h-32 bg-blue-600 dark:bg-blue-800 rounded-b-2xl" />

        {/* --- Header --- */}
        <header className="p-6 pt-10 pb-4 z-10">
          <div className="flex justify-between items-center">
            <div className="flex items-center gap-3">
              <div className="h-12 w-12 bg-blue-200 dark:bg-blue-500 rounded-full flex items-center justify-center text-blue-700 dark:text-white font-bold text-lg">JS</div>
              <div>
                <p className="text-sm text-blue-100 dark:text-blue-200">Bem-vindo,</p>
                <h1 className="text-xl font-bold text-white">João Silva</h1>
              </div>
            </div>
            <div className="flex items-center gap-4">
              <ThemeSwitcher theme={theme} toggleTheme={toggleTheme} />
              <button className="relative">
                <Bell className="text-blue-100 dark:text-blue-200" size={26} />
                {balance < 1000 && <div className="absolute top-0 right-0 h-2 w-2 bg-red-500 rounded-full"></div>}
              </button>
            </div>
          </div>
        </header>

        {/* --- Main Content --- */}
        <main className="flex-grow pb-28 overflow-y-auto overflow-x-hidden z-10">
          <div className="px-6">
            {/* --- Balance --- */}
            <div className="mt-10 mb-6">
              <p className="text-base font-semibold text-gray-500 dark:text-zinc-400 mb-1">Saldo em conta</p>
              <h2 className="text-4xl font-extrabold tracking-tighter">
                {loading ? "..." : `R$ ${balance.toFixed(2).replace('.', ',')}`}
              </h2>
            </div>
          </div>

          {/* --- Service Icons --- */}
          <div className="mb-8 pl-6">
             <Draggable>
                <ServiceCard title="Área Pix" icon={<Zap size={32} />} color="yellow" active={activeService === 'pix'} onClick={() => setActiveService(activeService === 'pix' ? 'home' : 'pix')} />
                <ServiceCard title="Cashback" icon={<Target size={32} />} color="purple" active={activeService === 'cashback'} onClick={() => setActiveService(activeService === 'cashback' ? 'home' : 'cashback')} />
                <ServiceCard title="Seguros" icon={<Shield size={32} />} color="blue" active={activeService === 'insurance'} onClick={() => setActiveService(activeService === 'insurance' ? 'home' : 'insurance')} />
                <ServiceCard title="Pagar Boleto" icon={<FileText size={32} />} color="green" active={activeService === 'boletos'} onClick={() => setActiveService(activeService === 'boletos' ? 'home' : 'boletos')} />
                <ServiceCard title="Recarga" icon={<Smartphone size={32} />} color="red" active={activeService === 'recargas'} onClick={() => setActiveService(activeService === 'recargas' ? 'home' : 'recargas')} />
                {/* Adicione mais cards aqui se precisar */}
             </Draggable>
          </div>
          
          <div className="px-6">
            {/* --- Active Service Component --- */}
            {renderActiveService()}

            {/* --- Activity Feed --- */}
            <div className="mb-8">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-bold">Atividade</h3>
                {transactions.length === 0 && !loading && !authError && (
                  <button onClick={seedDatabase} className="text-xs bg-blue-500 text-white px-3 py-1 rounded-full font-medium flex items-center gap-1 hover:bg-blue-600 transition-colors">
                    <Database size={12} /> Carregar Dados
                  </button>
                )}
              </div>

              <div className="space-y-2">
                {authError && <p className="text-red-500">{authError}</p>}
                {loading && <p className="text-center text-gray-400 py-8">Carregando transações...</p>}
                {!loading && transactions.length === 0 && (
                  <div className="text-center py-8 text-gray-400">
                    <p>Nenhuma transação registrada.</p>
                    <p className="text-xs mt-1">Clique para carregar dados de exemplo.</p>
                  </div>
                )}
                {transactions.slice(0, 5).map((t, index) => (
                  <TransactionItem 
                    key={t.id}
                    transaction={t} 
                    processed={processedTransactions[t.id]}
                    categoryDetails={getCategoryDetails(processedTransactions[t.id]?.category, t.type)}
                    style={{ animationDelay: `${index * 50}ms` }}
                  />
                ))}
              </div>
            </div>

            {/* --- Expense Chart --- */}
            <ExpenseChart transactions={transactions} processedTransactions={processedTransactions} />
          </div>
        </main>

        {/* --- Bottom Navigation --- */}
        <nav className="fixed bottom-0 left-0 w-full bg-white/80 dark:bg-black/80 backdrop-blur-sm border-t border-gray-100 dark:border-zinc-800 p-4 flex justify-around items-start md:absolute md:max-w-md">
          <NavItem icon={<Home size={26} />} label="Início" active={true} onClick={() => setActiveService('home')} />
          <NavItem icon={<Wallet size={26} />} label="Carteira" />
          <NavItem icon={<PieChart size={26} />} label="Análise" />
          <NavItem icon={<User size={26} />} label="Perfil" />
        </nav>
      </div>
    </div>
    </>
  );
}
