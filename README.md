## Descrição do Projeto

Este projeto realiza uma análise exploratória de dados sobre apartamentos disponíveis para aluguel em Nova York, utilizando o conjunto de dados `AB_NYC_2019.csv`. O objetivo é entender a distribuição dos apartamentos, o preço médio por tipo de quarto, a média de avaliações mensais por bairro e a disponibilidade dos imóveis ao longo do ano.

O conjunto de dados foi pré-processado para lidar com valores ausentes nas colunas `name`, `host_name`, `last_review`, e `reviews_per_month`, e a coluna `last_review` foi convertida para o formato `datetime`. A seguir, foram feitas as seguintes análises:

1. **Número de Apartamentos por Bairro**: Analisou a distribuição do número de apartamentos em cada bairro de Nova York, gerando um gráfico de barras para visualizar a quantidade de apartamentos em cada região.

2. **Média de Avaliações Mensais por Bairro**: Calculou a média de avaliações mensais por bairro e visualizou os 5 bairros com a maior média de avaliações mensais em um gráfico de barras horizontais.

3. **Preço Médio por Tipo de Quarto**: Calculou o preço médio por tipo de quarto (por exemplo, quarto compartilhado, inteiro ou privado) e gerou um gráfico de barras para comparar os preços.

4. **Média de Disponibilidade por Bairro**: Analisou a média de disponibilidade (dias em que o apartamento está disponível para reserva ao longo do ano) por bairro e gerou um gráfico de barras horizontais com os 5 bairros com maior média de disponibilidade.

5. **Distribuição de Preços**: Mostrou a distribuição dos preços dos apartamentos em um histograma para entender como os preços estão distribuídos entre os imóveis.

Essas análises permitem uma visão detalhada das características dos apartamentos em Nova York e fornecem insights valiosos para quem busca informações sobre o mercado de aluguel na cidade.
