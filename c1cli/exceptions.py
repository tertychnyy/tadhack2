class ClientException(Exception):
    """Raise when client gets wrong ec"""
    def __init__(self, message, ec, *args):
        self.message = message
        self.ec = ec
        super(ClientException, self).__init__(message, ec, *args)