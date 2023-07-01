from App.app import DB


class TokenModel(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True)
    token = DB.Column(DB.String(150))

    def __init__(self, token : str):
        self.token = token

        
    def __repr__(self):
        return "<Token %r>"%self.token