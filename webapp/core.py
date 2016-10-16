import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../out3.txt")
with open(path, "r") as o:
    s = o.read()
    tickets = json.loads(s)
