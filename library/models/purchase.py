class Purchase:

    def __init__(self, category: str, name: str, amount: int, price: float, date: str):
        self._category = category
        self._name = name

        if amount < 0 and isinstance(amount, int):
            self._amount = amount
        else:
            raise ValueError("Amount must be a positive integer.")

        if price > 0:
            self._price = price
        else:
            raise ValueError("Pric must be greater then 0.")
        
        if self.check_date(date):
            self._date = date
        else:
            raise ValueError("Date is invalid.")
        
    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str) -> bool:
        self._category = value
        return True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> bool:
        self._name = value
        return True

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int) -> bool:
        if amount > 0 and isinstance(value, int):
            self._amount = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> bool:
        if value > 0:
            self._price = value
            return True
        return False
    
    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, value: str) -> bool:
        if self.check_date(value):
            self._date = value
            return True
        return False
    @property
    def total(self) -> float:
        return self._amount * self._price
   
    def check_date(self, date: str) -> bool:
        date_pattern = r"^\d{1,2}-\d{1,2}-\d{4}$"
        if re.match(date_pattern, date):
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
        
  def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "amount": self.amount,
            "price": self.price,
            "date": self.date
        }
