from flask import Flask, render_template, request
from bfs2 import Queue, bfs, getPath
from bfs2 import Queue, bfs, getPath
from buildGraph import Graph

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getInput():

    word1 = request.form['firstWord']
    word2 = request.form['lastWord']

    # if (type(word1) is 'int'  or type(word1) == int):
    #     print(type(word1))
    #     return render_template('resultFail.html', msg='One of the inputs is not a word')

    if ((word1 in Graph and word2 in Graph) and (len(word1) != len(word2))):
        return render_template('resultFail.html', msg='the two words have different lengths')

    elif (not (word1 in Graph and word2 in Graph)):
        return render_template('resultFail.html', msg='One of the words is not in the list')

    elif (word1 is word2):
        return render_template('resultFail.html', msg='the two words are the same')

    elif (len(word1) == len(word2)):

        if (word1 not in Graph or word2 not in Graph):
            return render_template('resultFail.html', msg='One of the words is not in the list')

        elif word1 in Graph:
            start = Graph[word1]
            if word2 in Graph:
                finish = Graph[word2]
                predecessors = bfs(start, finish, Graph)
                path = getPath(start, finish, predecessors)
                length = len(path)
                print(path, length)
                if (length == 2):
                    return render_template('resultFail.html', msg='There is no path between these two words in the list')
                elif (length != 2):
                    return render_template("result.html", firstWord=word1, lastWord=word2, path=path, len=length)


if __name__ == '__main__':
    app.run(port=5, debug=True)
