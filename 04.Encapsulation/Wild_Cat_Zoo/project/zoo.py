from project.animal import Animal
from project.worker import Worker
from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal} the {type(animal)} added to the zoo"
        elif price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            self.__workers_capacity -= 1
            return f"{worker} the {type(worker)} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            fired_worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(fired_worker)
            self.__workers_capacity += 1
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        sum_salaries += next(filter(lambda s: s.salary, self.workers))
        if sum_salaries <= self.__budget:
            return f"You payed your workers. They are happy. Budget left: {self.__budget - sum_salaries}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_tend = 0
        sum_tend += next(filter(lambda a: a.money_for_care, self.animals))
        if sum_tend <= self.__budget:
            return f"You tended all the animals. They are happy. Budget left: {self.__budget - sum_tend}"

    def profit(self, amount):
        self.__budget += amount

    def animal_status(self):
        pass

    def worker_status(self):
        pass


from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet

zoo = Zoo("Zootopia", 3000, 5, 8)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
# Animal prices
prices = [200, 190, 204, 156, 211, 140]
# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]
# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
price = prices[i]
print(zoo.add_animal(animal, price))
# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))
# Tending animals
print(zoo.tend_animals())
# Paying keepers
print(zoo.pay_workers())
# Fireing worker
print(zoo.fire_worker("Adam"))
# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
