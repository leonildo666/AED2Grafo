#coding: utf8

class AdjNode: 
	def __init__(self, data):
		self.vertex = data
		self.next = None

class Grafo: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [None] * self.V

    def aum_vert(self, tamanho):
        self.grafo = self.grafo + ([None]*tamanho)

    def add_vert(self, origem, destino): 
        node = AdjNode(destino) 
        node.next = self.grafo[origem] 
        self.grafo[origem] = node 

        node = AdjNode(origem) 
        node.next = self.grafo[destino] 
        self.grafo[destino] = node

    def kill_vert(self, alvo):
#######################
#######################
#######################

#a dificuldade é matar o ramo, de resto, foi
#a tentativa maluca aqui foi matar o ramo de todas as listas de adjacencias
#mas ainda não está funcionando direito
#Os nomes também estão saindo estranhos

        for i in range(self.V):
            if i == 0:
                pass
            else:
                temp = self.grafo[i]
                print(i, len(self.grafo))
                x=0 #tentei botar o contador, não rolou
                while temp:
                    x +=1
                    if temp.vertex == '3':
                        self.grafo[i].pop(x)
                        temp = temp.next
                    else:
                        temp = temp.next     
        self.grafo.pop(alvo)
        self.V -= 1



    def print_grafo(self):
        for i in range(self.V):
            if i == 0:
                pass
            else:
                print("[{}]".format(i), end="") 
                temp = self.grafo[i] 
                while temp: 
                    print(" -> {}".format(temp.vertex), end="") 
                    temp = temp.next
                print(" \n") 


if __name__ == "__main__":

    print("Visualizador de Grafos")
    while True:
        choice = input("1-Carregar Grafo\n2-Inserir Nodo\n3-Remover Nodo\n0-Sair\n")

        if choice == '0':
            break

        if choice == '1':
            arquivo = open('entry.txt','r')
            arq = arquivo.read()
            '''O arquivo de entrada deve ter o número de vértices na primeira linha
            e as linhas subsquentes devem ter a seguinte formatação:
            vértice, vértice adjacente
            não devem ser repetidos os vértices, mas a ordem de inserção não é importante'''

            arq = arq.split("\n")

            grafo = Grafo(int(arq[0]))
            arq.pop(0)
            for i in range(0,len(arq)):
                arq[i] = arq[i].split(',')
                grafo.add_vert(int(arq[i][0]),int(arq[i][1])) #Adiciona os vértices ao grafo de acordo com o arquivo
            grafo.print_grafo()
            arquivo.close()

        if choice == '2':
            try:
                grafo.aum_vert(1)
                nome = int(input("Qual o número do vértice?  "))
                g = int(input("Qual o grau do vértice?  "))

                for i in range(0, g):
                    n = int(input("Qual o número do vértice adjacente?  "))
                    grafo.add_vert(nome, n)

                grafo.print_grafo()

            except NameError:
                print('Carregue um grafo antes!\n')
                '''print("Calmaê, nem tem grafo criado")
                new = int(input("Quantos vértices tem esse grafo?  "))
                grafo = Grafo(new+1)
                print('Pronto, agora bora preencher essa bagaça')
                for i in range(1, new+1):
                    g = int(input('Qual o grau do vértice {}?  '.format(i)))
                    for j in range(1, g+1):
                        n = int(input('Qual o número do vértice adjacente?  '))
                        grafo.add_vert(i, n)
                print('Agora sim!')'''

        if choice == '3':
            try:
                grafo.print_grafo()
                alvo = int(input("Qual vértice será deletado?  "))
                grafo.kill_vert(alvo)
                grafo.print_grafo()
            except NameError:
                print("Não existe grafo carregado!\n")
