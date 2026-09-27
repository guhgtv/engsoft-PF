import random

class Pessoa:
    def __init__(self, nome, idade, telefone, cidade=None):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone} | Cidade: {self.cidade}"

class NoLista:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
        self.cidades_disponiveis = self.carregar_cidades()

    def carregar_cidades(self):
        """Lê o arquivo CSV e extrai todas as cidades únicas das duas primeiras colunas"""
        cidades = set()
        try:
            with open('cidades_vizinhas.csv', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    partes = linha.strip().replace(';', ',').split(',')
                    if len(partes) >= 2:
                        cidades.add(partes[0].strip())
                        cidades.add(partes[1].strip())
        except FileNotFoundError:
            print("Aviso: Arquivo cidades_vizinhas.csv não encontrado.")
        return list(cidades)

    def cadastrar_pessoa(self, nome, idade, telefone):
        cidade_sorteada = random.choice(self.cidades_disponiveis) if self.cidades_disponiveis else "Desconhecida"
        nova_pessoa = Pessoa(nome, idade, telefone, cidade_sorteada)
        novo_no = NoLista(nova_pessoa)
        
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            
        self.tamanho += 1
        return nova_pessoa

    def consultar_pessoa(self, nome):
        atual = self.cabeca
        while atual is not None:
            if atual.pessoa.nome.lower() == nome.lower():
                return atual.pessoa
            atual = atual.proximo
        return None

    def obter_todas_pessoas(self):
        """Retorna uma lista em Python com os objetos Pessoa (útil para transferir para a árvore depois)"""
        pessoas = []
        atual = self.cabeca
        while atual is not None:
            pessoas.append(atual.pessoa)
            atual = atual.proximo
        return pessoas