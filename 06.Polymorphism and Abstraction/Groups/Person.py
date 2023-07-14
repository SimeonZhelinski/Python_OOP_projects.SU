from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        name = self.name
        surname = other.surname
        person = Person(name, surname)
        return person


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group = Group(f"{self.name} {other.name}", self.people + other.people)
        return new_group

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(Person.__repr__() for Person in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people.__getitem__(item)}"
