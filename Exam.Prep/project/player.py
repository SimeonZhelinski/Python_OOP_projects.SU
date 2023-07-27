class Player:
    _all_players = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        self.__name = value

        if Player.name_exists(self.__name):
            raise Exception(f"Name {self.__name} is already used!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value
        if self.__stamina < 100:
            self.need_sustenance = True

    @classmethod
    def name_exists(cls, name):
        for player in cls._all_players:
            if player.name == name:
                return True
            return False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
