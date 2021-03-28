from math import inf


class TrieNode(object):
    def __init__(self, word, first, last):
        self.word = word
        self.children = {}
        self.parents = None
        self.end_of_the_word = False
        self.link = None
        self.first = first
        self.last = last

    def add(self, child):
        self[self.word[child.first]] = child

    @property
    def edge(self):
        return self.first, max(self.first, self.last - 1)

    def __getitem__(self, i):
        return self.children[i]

    def __setitem__(self, i, child):
        self.children[i] = child


def test_and_split(root, k, i, char, word):
    if k <= i:
        root_ = root[word[k]]
        k_, i_ = root_.edge
        if char == word[k_ + i - k + 1]:
            return True, root
        else:
            new_node = TrieNode(word, k_, k_ + i - k + 1)
            root.add(new_node)
            root_.first = k_ + i - k + 1
            new_node.add(root_)
            return False, new_node
    else:
        if char in root.children:
            return True, root
        else:
            return False, root


def canonize(root, k, p, word):
    if p < k:
        return root, k
    else:
        root_ = root[word[k]]
        k_, p_ = root_.edge
        while p_ - k_ <= p - k:
            k = k + p_ - k_ + 1
            root = root_
            if k <= p:
                root_ = root[word[k]]
                k_, p_ = root_.edge
        return root, k


def update(root, k, i, word):
    old_root = root
    end_point, r = test_and_split(root, k, i - 1, word[i], word)
    while not end_point:
        root_ = TrieNode(word, i, inf)
        r.add(root_)
        if old_root != root:
            old_root.link = r
        old_root = r
        root, k = canonize(root.link, k, i - 1, word)
        end_point, r = test_and_split(root, k, i - 1, word[i], word)
    if old_root != root:
        old_root.link = root
    return root, k


def Ukkonen(root, word):
    trie = TrieNode(word, None, None)
    for i in word:
        trie[i] = root
    root.link = trie
    node = root
    k = 0
    for i in range(len(word)):
        node, k = update(node, k, i, word)
        node, k = canonize(node, k, i, word)


tab = []


def print_trie(root):
    node = root
    for i in node.children.values():
        if i.last != inf:
            tab.append([i.word[i.first:i.last]])
        else:
            tab.append([i.word[i.first:]])
        print_trie(i)
    return tab


if __name__ == '__main__':
    text = "abc"
    root = TrieNode(text, 0, 0)
    Ukkonen(root, text)
    print(print_trie(root))
