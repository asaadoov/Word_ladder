from flask import Flask, render_template, request
from bfs2 import Queue, bfs, getPath
from buildGraph import Graph
from checker import checker

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getInput():

    word1 = (request.form['firstWord']).strip().lower()
    word2 = (request.form['lastWord']).strip().lower()

    if ((word1 in Graph and word2 in Graph) and (len(word1) != len(word2))):
        return render_template('resultFailure.html', msg='The two words have different lengths')

    elif (word1 == word2):
        return render_template('resultFailure.html', msg='The two words are the same')

    elif (not (word1 in Graph and word2 in Graph)):
        return render_template('resultFailure.html', msg='One of the words is not in the list')

    elif (len(word1) == len(word2)):

        if (word1 not in Graph or word2 not in Graph):
            return render_template('resultFailure.html', msg='One of the words is not in the list')

        elif word1 in Graph:
            start = Graph[word1]
            if word2 in Graph:
                finish = Graph[word2]
                predecessors = bfs(start, finish, Graph)
                path = getPath(start, finish, predecessors)
                length = len(path)
                count = checker(word1, word2)
                print(path, length)
                print(count)
                if ((length == 2) and (count > 1)):
                    return render_template('resultFailure.html', msg='There is no path between these two words in the list')
                else:
                    return render_template("resultSuccess.html", firstWord=word1, lastWord=word2, path=path, len=length)


if __name__ == '__main__':
    app.run(port=5004, debug=True)
