from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        if not self.robots:
            return f"{MainService.__class__.__name__} Main Service:\n" \
                   f"Robots: none"

        else:
            return f"{MainService.__class__.__name__} Main Service:\n" \
                   f"Robots: {' '.join(self.robots)}"
