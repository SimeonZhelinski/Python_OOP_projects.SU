class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, name: str):
        if 5 < len(name) <= 15:
            self.__username = name
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @password.setter
    def password(self, p_word: str):
        upper = False
        lower = False
        for char in p_word:
            if char.isupper():
                upper = True
            if char.isnumeric():
                lower = True
        if len(p_word) >= 8 and upper and lower:
            self.__password = p_word
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
