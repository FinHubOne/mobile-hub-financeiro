import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer, CartesianGrid } from 'recharts';

const ExpenseChart = ({ transactions, processedTransactions }) => {
  const expenseData = transactions
    .filter(t => t.type === 'out' && processedTransactions[t.id])
    .reduce((acc, t) => {
      const category = processedTransactions[t.id]?.category || 'Outros';
      const amount = Math.abs(t.amount);

      if (!acc[category]) {
        acc[category] = { name: category, value: 0 };
      }
      acc[category].value += amount;
      return acc;
    }, {});

  const chartData = Object.values(expenseData).sort((a, b) => b.value - a.value);

  if (chartData.length === 0) {
    return null; 
  }
  
  const CustomTooltip = ({ active, payload, label }) => {
      if (active && payload && payload.length) {
          return (
          <div className="p-3 bg-slate-900 text-white rounded-lg shadow-lg">
              <p className="font-bold">{label}</p>
              <p className="text-sm">{`Total: R$ ${payload[0].value.toFixed(2)}`}</p>
          </div>
          );
      }
      return null;
  };


  return (
    <div className="my-8">
        <h3 className="text-lg font-bold mb-4">Análise de Despesas</h3>
        <div style={{ width: '100%', height: 300 }}>
            <ResponsiveContainer>
                <BarChart data={chartData} margin={{ top: 5, right: 20, left: -10, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#e0e0e020" />
                    <XAxis 
                        dataKey="name" 
                        stroke="#888888"
                        fontSize={12} 
                        tickLine={false}
                        axisLine={false}
                    />
                    <YAxis 
                        stroke="#888888"
                        fontSize={12}
                        tickLine={false}
                        axisLine={false}
                        tickFormatter={(value) => `R$${value}`}
                    />
                    <Tooltip 
                        cursor={{ fill: 'rgba(136, 132, 216, 0.1)' }}
                        content={<CustomTooltip />}
                    />
                    <Bar dataKey="value" name="Total Gasto" fill="#8884d8" barSize={30} radius={[10, 10, 0, 0]} />
                </BarChart>
            </ResponsiveContainer>
        </div>
    </div>
  );
};

export default ExpenseChart;
