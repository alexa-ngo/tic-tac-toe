class Player:

    def __init__(self, x_or_o):
        self._role = x_or_o

    def get_player_role(self):
        return self._role

    def set_player_role(self):
        if self._role == "x":
            self._role = "o"
        self._role = "o"
        return