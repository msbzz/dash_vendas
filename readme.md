# Dash Vendas

Este projeto é fruto do curso **Dashboards com Dash** da plataforma **Asimov Academy**  onde se tem um **dashboard interativo** desenvolvido com **Dash** e **Plotly** em Python, que analisa os dados de vendas de um supermercado. Ele permite a visualização dinâmica de diferentes métricas, como receita bruta, avaliações (ratings), métodos de pagamento, e linhas de produtos, filtradas por cidades.

## Funcionalidades

- **Seleção de Cidades**: Use a checklist para filtrar os gráficos com base em uma ou mais cidades.
- **Análise de Variáveis**: Escolha entre `gross income` (receita bruta) ou `Rating` (avaliações) para análise, com opções de soma ou média.
- **Gráficos Interativos**:
  - **Por Cidade**: Mostra a soma ou média da variável selecionada agrupada por cidade.
  - **Por Método de Pagamento**: Analisa as vendas por diferentes formas de pagamento.
  - **Por Linha de Produtos**: Detalha o desempenho por tipo de produto, colorido e agrupado por cidade.

## Estrutura do Projeto

- **`app.py`**: Contém o código principal da aplicação.
- **`supermarket_sales.csv`**: Arquivo com os dados de vendas do supermercado.

## Pré-requisitos

- **Python 3.7+**
- Dependências listadas no arquivo `requirements.txt`:
  - `dash`
  - `pandas`
  - `numpy`
  - `plotly`

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/msbzz/dash_vendas.git
   cd dash_vendas 
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o servidor**:
   ```bash
   python app.py
   ```

4. **Acesse o dashboard**:
   - O servidor estará disponível em [http://localhost:8051](http://localhost:8051).

## Estrutura do Dashboard

### Layout
O dashboard possui os seguintes elementos:
- **Checklist de cidades**: Filtra os dados exibidos nos gráficos.
- **Radio buttons de variáveis**: Alterna entre `gross income` (receita bruta) e `Rating` (avaliações).
- **Gráficos interativos**:
  1. **Por Cidade**: Representação por barras.
  2. **Por Método de Pagamento**: Barras horizontais.
  3. **Por Linha de Produtos**: Barras agrupadas por cidade e coloridas.

### Callbacks
Os gráficos são atualizados dinamicamente com base nas entradas do usuário, utilizando filtros e operações de soma/média.

## Exemplo de Uso

1. Selecione as cidades desejadas na checklist.
2. Escolha a variável de análise (`gross income` ou `Rating`) nos botões de rádio.
3. Explore os gráficos atualizados com base nas suas seleções.

---

### Possíveis Melhorias Futuras

- Adicionar mais dimensões de análise, como período de tempo.
- Melhorar a experiência visual com customizações de cores e temas.
- Implementar funcionalidades de exportação de dados filtrados.

---

 