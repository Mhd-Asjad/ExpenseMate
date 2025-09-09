import sqlalchemy as db
from sqlalchemy import create_engine 
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

engine = create_engine('sqlite:///expenses.db',echo=False)
metadata = db.MetaData()

console = Console()

categories = db.Table('categories', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String, unique=True, nullable=False)
)

expenses = db.Table('expenses', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('description', db.String),
    db.Column('amount', db.Float, nullable=False),
    db.Column('category_id', db.Integer , db.ForeignKey('categories.id'), nullable=False),
    db.Column('date', db.DateTime, default=datetime.utcnow)
    
)

budgets = db.Table('budgets', metadata,
                   
    db.Column('id' , db.Integer, primary_key=True),
    db.Column('year_month', db.String , unique=True , nullable=False),
    db.Column('amount', db.Float , nullable=False)
    
)

# creating new db instance
def setup_database():
    metadata.create_all(engine)
    
def add_expense(description, amount, category_name):
    with engine.connect() as connection:
        category_query = db.select(categories.c.id).where(categories.c.name == category_name)
        result = connection.execute(category_query).fetchone()

        if result:
            category_id = result[0]
        else:
            insert_cat = db.insert(categories).values(name=category_name)
            result = connection.execute(insert_cat)
            category_id = result.inserted_primary_key[0]
            print(f'Category "{category_name}" added with ID {category_id}.')

        insert_exp = db.insert(expenses).values(
            description=description,
            amount=amount,
            category_id=category_id
        )
        connection.execute(insert_exp)
        connection.commit()
        
# show category wise expenses
def category_expenses( category):
    with engine.connect() as connection:
        category_query = db.select(categories.c.id).where(categories.c.name == category)
        result = connection.execute(category_query).fetchone()
        if result:
            category_id = result[0]
            # get the expenses from the category    
            expense_query = db.select(expenses.c.amount, expenses.c.description).where(
            expenses.c.category_id == category_id
            )
            rows = connection.execute(expense_query).fetchall()
            if rows :
                total_amount = sum( r.amount for r in rows )
                return rows , total_amount
            else:
                return [] , 0.0
        else:
            print(f"Category '{category}' does not exist.")
            return [] , 0.0

def display_category_expenses(rows, total_amount, category):
    table = Table(title=f"Expenses for '{category}'", box=box.ROUNDED, show_lines=True)

    table.add_column("Description", style="cyan", no_wrap=True)
    table.add_column("Amount (₹)", justify="right", style="green")

    for r in rows:
        table.add_row(r.description, f"₹{r.amount:,.2f}")

    table.add_row("[bold yellow]Total[/bold yellow]", f"[bold red]₹{total_amount:,.2f}[/bold red]")

    console.print(table)

# add montly budget or update existing month budget
def set_monthly_salary(year_month , amount):
    with engine.begin() as connection:
        query = db.select(budgets).where(budgets.c.year_month == year_month)
        existing_budget = connection.execute(query).fetchone()
        
        if existing_budget :
            update_budget = db.update(budgets).where(budgets.c.year_month == year_month).values(amount=amount)
            connection.execute(
                update_budget
            )

        else :
            insert_budget = db.insert(budgets).values(year_month=year_month,amount=amount)
            connection.execute(insert_budget)
            
# get monthly budget for the given year-month
def get_monthly_budgets(year_month):
    with engine.connect() as conn:
        query = db.select(budgets.c.amount).where(budgets.c.year_month == year_month)
        result = conn.execute(query).scalar()
        return result if result else 0.00
    
# get total amount expenses are held for given month
def get_total_expenses_for_month(year_month):
    with engine.connect() as conn:
        """ query for calculate all expense on the month """
        query = db.select(db.func.sum(expenses.c.amount)).where(
            db.func.strftime("%Y-%m",expenses.c.date) == year_month
        )
        
        result = conn.execute(query).scalar()
        return result if result else 0.00
