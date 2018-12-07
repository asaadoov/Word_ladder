import pickle
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    __slots__ = ('name', 'neighbours')

    def __str__(self):
        result = self.name + ' : '
        for n in self.neighbours:
            result += n.name + ', '
        return result[:-1]

def buildDice() :
    pickleIn = open ("dict.pickle","rb")
    w=pickle.load(pickleIn)
    # print (w)
    for key in w:
            
        wordlist = w[key]
        for w1 in wordlist:
                # print (wordlist)
            for w2 in wordlist:
                if w1 != w2:
                    inputGraph(w1, w2)

def inputGraph(word1, word2):

    if word1 not in Graph:
        node = Node(word1)
        node.neighbours.append(Node(word2))
        Graph[word1] = node
    else:
        neighbours = Graph[word1].neighbours
        if word2 not in [x.name for x in neighbours]:
            neighbours.append(Node(word2))

    if word2 not in Graph:
        node = Node(word2)
        node.neighbours.append(Node(word1))
        Graph[word2] = node
    else:
        neighbours = Graph[word2].neighbours

        if word1 not in [x.name for x in neighbours]:
            neighbours.append(Node(word1))


   
    
Graph = {}

buildDice()
# file="words.txt"

# buildWordGraph(file) 
