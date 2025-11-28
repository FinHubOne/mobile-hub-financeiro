import React from 'react';
import ExpenseChart from './ExpenseChart.jsx';
import { Lightbulb, TrendingUp, DollarSign } from 'lucide-react';
import './Analysis.css';

// --- HELPER COMPONENTS ---

const RecommendationCard = ({ icon, title, text }) => (
  <div className="recommendation-card">
    <div className="recommendation-icon">
      {icon}
    </div>
    <div>
      <h4>{title}</h4>
      <p>{text}</p>
    </div>
  </div>
);

// --- MAIN ANALYSIS COMPONENT ---

const AnalysisService = ({ transactions }) => {
  // Simples lógica para gerar recomendações baseada nas categorias de gastos
  const generateRecommendations = () => {
    const recommendations = [];
    const expenseCategories = transactions
      .filter(t => t.type === 'out')
      .reduce((acc, t) => {
        acc[t.category] = (acc[t.category] || 0) + Math.abs(t.amount);
        return acc;
      }, {});

    const totalExpenses = Object.values(expenseCategories).reduce((sum, amount) => sum + amount, 0);

    // Encontra a categoria de maior gasto
    const biggestExpenseCategory = Object.keys(expenseCategories).reduce((a, b) => expenseCategories[a] > expenseCategories[b] ? a : b, null);

    if (biggestExpenseCategory) {
      const percentage = ((expenseCategories[biggestExpenseCategory] / totalExpenses) * 100).toFixed(0);
      recommendations.push({
        icon: <Lightbulb size={20} />,
        title: `Atenção aos gastos com ${biggestExpenseCategory}!`,
        text: `Você gastou cerca de ${percentage}% do total de suas despesas nesta categoria. Que tal rever alguns custos?`
      });
    }

    // Recomendação genérica de investimento
    recommendations.push({
      icon: <TrendingUp size={20} />,
      title: 'Comece a investir',
      text: 'Mesmo pequenas quantias podem crescer com o tempo. Explore opções de investimento de baixo risco para iniciar.'
    });
    
    // Recomendação genérica de economia
    recommendations.push({
      icon: <DollarSign size={20} />,
      title: 'Crie uma reserva de emergência',
      text: 'Guarde um pouco a cada mês para cobrir despesas inesperadas. O ideal é ter o equivalente a 3-6 meses de seus custos.'
    });

    return recommendations;
  };

  const recommendations = generateRecommendations();

  return (
    <div className="analysis-container">
      <div>
        <h3>Análise de Despesas</h3>
        <ExpenseChart transactions={transactions} />
      </div>

      <div>
        <h3>Recomendações para Você</h3>
        <div className="recommendations-list">
          {recommendations.map((rec, index) => (
            <RecommendationCard key={index} icon={rec.icon} title={rec.title} text={rec.text} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default AnalysisService;
