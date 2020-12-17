
ROOT = 'root'
REPRES = []

class Node:
    def __init__(self, element):  # atributos da classe
        self.data = element
        self.left = None
        self.right = None


    def __str__(self):
        return f'{self.data}'


class BinarySearchTree:
    def __init__(self, element=None, node=None):

        # Iniciando a raíz da árvore a partir de um nó já criado.        
        if node is not None:
            self.root = node

        # Caso contrário, cria-se um nó e atribui para a raíz da árvore.
        elif element is not None:
            self.root = Node(element)
        else:
            self.root = None
    

    def insert(self, element):
        father = None  # pai do elemento que será inserido
        point = self.root

        while point is not None:
            father = point
            
            if element < point.data:
                point = point.left
            else:
                point = point.right
            
        # Se a árvore estiver vazia, o elemento que entra é a raíz.
        if father is None:
            self.root = Node(element)
        
        # Adicionando o elemento
        elif element < father.data:
            father.left = Node(element)
        else:
            father.right = Node(element)
    

    def route_at_level(self, node=ROOT):
        if node == ROOT:
            node = self.root
        
        queue = []
        queue.append(node)  # insere no final, e remove do inicio

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
            
            REPRES.append(str(node))
        
        return REPRES


casos = int(input())
        
for i in range(casos):
    quantidade = int(input())
    numeros = list(map(int, input().split()))

    bst = BinarySearchTree()

    for j in numeros:
        bst.insert(j)

    REPRES.clear()
    percurso = bst.route_at_level()

    print(f'Case {i + 1}:')
    print(' '.join(percurso))
    print()
