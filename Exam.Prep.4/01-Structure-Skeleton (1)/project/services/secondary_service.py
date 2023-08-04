from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self):
        if not self.robots:
            return f"{SecondaryService.__class__.__name__} Secondary Service:\n" \
                   f"Robots: none"

        else:
            return f"{SecondaryService.__class__.__name__} Secondary Service:\n" \
                   f"Robots: {' '.join(self.robots)}"
