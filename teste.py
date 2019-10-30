class AdjNode: 
	def __init__(self, data):
		self.vertex = data
		self.next = None

class Grafo: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.grafo = [None] * self.V 

	def add_vert(self, origem, destino): 
		node = AdjNode(destino) 
		node.next = self.grafo[origem] 
		self.grafo[origem] = node 

		node = AdjNode(origem) 
		node.next = self.grafo[destino] 
		self.grafo[destino] = node 

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
	V = 6
	grafo = Grafo(V) 
	grafo.add_vert(1,2) 
	grafo.add_vert(1,5) 
	grafo.add_vert(2,5) 
	grafo.add_vert(2,3) 
	grafo.add_vert(2,4) 
	grafo.add_vert(5,4) 
	grafo.add_vert(4,3) 

	grafo.print_grafo()