class Product:
    
    def __init__(self, description, price, *ratings):
        self.description = description
        self.price = price
        self.ratings = list(ratings)

    def taxPayable(self):
        return self.price * 0.20
    
    def __str__(self):
        return f"{self.description}, £{self.price}, {self.ratings}"