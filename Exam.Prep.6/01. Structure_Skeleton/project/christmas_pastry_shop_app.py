from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:
    VALID_TYPES_DELICACIES = ["Gingerbread", "Stolen"]
    VALID_TYPES_BOOTH = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_TYPES_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        if type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_TYPES_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        if type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_booth = None
        current_delicacy = None

        for booth in self.booths:
            if booth.booth_number == booth_number:
                current_booth = booth

        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")

        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                current_delicacy = delicacy

        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        all_orders = []

        for orders in current_booth.delicacy_orders:
            all_orders.append(orders.price)

        total_bill = sum(all_orders) + current_booth.price_for_reservation
        self.income += total_bill

        current_booth.delicacy_orders.clear()
        current_booth.price_for_reservation = 0
        current_booth.is_reserved = False

        return (f"Booth {booth_number}:\n"
                f"Bill: {total_bill:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
