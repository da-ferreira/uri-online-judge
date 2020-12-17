
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
            
            # Se o elemento for menor, ele segue descendo à esquerda,
            # caso contrário, segue descendo à direita.
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
    

    # Percurso em pós ordem: exibi os filhos da esquerda e direita antes de mostrar a sí mesmo,
    # visitando recursivamente sua sub-árvore da esquerda, e depois sua sub-árvore da direta. 

    def post_order_route(self, node=None):
        if node is None:  # Começa o percurso pela raíz da árvore
            node = self.root

        if node.left is not None:
            self.post_order_route(node.left)
        
        if node.right is not None:
            self.post_order_route(node.right)
        
        REPRES.append(str(node))

        return REPRES


casos = int(input())

for i in range(casos):
    quantidade = int(input())
    numeros = list(map(int, input().split()))

    bst = BinarySearchTree()

    for j in numeros:
        bst.insert(j)

    print(f'Case {i + 1}:')

    REPRES.clear()

    pre_ordem = bst.pre_order_route()    
    print(f'Pre.: {" ".join(pre_ordem)}')

    REPRES.clear()

    in_ordem = bst.inorder_route()
    print(f'In..: {" ".join(in_ordem)}')

    REPRES.clear()

    pos_ordem = bst.post_order_route()
    print(f'Post: {" ".join(pos_ordem)}')

    print()
 