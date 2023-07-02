from project.product import Product
from typing import List


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product_find = next(filter(lambda p: p.name == product_name, self.products))
            return product_find
        except StopIteration:
            pass

    def remove(self, product_name):
        try:
            product_remove = next(filter(lambda p: p.name == product_name, self.products))
            self.products.remove(product_remove)
        except StopIteration:
            pass

    def __repr__(self):
        output = []
        for p in self.products:
            output.append(f"{p}: {p.quantity}")
        return "\n".join(output)
