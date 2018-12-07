
from bfs2 import Queue, bfs, getPath
from buildGraph import Graph


if __name__ == '__main__':
    """ Enter Input here  """
    word1 = input ("Enter the first word : ")
    word2 = input ("Enter the second word : ")
    
    # if len(sys.argv) > 1:


    #     word1=sys.argv[1]
    #     word2=sys.argv[2]

    if word1 in Graph:

        start = Graph[word1]
        if word2 in Graph:
            finish=Graph[word2]
            predecessors = bfs(start, finish, Graph)
            path = getPath(start, finish, predecessors) 
            str = ''

            for p in path:

                str += p + ' -> '

            print (str[:-3])
	    
    	
        else:
             print("Word2 not in Graph") 

	
    else:
        print("Word1 not in Graph")










