# https://www.youtube.com/watch?v=BXeIu54mUg0&t=1s


class Node:
    def __init__(self, key=None, word=None):
        self.key = key
        self.word = word
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def put(self, word):
        node = self.head

        for char in word:
            if char not in node.children:
                node.children[char] = Node(key=char)
            node = node.children[char]

        node.word = word

    def exist(self, word):
        node = self.head

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.word == word

    def search(self, query):
        node = self.head

        for char in query:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        words = []
        Q = node.children.items()
        while Q:
            key, node = Q.pop(0)
            Q.extend(node.children.items())
            if node.word:
                words.append(node.word)

        return words


if "__main__" == __name__:
    trie = Trie()
    trie.put("cat")
    trie.put("catering")
    trie.put("category")
    trie.put("cake")
    trie.put("abs")
    trie.put("abba")
    trie.put("abroad")
    trie.put("jesus")
    trie.put("jeus")

    assert trie.exist("cat")
    assert not trie.exist("cate")
    assert trie.exist("jesus")
    assert not trie.exist("jean")

    print(trie.search("cate"))

    print(trie.search("je"))
    print(trie.search("jes"))
