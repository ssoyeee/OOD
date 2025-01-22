'''
You are going to subscribe to a few stocks that will notify us when their price drops below a certain threshold as well as it will also notify when it rises beyond our expectations


Assume you have an object, X, that holds some data.
Now, imagine a list of other objects that need to be notified whenever the data in X changes.
This is a perfect scenario to apply the Observer Pattern.

'Observer pattern = Publishers + Subscribers'
ex) In stock market, a stock: subject, mobile app/software that display price of stock: observer
'''

# Step1: create an interface Stock contains methods to add, remove, and notify the observers
# Step2: Implement observer
from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update_price(self, current_price: float):
        """Update the current price for the observer."""
        pass


# Additional interface for displaying changes (not part of the Observer pattern)
class DisplayElement(ABC):
    @abstractmethod
    def display_price(self):
        """Display the current price."""
        pass


# Stock interface
class Stock(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concrete Stock implementation (Tesla)
class Tesla(Stock):
    def __init__(self):
        self.observers = []
        self.current_price = 0.0
        self.threshold = 0.0

    def register_observer(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_price(self.current_price)

    def price_changed(self):
        # Notify observers if price crosses the threshold
        if self.current_price <= self.threshold or self.current_price >= self.threshold:
            self.notify_observers()

    def set_price(self, price: float):
        self.current_price = price
        self.price_changed()

    def set_threshold(self, threshold: float):
        self.threshold = threshold


# Concrete Observer implementation (Investor)
class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update_price(self, price: float):
        print(f"{self.name} has been notified: Tesla's price is now ${price:.2f}")


# Concrete implementation of Observer and DisplayElement
class AppDisplay(Observer, DisplayElement):
    def __init__(self, stock_data: Stock):
        """
        Initialize the observer with a reference to the subject (Stock).
        Automatically registers itself with the subject.
        """
        self.current_price = 0.0
        self.stock_data = stock_data
        stock_data.register_observer(self)

    def update_price(self, current_price: float):
        """
        Update the current price and display it.
        """
        self.current_price = current_price
        self.display_price()

    def display_price(self):
        """
        Display the current price of Tesla.
        """
        print(f"Current Price of Tesla: ${self.current_price:.2f}")


# Main execution
if __name__ == "__main__":
    # Create an object for the subject (Tesla stock)
    tesla_stock = Tesla()

    # Set a price threshold
    tesla_stock.set_threshold(670.0)

    # Create objects for observers and register them with the subject
    mobile_screen = AppDisplay(tesla_stock)
    web_screen = AppDisplay(tesla_stock)  # Example for another observer
    api_observer = AppDisplay(tesla_stock)  # Example for third-party API observer

    # When the stock price is updated, observers will be notified if conditions are met
    tesla_stock.set_price(660.08)  # Notification triggered
    tesla_stock.set_price(678.10)  # Notification triggered