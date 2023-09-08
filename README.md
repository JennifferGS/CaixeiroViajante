# CaixeiroViajante
# Problema do Caixeiro Viajante

Este é um exemplo simples de resolução do problema do caixeiro viajante usando força bruta. O problema do caixeiro viajante envolve encontrar o caminho mais curto que visita todas as cidades exatamente uma vez e retorna à cidade de origem.

## Descrição

A biblioteca itertools é importada para gerar todas as permutações possíveis dos vértices do grafo. Isso é usado para testar todas as possíveis ordens de visita aos vértices.

## Como usar

1. Defina o grafo de entrada no formato de matriz de adjacência. O exemplo a seguir representa um grafo com 4 cidades numeradas de 0 a 3:

   ```python
   grafo = [
       [0, 29, 20, 21],
       [29, 0, 15, 18],
       [20, 15, 0, 27],
       [21, 18, 27, 0]
   ]
Passando o grafo como entrada. Ela retornará o melhor caminho encontrado e a menor distância percorrida.

       melhor_caminho, menor_distancia = caixeiro_viajante(grafo)

O resultado será impresso no console:

    python
    Copy code
    print("Melhor caminho:", melhor_caminho)
    print("Menor distância:", menor_distancia)
       
Observação
Esta é uma implementação de força bruta e pode ser lenta para grafos grandes. Existem algoritmos mais eficientes para resolver o problema do caixeiro viajante em casos reais.

Sinta-se à vontade para ajustar o grafo de entrada para testar diferentes cenários.

Licença
Este código é distribuído sob a licença MIT. Consulte o arquivo LICENSE para obter detalhes.

Nota: Este é um exemplo educacional e simplificado do problema do caixeiro viajante.


Lembre-se de incluir informações relevantes sobre a licença do seu código e quaisquer outros detalhes importantes que os usuários possam precisar para entender e usar o seu projeto. Certifique-se de atualizar o conteúdo conforme necessário.
