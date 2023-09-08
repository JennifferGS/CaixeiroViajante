# A biblioteca itertools é importada para gerar todas as permutações possíveis dos vértices do grafo. 
# Isso será usado para testar todas as possíveis ordens de visita aos vértices.
import itertools

# Função para calcular a distância entre dois pontos (cidades)
def calcula_distancia(caminho, grafo):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        distancia_total += grafo[origem][destino]
    distancia_total += grafo[caminho[-1]][caminho[0]]  # Volta ao ponto de partida
    return distancia_total

# Função para calcular a distância (permutação das cidades)
# Ela recebe uma matriz de adjacência, grafo como entrada.
def caixeiro_viajante(grafo):
    num_vertices = len(grafo)
    vertices = list(range(num_vertices))
    melhor_caminho = None
    menor_distancia = float('inf')

    for permutacao in itertools.permutations(vertices):
        distancia = calcula_distancia(permutacao, grafo)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_caminho = permutacao

    return melhor_caminho, menor_distancia

# Neste exemplo, temos 4 cidades numeradas de 0 a 3
cidades = [0, 1, 2, 3]  

# Exemplo de uso
grafo = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 27],
    [21, 18, 27, 0]
]

melhor_caminho, menor_distancia = caixeiro_viajante(grafo)
print("Melhor caminho:", melhor_caminho)
print("Menor distância:", menor_distancia)

# Este é um exemplo simples de resolução do problema do caixeiro viajante usando força bruta. 
# Para grafos maiores, essa abordagem pode ser extremamente lenta.