'''
[SOLID]
Open-Closed Principle - a system should be open for extension, closed to modification

Decorator Pattern [Head First Design Pattern]
: attaches additional responsibilities to an object dynamically. 
  Decorators provide a flexible alternative to subclassing for extending the functionality.


Pizza Order
- different type of pizza bases
- different type of toppings

'''
from abc import ABC, abstractmethod
# Step 1: Create a Pizza class, instance variables for each type of toppings in pizza base class
class Pizza:
    def __init__(self):
        """
        Initialize the Pizza with no toppings by default.
        """
        self.cheese = False
        self.paneer = False
        self.olive = False
        self.mushroom = False
        self.veg = False
        self.chili = False

    def description(self):
        """
        Placeholder method for the description of the pizza.
        """
        pass

    def get_price(self):
        """
        Placeholder method for getting the price of the pizza.
        """
        pass

# Step 2: Apply decorator pattern
# Basic Pizza Object: start by creating a basic pizza object. This object represents a plain pizza w/o any toppings.
# Implement toppings (e.g., cheese, paneer, olive) using the decorator pattern. The decorator wraps the basic pizza object and adds new functionality (e.g., adding the price of the topping).
# Call the get_price() Method:	
#   Finally, call the get_price() method to calculate the total cost of the pizza.
#   The decorator invokes the get_price() method of the wrapped object, adds its own price, and delegates the remaining calculation to the inner object.
#   This step-by-step process ensures the total cost is calculated incrementally.

# Abstract base class for Pizza
class Pizza(ABC):
    def __init__(self):
        self.description = "Basic Pizza"

    def get_description(self):
        return self.description

    @abstractmethod
    def get_price(self):
        pass


class Domino(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Watch the pizza of your wildest dreams come to life!"

    def get_price(self):
        return 15

# Abstract decorator class for extra toppings
class ExtraToppings(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

# Concrete decorators for specific toppings
class Cheese(ExtraToppings):
    def get_description(self):
        return super().get_description() + ", Cheese"

    def get_price(self):
        return self.pizza.get_price() + 5


class Paneer(ExtraToppings):
    def get_description(self):
        return super().get_description() + ", Paneer"

    def get_price(self):
        return self.pizza.get_price() + 4


class Olive(ExtraToppings):
    def get_description(self):
        return super().get_description() + ", Olive"

    def get_price(self):
        return self.pizza.get_price() + 3

# Example usage
if __name__ == "__main__":
    # Base pizza (Domino)
    pizza = Domino()

    # Add toppings
    pizza = Paneer(pizza)
    pizza = Olive(pizza)
    pizza = Cheese(pizza)

    # Print final description and price
    print("Description:", pizza.get_description())  # Watch the pizza of your wildest dreams come to life!, Paneer, Olive, Cheese
    print("Total Price: $", pizza.get_price())  # 25 + 4 + 3 + 5 = 37