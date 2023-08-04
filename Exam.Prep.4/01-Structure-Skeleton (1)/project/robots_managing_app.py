from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = ["MainService", "SecondaryService"]
    VALID_ROBOT_TYPES = ["MaleRobot", "FemaleRobot"]

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        current_service = None

        if service_type == "MainService":
            current_service = MainService(name)
        if service_type == "SecondaryService":
            current_service = SecondaryService(name)

        self.services.append(current_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        current_robot = None

        if robot_type == "MaleRobot":
            current_robot = MaleRobot(name, kind, price)
        if robot_type == "FemaleRobot":
            current_robot = FemaleRobot(name, kind, price)

        self.robots.append(current_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = None
        current_service = None

        for robot in self.robots:
            if robot.name == robot_name:
                current_robot = robot

        for ser in self.services:
            if ser.name == service_name:
                current_service = ser

        if current_robot.__class__.__name__ == "MaleRobot" and current_service.__class__.__name__ == "MainService":
            if current_service.capacity > 0:
                current_service.robots.append(current_robot)
                self.robots.remove(current_robot)
            else:
                raise Exception("Not enough capacity for this robot!")

        elif current_robot.__class__.__name__ == "FemaleRobot" and current_service.__class__.__name__ == "SecondaryService":
            if current_service.capacity > 0:
                current_service.robots.append(current_robot)
                self.robots.remove(current_robot)
            else:
                raise Exception("Not enough capacity for this robot!")

        else:
            return "Unsuitable service."

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        current_robot = None

        for ser in self.services:
            if ser.name == service_name:
                for robot in ser.robots:
                    if robot.name == robot_name:
                        current_robot = robot
                        ser.robots.remove(robot)
                    else:
                        raise Exception("No such robot in this service!")

        self.robots.append(current_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        count = 0
        for ser in self.services:
            if ser.name == service_name:
                count = len(ser.robots)
                for robot in ser.robots:
                    robot.eating()

        return f"Robots fed: {count}."

    def service_price(self, service_name: str):
        all_prices = []
        for ser in self.services:
            if ser.name == service_name:
                for robot in ser.robots:
                    all_prices.append(robot.price)

        total_price = sum(all_prices)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for ser in self.services:
            result.append(ser.details())

        return "\n".join(result)


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
