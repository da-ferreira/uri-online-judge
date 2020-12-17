
ROOT = 'root'
REPRES = []

# o nó permite ligar os elementos esparsos da árvore
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
    

    def search(self, element, node=0):

        # Começa a busca pela raíz.
        if node == 0:
            node = self.root

        # Caso o item não esteja na árvore retorna None
        if node is None:
            return node

        # Retorna uma sub-árvore
        elif node.data == element:
            return BinarySearchTree(node=node)
        
        elif element < node.data:
            return self.search(element, node.left)  # Se o elemento for menor que o valor do nó, ele segue pela esquerda.
        
        return self.search(element, node.right)  # Se for maior, segue pela direita.


    def pre_order_route(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node is not None:
            REPRES.append(str(node))

            self.pre_order_route(node.left)
            self.pre_order_route(node.right)
        
        return REPRES
            

    def inorder_route(self, node=None):
        if node is None:
            node = self.root
        
        # Chamando recursivamente e mostrando os elementos

        if node.left is not None:
            self.inorder_route(node.left)
        
        REPRES.append(str(node))

        if node.right is not None:
            self.inorder_route(node.right)
        
        return REPRES
    

    def post_order_route(self, node=None):
        if node is None:  # Começa o percurso pela raíz da árvore
            node = self.root

        if node.left is not None:
            self.post_order_route(node.left)
        
        if node.right is not None:
            self.post_order_route(node.right)
        
        REPRES.append(str(node))

        return REPRES


bst = BinarySearchTree()

while True:
    try:
        operacao = input().split()

        if len(operacao) == 2:
            if operacao[0] == 'I':
                bst.insert(operacao[1])
            else:
                temp = bst.search(operacao[1])

                if temp is None:
                    print(f'{operacao[1]} nao existe')
                else:
                    print(f'{operacao[1]} existe')
        else:
            if operacao[0] == 'INFIXA':
                REPRES.clear()

                infixa = bst.inorder_route()
                print(' '.join(infixa))

            elif operacao[0] == 'PREFIXA':
                REPRES.clear()

                prefixa = bst.pre_order_route()
                print(' '.join(prefixa))
            
            else:
                REPRES.clear()

                posfixa = bst.post_order_route()
                print(' '.join(posfixa))
    except EOFError:
        break
