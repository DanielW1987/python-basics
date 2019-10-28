class Product:

    # constructor
    def __init__(self):
        # define instance variables
        self.name = "Smartphone"
        self.description = "Awesome description"
        self.price = 700.50


product: Product = Product() # invokes __init__()
assert product.name == "Smartphone"
assert product.description == "Awesome description"
assert product.price == 700.50
