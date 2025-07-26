class Server:
    def __init__(self, env):
        self.reqres = {
            "rc": "https://reqres.in"
        }[env]