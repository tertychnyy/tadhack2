import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../out3.txt")
with open(path, "r") as o:
    s = o.read()
    tickets = json.loads(s)

r = dict()
r["Count"] = 0
r["Entities"] = []
r["ForcedKeyboard"] = None
r["ForcedState"] = None
r["Messages"] = ["Customers Who Bought This Item Also Bought: Vino Riesling Clas\nBolsa Carrefour\nQueso Gran Biraghi", "Recipe by Jamie Oliver: riesling", "Save 0.0 by joining Carrefour MyClub http://carrefourmyclub.com"]

cache = dict(riesling=r)
