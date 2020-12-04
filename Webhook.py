from flask import Flask
import git
import sys

app = Flask(__name__)

folder = sys.argv[1] 
port = sys.argv[2]

@app.route('/', methods=['POST'])
def index():
    g = git.cmd.Git(folder)
    g.pull("https://github.com/smeup/doc-template", "master")
    return "True"

if __name__ == '__main__':
        app.run(debug = False,host='0.0.0.0',port=port)