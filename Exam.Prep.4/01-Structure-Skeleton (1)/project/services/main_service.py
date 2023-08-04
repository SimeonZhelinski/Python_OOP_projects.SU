from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"

        else:
            robot_names = [r.name for r in self.robots]
            return f"{self.name} Main Service:\n" \
                   f"Robots: {' '.join(robot_names)}"
