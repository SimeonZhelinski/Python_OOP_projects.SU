class BaseStack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


class AddBaseStack(BaseStack):
    def push(self, element):
        self.data.append(element)


class RemoveBaseStack(BaseStack):
    def pop(self):
        last_element = self.data.pop()
        return last_element


class TopBaseStack(BaseStack):
    def top(self):
        return self.data[-1]


class Stack(AddBaseStack, RemoveBaseStack, TopBaseStack):
    pass
