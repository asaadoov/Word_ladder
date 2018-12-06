import pickle
def buildWordGraph(file):
    w = {}
    f = open(file)
    words = f.read().split('\n')

    for word in words:

        for i in range(len(word)):
            wcard = word[:i] + '*' + word[i + 1:]
            # print (wcard)
            if wcard in w:
                w[wcard].append(word)
            else:
                w[wcard] = [word]
    return w
   

file="oxford_3000.txt"
Dic=buildWordGraph(file) 

pickleOut = open ("dict3.pickle","wb")
pickle.dump (Dic, pickleOut)     
pickleOut.close()  
