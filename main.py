from textual.app import App, ComposeResult
from textual.widgets import DataTable
from textual.containers import Horizontal

from pathlib import Path
from library.models.expenses import Expenses

    
class ExpenseApp(App):

    CSS_PATH = Path("style") / "style.tcss"
    BINDINGS = [
        ('d', "toggle_dark", "Dark mode"),
        ("a", "add_expenses", "Add a expense to the list")
    ]

    
    def compose(self) -> ComposeResult:
        table = DataTable()
        table.add_columns("Category", "Name", "Amount", "Price", "Date")
        for p in expenses.all_items():
            table.add_row(p.category, p.name, p.amount, p.price, p.date)
        table.add_class("expenses")    
        yield table
        
if __name__ == "__main__":
    app = ExpenseApp()
    expenses = Expenses()
    app.run()
