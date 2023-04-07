from flask import Flask
from .Decision_Tree import decision_tree
import time

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/test')
def test():
    return decision_tree.decision_tree([[1,2],[4,2],[1,5],[1,1],[3,2],[2,2]], [1,2,3,4,1,2], attributes=["a", "b"])