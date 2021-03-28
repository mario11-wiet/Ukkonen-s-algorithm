k = 0


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.parents = None
        self.end_of_the_word = False
        self.k = 0


def add(root_, word):
    global k
    node = root_
    for i in word:
        is_char = False
        for j in node.children:
            if j.char == i:
                node = j
                is_char = True
                break
        if not is_char:
            new_node = TrieNode(i)
            new_node.parents = node
            k = k + 1
            new_node.k = k
            node.children.append(new_node)
            node = new_node
    node.end_of_the_word = True


def add_suffix(root_, word):
    for i in range(len(word)):
        # print(word[i:])
        add(root_, word[i:])


def find_suffix(root, word):
    if len(root.children) == 0:
        return False

    node = root
    for i in word:
        is_char = False
        for j in node.children:
            if j.char == i:
                is_char = True
                node = j
                break
        if not is_char:
            return False

    return True


tab = []


import matplotlib.pyplot as plt
import networkx as nx
import random


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


class Visualization:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self, root):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        pos = hierarchy_pos(G, root.char + str(root.k))
        nx.draw(G, pos=pos, with_labels=True)
        plt.savefig('hierarchy.png')
        plt.show()
        # nx.draw_networkx(G)
        # plt.show()


def print_trie(root):
    node = root
    for i in node.children:
        tab.append([node.char + str(node.k), i.char + str(i.k)])
        print_trie(i)
    return tab


if __name__ == "__main__":
    root_ = TrieNode('?')
    add_suffix(root_, "abcbcsodd")
    print(find_suffix(root_, "Art"))
    tab1 = (print_trie(root_))
    tab1.sort()
    print(tab1)
    G = Visualization()
    for i in range(len(tab1)):
        G.addEdge(tab1[i][0], tab1[i][1])
    G.visualize(root_)
