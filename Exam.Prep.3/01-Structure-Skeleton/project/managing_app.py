from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route
from project.user import User


class ManagingApp:
    VALID_VEHICLES = ["PassengerCar", "CargoVan"]

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        current_user = User(first_name, last_name, driving_license_number)
        self.users.append(current_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == "PassengerCar":
            current_vehicle = PassengerCar(brand, model, license_plate_number)
        else:
            current_vehicle = CargoVan(brand, model, license_plate_number)

        self.vehicles.append(current_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        current_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(current_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        current_user = None
        current_route = None
        current_vehicle = None

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                if user.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                current_user = user

        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                if v.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
                current_vehicle = v

        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                current_route = route

        current_vehicle.drive(current_route.length)
        if is_accident_happened:
            current_vehicle.change_status()
            current_user.decrease_rating()

        else:
            current_user.increase_rating()

        return current_vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = []
        for v in self.vehicles:
            if v.is_damaged:
                damaged_vehicles.append(v)

        damaged_vehicles.sort(key=lambda v: (v.brand, v.model))
        if count > len(damaged_vehicles):
            for v in damaged_vehicles:
                v.change_status()
                v.recharge()
            final_count = len(damaged_vehicles)

        else:
            for v in range(len(damaged_vehicles), count):
                damaged_vehicles[v].change_status()
                damaged_vehicles[v].recharge()
            final_count = count

        return f"{final_count} vehicles were successfully repaired!"

    def users_report(self):

        self.users.sort(key=lambda u: -u.rating)

        result = ["*** E-Drive-Rent ***"]
        for user in self.users:
            result.append(user.__str__())

        return "\n".join(result)
