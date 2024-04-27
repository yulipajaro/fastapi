from abc import ABC, abstractmethod
from datetime import datetime

class MovieTicketDiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, age: int, is_military: bool, date: datetime) -> float:
        pass

class ChildDiscount(MovieTicketDiscountStrategy):
    def apply_discount(self, age: int, is_military: bool, date: datetime) -> float:
        if age < 5:
            return 0.05
        else:
            return 0

class MilitaryDiscount(MovieTicketDiscountStrategy):
    def apply_discount(self, age: int, is_military: bool, date: datetime) -> float:
        if is_military:
            return 0.1
        else:
            return 0

class WeekdayDiscount(MovieTicketDiscountStrategy):
    def apply_discount(self, age: int, is_military: bool, date: datetime) -> float:
        if date.weekday() < 5:  # Monday to Friday
            return 0.1
        else:
            return 0

class NormalPrice(MovieTicketDiscountStrategy):
    def apply_discount(self, age: int, is_military: bool, date: datetime) -> float:
        return 0

class MovieTicket:
    def _init_(self, age: int, is_military: bool, date: datetime, discount_strategy: MovieTicketDiscountStrategy):
        self.age = age
        self.is_military = is_military
        self.date = date
        self.discount_strategy = discount_strategy

    def get_price(self) -> float:
        base_price = 10.0  # Base price of movie ticket
        discount = self.discount_strategy.apply_discount(self.age, self.is_military, self.date)
        return base_price - (base_price * discount)

if _name_ == "_main_":
    # Example usage
    ticket1 = MovieTicket(age=3, is_military=False, date=datetime(2024, 4, 30), discount_strategy=ChildDiscount())
    print("Ticket 1 Price:", ticket1.get_price())

    ticket2 = MovieTicket(age=25, is_military=True, date=datetime(2024, 4, 30), discount_strategy=MilitaryDiscount())
    print("Ticket 2 Price:", ticket2.get_price())

    ticket3 = MovieTicket(age=30, is_military=False, date=datetime(2024, 5, 2), discount_strategy=WeekdayDiscount())
    print("Ticket 3 Price:", ticket3.get_price())

    ticket4 = MovieTicket(age=40, is_military=False, date=datetime(2024, 5, 4), discount_strategy=NormalPrice())
    print("Ticket 4 Price:", ticket4.get_price())