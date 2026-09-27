class NoArvore:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, pessoa):
        if self.raiz is None:
            self.raiz = NoArvore(pessoa)
        else:
            self._inserir_recursivo(self.raiz, pessoa)

    def _inserir_recursivo(self, no_atual, pessoa):
        if pessoa.nome.lower() < no_atual.pessoa.nome.lower():
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(pessoa)
            else:
                self._inserir_recursivo(no_atual.esquerda, pessoa)
        elif pessoa.nome.lower() > no_atual.pessoa.nome.lower():
            if no_atual.direita is None:
                no_atual.direita = NoArvore(pessoa)
            else:
                self._inserir_recursivo(no_atual.direita, pessoa)

    def buscar(self, nome):
        return self._buscar_recursivo(self.raiz, nome)

    def _buscar_recursivo(self, no_atual, nome):
        if no_atual is None:
            return None
        if nome.lower() == no_atual.pessoa.nome.lower():
            return no_atual.pessoa
        elif nome.lower() < no_atual.pessoa.nome.lower():
            return self._buscar_recursivo(no_atual.esquerda, nome)
        else:
            return self._buscar_recursivo(no_atual.direita, nome)

    def remover(self, nome):
        self.raiz, removido = self._remover_recursivo(self.raiz, nome)
        return removido

    def _remover_recursivo(self, no_atual, nome):
        if no_atual is None:
            return no_atual, False

        if nome.lower() < no_atual.pessoa.nome.lower():
            no_atual.esquerda, removido = self._remover_recursivo(no_atual.esquerda, nome)
        elif nome.lower() > no_atual.pessoa.nome.lower():
            no_atual.direita, removido = self._remover_recursivo(no_atual.direita, nome)
        else:
            removido = True
            if no_atual.esquerda is None:
                return no_atual.direita, removido
            elif no_atual.direita is None:
                return no_atual.esquerda, removido
            
            temp = self._minimo_no(no_atual.direita)
            no_atual.pessoa = temp.pessoa
            no_atual.direita, _ = self._remover_recursivo(no_atual.direita, temp.pessoa.nome)
            
        return no_atual, removido

    def _minimo_no(self, no_atual):
        atual = no_atual
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def obter_primeiro_ordem_alfabetica(self):
        if self.raiz is None:
            return None
        return self._minimo_no(self.raiz).pessoa

    def obter_ultimo_ordem_alfabetica(self):
        atual = self.raiz
        if atual is None:
            return None
        while atual.direita is not None:
            atual = atual.direita
        return atual.pessoa

    def obter_todas_pessoas(self):
        """Retorna uma lista ordenada das pessoas (útil para as varreduras do Assistente)"""
        pessoas = []
        self._in_ordem(self.raiz, pessoas)
        return pessoas

    def _in_ordem(self, no_atual, pessoas):
        if no_atual is not None:
            self._in_ordem(no_atual.esquerda, pessoas)
            pessoas.append(no_atual.pessoa)
            self._in_ordem(no_atual.direita, pessoas)