# Algoritmo Genético para Alocação de Clientes em Access Points

## Descrição

Este projeto implementa um Algoritmo Genético (AG) para otimizar a alocação de clientes em pontos de acesso (Access Points - APs), garantindo que a capacidade de cada AP não seja ultrapassada e minimizando a distância total entre clientes e APs.

O código lê um arquivo CSV contendo as coordenadas dos clientes e usa um AG para encontrar a melhor distribuição dos clientes entre os APs disponíveis.

## Funcionalidades

- Cálculo da distância euclidiana entre clientes e APs.
- Avaliação da qualidade das soluções considerando a distância total e restrições de capacidade.
- Algoritmo Genético com:
  - Geração de população inicial válida
  - Seleção por torneio
  - Cruzamento (crossover)
  - Mutação com correção de soluções inválidas
- Carregamento de clientes a partir de um arquivo CSV.
- Exibição do resultado final com a alocação de clientes por AP.

## Estrutura do Código

- **Definição dos APs:** Cada AP tem uma localização e capacidade máxima de clientes suportados.
- **Funções principais:**
  - `calcular_distancia(cliente, ap)`: Calcula a distância euclidiana entre um cliente e um AP.
  - `avaliar_solucao(solucao, clientes)`: Calcula o fitness de uma solução.
  - `gerar_populacao_inicial(tamanho_populacao, num_clientes)`: Cria soluções iniciais válidas.
  - `selecao_torneio(populacao, fitness)`: Seleção de indivíduos para reprodução.
  - `crossover(pai1, pai2)`: Realiza o cruzamento entre dois indivíduos.
  - `mutacao(solucao, taxa_mutacao)`: Aplica mutação a uma solução.
  - `corrigir_solucao(solucao)`: Garante que a solução final respeite as restrições de capacidade.
  - `algoritmo_genetico(clientes, tamanho_populacao, geracoes, taxa_mutacao)`: Executa o AG para encontrar a melhor alocação.
  - `carregar_clientes(caminho_arquivo)`: Lê as coordenadas dos clientes de um arquivo CSV.
  - `formatar_solucao(solucao, clientes)`: Organiza a solução final para exibição.

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias (caso não tenha):
   ```bash
   pip install numpy
   ```
3. Prepare um arquivo CSV chamado `ag_data.csv` contendo os clientes no seguinte formato:
   ```csv
   Cliente;X;Y
   1;10;20
   2;30;40
   3;50;60
   ```
4. Execute o script:
   ```bash
   python nome_do_arquivo.py
   ```

## Exemplo de Saída

```text
-------------APA--------------
APA: [1, 3, 5]
(Quantidade de clientes: 3)
-------------APB--------------
APB: [2, 4]
(Quantidade de clientes: 2)
...
```

## Personalização

- Modifique os parâmetros do AG na função `algoritmo_genetico()` para ajustar o comportamento do algoritmo.
- Alterar as localizações e capacidades dos APs conforme necessário.

## Licença

Este projeto está sob a licença MIT.

