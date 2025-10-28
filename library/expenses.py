import csv
import re
import Number

class Expenses:
    def __init__(self, filename = "../data/expenses.csv"):
        self.valid_date = r"^\d{1,2}-\d{1,2}-\d{4}$"
        self.expenses = {}
        self.filename = filename
        self.load()

    def load(self) -> None:
        with open(self.filename, 'a+', newline="") as fhand:
            fhand.seek(0)
            reader = csv.reader(fhand)
            for category, name, amount, date in reader:
                category, name, amount, date = category.strip(), name.strip(), amount.strip(), date.strip()
                if category in self.expenses:
                    self.expenses[category][name] = {"amount" : float(amount), "date" : date}
                else:
                    self.expenses[category] = {name : {"amount" : float(amount), "date" : date}}

    def save(self) -> None:
        with open(self.filename, 'w') as fhand:
            writer = csv.writer(fhand)
            for category, items in self.expenses.items():
                for name, details in items.items():
                    writer.writerow([category, name, details["amount"], details["date"]])

    def add_expense(self, category, name: str, amount: float, date: str) -> bool:
        if not self.checkDate(date) or amount < 0.0:
            return False
        if category in self.expenses:
            if not name in self.expenses[category]:
                self.expenses[category][name] = {"amount" : amount, "date" : date}
                return True
            else:
                return False
        else:
                self.expenses[category] = {name : {"amount" : amount, "date" : date}}
                return True
            
    def add_category(self, category: str) -> bool:
       if category in self.expenses:
           return False
       self.expenses[category] = {}
       return True
   
    def update_item(self, category, name: str, field: str, value: str | float ) -> bool:
        if category in self.expenses and name in self.expenses[category]:
            if field in ["amount", "date"]:
                if field == "amount" and not isinstance(value, numbers.Number):
                    return False
                if field == "date":
                   if not self.checkDate(value):
                       return False
                self.expenses[category][name][field] = value
                return True
        return False    

    def checkDate(self, date: str) -> bool:
        if re.match(self.valid_date, date):
            day, month, year = map(int, date.split('-'))
            min_year = 1970
            if year < min_year:
                return False
            feb_max_days = lambda year: 29 if ((year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)) else 28  
            month_days = {
                1: 31,  # January
                2: feb_max_days(year), # February
                3: 31,  # March
                4: 30,  # April
                5: 31,  # May
                6: 30,  # June
                7: 31,  # July
                8: 31,  # August
                9: 30,  # September
                10: 31, # October
                11: 30, # November
                12: 31  # December
                       }
            if not month in month_days:
                return False
            if not 0 < day <= month_days[month]:
                return False
            return True
        else:
            return False
        
    def change_name(self, category: str,old_name: str, new_name: str) -> bool:
        try:
            self.expenses[category][new_name] = self.expenses[category][old_name]
            del self.expenses[category][old_name]
            return True
        except KeyError:
            return False

    def change_category(self, old_category: str, new_category: str) -> bool:
        try: 
            self.expenses[new_category] = self.expanses[old_category]
            del self.expenses[old_category]
            return True
        except KeyError:
            return False

    def remove_item(self, category: str, name: str) -> bool:
        try:
            del self.expenses[category][name]
            return True
        except KeyError:
            return False

    def remove_category(self, category: str) -> bool:
        try:
            del self.expenses[category]
            return True
        except KeyError:
            return False

    def clear(self):
        self.expenses = {}
        return True
    
    def search(self, name):
        pass
    
    def fillter(self):
        pass
     
