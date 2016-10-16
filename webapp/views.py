from c1cli.entities.CoreResponse import ActionResponse
from flask import jsonify, request
from webapp.scripts import get_suggestions_by_name, get_recipe_by_name, get_discount
from webapp.wsgi import bot


@bot.route("/")
def hello():
    name = request.args.get('name', None)
    if name is None:
        raise AttributeError

    rv = ActionResponse()

    suggestions = get_suggestions_by_name(name)

    recipe = get_recipe_by_name(name)

    discount = get_discount(name)

    msg1 = "Customers Who Bought This Item Also Bought: {suggestions}".format(suggestions="\n".join(suggestions))
    msg2 = "Recipe by Jamie Oliver: {recipe}".format(recipe=recipe)
    msg3 = "Save {discount} by joining Carrefour MyClub http://carrefourmyclub.com".format(discount=discount)

    rv.messages = [msg1, msg2, msg3]
    return jsonify(rv.to_dict())
