
import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, CartesianGrid } from 'recharts';

const ExpenseChart = ({ transactions }) => {
  const expenseData = transactions
    .filter(t => t.type === 'out' && t.category)
    .reduce((acc, t) => {
      const category = t.category || 'Outros';
      const amount = Math.abs(t.amount);

      if (!acc[category]) {
        acc[category] = { name: category, value: 0 };
      }
      acc[category].value += amount;
      return acc;
    }, {});

  const chartData = Object.values(expenseData).sort((a, b) => b.value - a.value);

  if (chartData.length === 0) {
    return <p className="empty-chart-text">Não há dados de despesas para exibir o gráfico.</p>; 
  }
  
  const CustomTooltip = ({ active, payload, label }) => {
      if (active && payload && payload.length) {
          return (
          <div className="chart-tooltip">
              <p className="tooltip-label">{label}</p>
              <p className="tooltip-value">{`Total: R$ ${payload[0].value.toFixed(2).replace('.', ',')}`}</p>
          </div>
          );
      }
      return null;
  };


  return (
    <div className="chart-wrapper">
        <ResponsiveContainer width="100%" height={300}>
            <BarChart data={chartData} margin={{ top: 5, right: 20, left: -10, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="var(--border, #e0e0e020)" />
                <XAxis 
                    dataKey="name" 
                    stroke="var(--text-secondary, #888888)"
                    fontSize={12} 
                    tickLine={false}
                    axisLine={false}
                />
                <YAxis 
                    stroke="var(--text-secondary, #888888)"
                    fontSize={12}
                    tickLine={false}
                    axisLine={false}
                    tickFormatter={(value) => `R$${value}`}
                />
                <Tooltip 
                    cursor={{ fill: 'rgba(136, 132, 216, 0.1)' }}
                    content={<CustomTooltip />}
                />
                <Bar dataKey="value" name="Total Gasto" fill="var(--icon-active, #8884d8)" barSize={30} radius={[10, 10, 0, 0]} />
            </BarChart>
        </ResponsiveContainer>
    </div>
  );
};

export default ExpenseChart;
