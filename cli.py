import click
from datetime import datetime
from database import setup_database
from repositories import  add_expense , category_expenses , set_monthly_salary , get_monthly_budgets , get_total_expenses_for_month , display_category_expenses
import calendar
from rich.console import Console
from rich.table import Table
from rich import box


console = Console()

@click.group()
def cli():
    pass

@cli.command("init-db")
def init_db():
    """Initialize the database."""
    setup_database()
    click.echo('Database initialized successfully.')

@cli.command("add-expense")
@click.argument('amount', type=float)
@click.argument('description', type=str)
@click.option('-c', '--category',type=click.Choice(['Food','Rent','Travel' , 'Misc']), default='Misc', help='Category of the expense.')
def add(amount, description, category):
    """Add a new expense."""
    add_expense(description, amount, category)
    click.echo(f'Expense "{description}" of amount {amount} added under category "{category}".')
    
@cli.command('show-category')
@click.argument('category',type=str)
def show_category(category):
    """to show the category vise expenses"""
    rows , total_amount = category_expenses(category)
    if not rows:
        console.print(f"[red]No expenses found for category '{category}' [/red]")
    else:
        display_category_expenses(rows, total_amount, category)        

@cli.command('add-budget')
@click.option('--month', default=datetime.now().strftime('%Y-%m'), help="The month in YYYY-MM format.")
@click.option('--amount', type=float , required=True, help="the budget amount for the month")
def add_budget(month , amount):
    """ add budget for particular month """
    if amount < 0 :
        console.print("[red]Budget amount cannot be negative. [/red]")
        return
        
    set_monthly_salary(month , amount)
    click.echo(f"✅ Budget for {month} has been set to ₹{amount:,.2f}.")

@cli.command('show-expense')
@click.option('--month',default=datetime.now().strftime('%Y-%m'), help="The month in YYYY-MM format.")
def show_expenses(month):
    """ show monthly expenses and personal budget tracker for the given month """
    total_budget = get_monthly_budgets(month)
    if total_budget == 0.00:
        click.echo(f"No budget set for {month}. Please set one using 'budget set --amount <value>'.")
        return

    amount_spent = get_total_expenses_for_month(month)
    remaining_budget = total_budget - amount_spent
    
    now = datetime.now()
    year , month_num = map(int , month.split('-'))
    days_in_month = calendar.monthrange(year, month_num)[1]

    if month == now.strftime('%Y-%m'):
        remaining_days = days_in_month - now.day + 1
    else :
        remaining_days = days_in_month
    
    daily_spend_allowance = remaining_budget // remaining_days if remaining_days > 0 else remaining_budget
    updated_dayily_spend = daily_spend_allowance if daily_spend_allowance > 0 else None
    
    table = Table(title=f"Budget Status for {month}", box=box.SIMPLE_HEAVY)

    table.add_column("Description", style="cyan", no_wrap=True)
    table.add_column("Amount (₹)", justify="right", style="green")
    
    table.add_row("Total Budget", f"₹{total_budget:,.2f}")
    table.add_row("Amount Spent 💵", f"₹{amount_spent:,.2f}")
    table.add_row("Remaining Budget", f"₹{remaining_budget:,.2f}" , style=f"{"green" if round(remaining_budget) > 0 else "red"}")
    
    if updated_dayily_spend and isinstance(round(updated_dayily_spend) , int):
        
        table.add_row("Remaining Days", str(remaining_days))
        table.add_row("Daily Spend Allowance", f"₹{daily_spend_allowance:,.2f}")
    
    console.print(table)
    
    if not updated_dayily_spend :
        console.print("[bold red]♨️ Your budget for the month has been exeeded![/bold red]")
    else :
        console.print(f"you can spend about [bold green]₹{daily_spend_allowance:,.2f}[/bold green] per day for the rest of the month.")
    
if __name__ == '__main__':
    cli()