class Killmail:
    def __init__(self, payload, *args, **kwargs):
        try:
            self.id = None
            self.killmail = None
            p = payload['package']
            if p is not None:
                self.id = p['killID']
                self.killmail = p['killmail']
        except KeyError:
            print('Malforned killmail passed in!');
            raise ValueError
