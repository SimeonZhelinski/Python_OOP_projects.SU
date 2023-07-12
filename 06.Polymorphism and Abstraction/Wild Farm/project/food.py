from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity
