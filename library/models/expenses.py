import json
from library.models.purchase import Purchase
from typing import List, Generator, Tuple

class Expenses:
    def __init__(self, filename = "data/expenses.json"):
        self.expenses = []
        self.filename = filename
        self.load()

    def load(self) -> None:
        try:
            with open(self.filename, 'a+') as fhand:
                fhand.seek(0)
                data = json.load(fhand)
                for purchase in data.get("purchases", []):
                    self.expenses.append(Purchase(purchase["category"], purchase["name"], purchase["amount"], purchase["price"], purchase["date"]))
        except json.JSONDecodeError:
            self.expenses = []
            
    def save(self) -> None:
        with open(self.filename, 'w') as fhand:
            data = {"purchases": [p.to_dict() for p in self.expenses]}
            json.dump(data, fhand, indent=2)
            
    def add_expense(self, category, name: str, amount: float, price: float, date: str) -> bool:
        try:
            self.expenses.append(Purchase(category, name, amount, price, date))
            return True
        except ValueError:
            return False    

    def all_items(self):
        return self.expenses
    
    def filter_items(self, value: int | float | str, key: str) -> Generator[Tuple[Purchase, int], None, None]:
        functions = {
            "name" : lambda p, value: p.name == value,
            "category" : lambda p, value: p.category == value,
            "price" : lambda p, value: p.price == value,
            "amount" : lambda p, value: p.amount == value,
            "date" : lambda p, value: p.date == value
        }
        compr = functions.get(key)
        if not compr:    
            return
        return ((purchase, idx) for idx, purchase in enumerate(self.expenses) if compr(purchase, value))
            
                
    def remove_purchase(self, idx) -> bool:
        try:
            del self.expenses[idx]
        except IndexError:
            return False
        return True
    
    def update(self, key: str, old_val: str, new_val: str ) -> None:
        for p, _ in self.filter_items(old_val, key):
            setattr(p, key, new_val)
        
    def clear(self):
        self.expenses = []
        return True
