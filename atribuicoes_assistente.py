import heapq

class Grafo:
    def __init__(self):
        self.adjacencias = {}
        self.carregar_grafo()

    def carregar_grafo(self):
        try:
            with open('cidades_vizinhas.csv', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    partes = linha.strip().replace(';', ',').split(',')
                    if len(partes) >= 3:
                        cidade1 = partes[0].strip()
                        cidade2 = partes[1].strip()
                        distancia = float(partes[2].strip())

                        if cidade1 not in self.adjacencias:
                            self.adjacencias[cidade1] = {}
                        if cidade2 not in self.adjacencias:
                            self.adjacencias[cidade2] = {}
                            
                        self.adjacencias[cidade1][cidade2] = distancia
                        self.adjacencias[cidade2][cidade1] = distancia
        except Exception as e:
            print("Erro ao carregar o grafo:", e)

    def calcular_menor_caminho(self, origem, destino_procurado=None):
        """Algoritmo de Dijkstra para menor caminho"""
        distancias = {cidade: float('infinity') for cidade in self.adjacencias}
        caminhos = {cidade: [] for cidade in self.adjacencias}
        
        if origem not in self.adjacencias:
            return distancias, caminhos

        distancias[origem] = 0
        caminhos[origem] = [origem]
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            distancia_atual, cidade_atual = heapq.heappop(fila_prioridade)

            if distancia_atual > distancias[cidade_atual]:
                continue
                
            if destino_procurado and cidade_atual == destino_procurado:
                break

            for vizinho, peso in self.adjacencias[cidade_atual].items():
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    caminhos[vizinho] = caminhos[cidade_atual] + [vizinho]
                    heapq.heappush(fila_prioridade, (distancia, vizinho))
                    
        return distancias, caminhos

    def menor_distancia_simples(self, origem, destino):
        distancias, caminhos = self.calcular_menor_caminho(origem, destino)
        return caminhos.get(destino, []), distancias.get(destino, float('inf'))

    def menor_distancia_com_escala(self, origem, escala, destino):
        caminho_parte1, dist1 = self.menor_distancia_simples(origem, escala)
        caminho_parte2, dist2 = self.menor_distancia_simples(escala, destino)
        
        if dist1 == float('inf') or dist2 == float('inf'):
            return [], float('inf')
            
        caminho_final = caminho_parte1 + caminho_parte2[1:]
        distancia_total = dist1 + dist2
        return caminho_final, distancia_total