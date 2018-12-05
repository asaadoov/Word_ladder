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

    if (len(word1) == len(word2)):
        valid = True
    else:
        valid = False

    if word1 in Graph:

        start = Graph[word1]
        if word2 in Graph:
            finish = Graph[word2]
            predecessors = bfs(start, finish, Graph)
            path = getPath(start, finish, predecessors)
            length = len(path)
        return render_template("result.html", firstWord=word1, lastWord=word2, path=path, valid=valid, len=length)


if __name__ == '__main__':
    app.run(port=5, debug=True)
