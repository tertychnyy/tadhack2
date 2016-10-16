# -*- coding: utf-8 -*-
from c1cli.exceptions import ClientException
from c1cli.bots.models import Bot


def get(client):
    """
    Lists all user bots
    :param client: Current Client object
    :return:
    """
    _method = "/bots/"

    data = client.get(_method)

    # Prepare retval list
    retval = list()
    for item in data:
        retval.append(Bot(item))

    return retval


def get_by_name(client=None, bot_name=None):
    """
    Gets bot by name
    :param client: Current Client object
    :param bot_name: Name of Bot to fetch
    :return:
    """
    if client is None:
        raise ClientException("Client obj not initialized", 404)

    try:
        _method = "/bots/" + str(bot_name)
    except:
        raise ClientException("Illegal bot_name param", 400)

    try:
        data = client.get(_method)
    except ClientException as e:
        if e.ec == 404:
            # Bot not found
            return None
        else:
            raise e

    # Prepare retval list
    retval = Bot(data)

    return retval


def save(client=None, usertoken=None, bot=None):
    """
    Saves new bot
    :param client: Current Client object
    :param usertoken: User token
    :param bot: Bot object to save
    :return:
    """
    if client is None:
        raise ClientException("Client obj not initialized", 400)
    if bot is None:
        raise ClientException("Bot obj not initialized", 400)
    if usertoken is None:
        raise ClientException("User Token not initialized", 400)

    _method = "/bots?usertoken=" + str(usertoken)

    data = client.post(_method, json=bot.to_json())

    # Prepare retval list
    retval = Bot(data)

    return retval


def update(client=None, bot=None):
    """
    Updates existing bot
    :param client: Current Client object
    :param bot: Bot object to update
    :return:
    """
    if client is None:
        raise ClientException("Client obj not initialized", 400)
    if bot is None:
        raise ClientException("Bot obj not initialized", 400)

    try:
        _method = "/bots/" + str(bot.name)
    except:
        raise ClientException("Illegal Bot obj", 400)

    data = client.put(_method, json=bot.to_json())

    # Prepare retval list
    retval = Bot(data)

    return retval


def delete(client=None, bot_name=None):
    """
    Deletes existing bot
    :param client: Current Client object
    :param bot_name: Name of Bot to delete
    :return:
    """
    if client is None:
        raise ClientException("Client obj not initialized", 400)
    if bot_name is None:
        raise ClientException("Bot name not initialized", 400)

    try:
        _method = "/bots/" + str(bot_name)
    except:
        raise ClientException("Illegal bot_name param", 400)

    data = client.delete(_method)

    # Prepare retval list
    retval = Bot(data)

    return retval