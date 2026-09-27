from atribuicoes_secretario import ListaEncadeada
from atribuicoes_diretor import ArvoreBinariaBusca
from atribuicoes_assistente import Grafo

def menu_secretario():
    print("\nVocê deseja:")
    print("(1) Cadastrar nova pessoa na lista de espera.")
    print("(2) Consultar pessoa cadastrada.")
    print("(3) Ver quantidade de pessoas cadastradas.")
    print("(4) Finalizar execução.")
    return input("Digite sua opção: ")

def menu_diretor():
    print("\nVocê deseja:")
    print("(1) Alterar nome, idade ou telefone de pessoa cadastrada.")
    print("(2) Descadastrar pessoa.")
    print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
    print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
    print("(5) Confirmar validade da lista de espera e finalizar execução.")
    return input("Digite sua opção: ")

def menu_assistente():
    print("\nVocê deseja:")
    print("(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.")
    print("(2) Ver a menor distância da cidade da escola até a cidade da pessoa passando por uma cidade específica.")
    print("(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade da escola (incluindo distância).")
    print("(4) Finalizar execução.")
    return input("Digite sua opção: ")

def main():
    lista_pessoas = ListaEncadeada()
    print("----------- Olá, Secretário(a)! -----------")
    
    while True:
        opcao = menu_secretario()
        if opcao == '1':
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade: ")
            telefone = input("Digite o telefone: ")
            pessoa = lista_pessoas.cadastrar_pessoa(nome, idade, telefone)
            print(pessoa)
            
        elif opcao == '2':
            nome = input("Digite o nome da pessoa: ")
            pessoa = lista_pessoas.consultar_pessoa(nome)
            if pessoa:
                print(pessoa)
            else:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
                
        elif opcao == '3':
            print(f"São {lista_pessoas.tamanho} pessoas na lista de espera.")
            
        elif opcao == '4':
            print("Fim das atividades sob responsabilidade do(a) Secretário(a).")
            break
        else:
            pass

    arvore_pessoas = ArvoreBinariaBusca()
    for pessoa in lista_pessoas.obter_todas_pessoas():
        arvore_pessoas.inserir(pessoa)

    print("\n----------- Olá, Diretor(a)! -----------")
    while True:
        opcao = menu_diretor()
        if opcao == '1':
            nome = input("Digite o nome da pessoa que você quer editar: ")
            pessoa = arvore_pessoas.buscar(nome)
            if pessoa:
                print(pessoa)
                escolha_edicao = input("O que você quer editar? Digite 1 para nome, 2 para idade ou 3 para telefone: ")
                if escolha_edicao == '1':
                    novo_nome = input("Digite o novo nome: ")
                    pessoa.nome = novo_nome
                    arvore_pessoas.remover(nome)
                    arvore_pessoas.inserir(pessoa)
                    print("Dados atualizados com sucesso.")
                elif escolha_edicao == '2':
                    nova_idade = input("Digite a nova idade: ")
                    pessoa.idade = nova_idade
                    print("Dados atualizados com sucesso.")
                elif escolha_edicao == '3':
                    novo_telefone = input("Digite o novo telefone: ")
                    pessoa.telefone = novo_telefone
                    print("Dados atualizados com sucesso.")
            else:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")

        elif opcao == '2':
            nome = input("Digite o nome da pessoa que você quer descadastrar: ")
            pessoa = arvore_pessoas.buscar(nome)
            if pessoa:
                print(pessoa)
                confirmacao = input(f"Tem certeza que deseja descadastrar {nome}? Digite S ou N: ")
                if confirmacao.upper() == 'S':
                    arvore_pessoas.remover(nome)
                    print(f"{nome} descadastrado com sucesso.")
            else:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")

        elif opcao == '3':
            pessoa = arvore_pessoas.obter_primeiro_ordem_alfabetica()
            if pessoa: print(pessoa)
            
        elif opcao == '4':
            pessoa = arvore_pessoas.obter_ultimo_ordem_alfabetica()
            if pessoa: print(pessoa)
            
        elif opcao == '5':
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).")
            break

    grafo_cidades = Grafo()
    print("\n----------- Olá, Assistente! -----------")
    cidade_escola = "Guarujá"
    cidade_escala_fixa = "Indaiatuba"

    while True:
        opcao = menu_assistente()
        if opcao == '1':
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ")
            pessoa = arvore_pessoas.buscar(nome)
            if pessoa:
                print(pessoa)
                caminho, distancia = grafo_cidades.menor_distancia_simples(cidade_escola, pessoa.cidade)
                print(f"Menor caminho = {caminho} com custo {int(distancia)}")
            else:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")

        elif opcao == '2':
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ")
            pessoa = arvore_pessoas.buscar(nome)
            if pessoa:
                print(pessoa)
                caminho, distancia = grafo_cidades.menor_distancia_com_escala(cidade_escola, cidade_escala_fixa, pessoa.cidade)
                print(f"Menor caminho = {caminho} com custo {int(distancia)}")
            else:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")

        elif opcao == '3':
            todas_pessoas = arvore_pessoas.obter_todas_pessoas()
            if not todas_pessoas:
                print("Nenhuma pessoa na lista de espera.")
                continue

            menor_distancia = float('inf')
            cidade_mais_proxima = ""
            moradores_mais_proximos = []

            distancias, _ = grafo_cidades.calcular_menor_caminho(cidade_escola)
            
            for pessoa in todas_pessoas:
                dist_pessoa = distancias.get(pessoa.cidade, float('inf'))
                if dist_pessoa < menor_distancia:
                    menor_distancia = dist_pessoa
                    cidade_mais_proxima = pessoa.cidade
                    moradores_mais_proximos = [pessoa]
                elif dist_pessoa == menor_distancia and pessoa.cidade == cidade_mais_proxima:
                    moradores_mais_proximos.append(pessoa)

            print(f"A cidade mais próxima à cidade da escola que tem moradores na lista de espera (ver abaixo) é {cidade_mais_proxima}. Distância = {int(menor_distancia)}")
            for morador in moradores_mais_proximos:
                print(morador)

        elif opcao == '4':
            print("Execução finalizada.")
            break

if __name__ == "__main__":
    main()