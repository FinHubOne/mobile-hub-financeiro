# Mobile Hub Financeiro 🏦



## 📋 Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Dados de transações financeiras
├── src/

```

## ✨ Features



### Tecnologias:
- Python 3.7+
- Flet (Framework para apps desktop/mobile)
- Interface moderna com cores inspiradas em fintechs (Nubank)



A aplicação abrirá em uma janela desktop mostrando o Hub Financeiro.

## 📱 Interface

A aplicação possui:



## 📊 Formato dos Dados

O arquivo `data/extrato.json` contém transações no formato:

```json
{
  "id": 1,
  "titulo": "Supermercado Extra",
  "valor": -45.50,
  "data": "2025-11-20",
  "categoria": "Alimentação",
  "tipo": "compra"
}
```

### Campos:
- **id**: Identificador único
- **titulo**: Descrição da transação
- **valor**: Valor (negativo para gastos, positivo para receitas)
- **data**: Data no formato YYYY-MM-DD
- **categoria**: Categoria (Alimentação, Transporte, Lazer, Salário, etc.)
- **tipo**: Tipo da transação (pix, compra, recarga)

## 🎨 Design



## 📄 License

MIT - Projeto Hackathon