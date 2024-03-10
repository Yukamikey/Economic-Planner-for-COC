class Good:
    def __init__(self, name: str, price: float, num_produced: int):
        self.name = name
        self.price = price
        self.num_produced = num_produced

    def rename(self, new_name: str):
        self.name = new_name

    def reprice(self, new_price: float):
        self.price = new_price

    def produce(self, stacks_added: float):
        self.num_produced += (stacks_added * 64)