import matplotlib.pyplot as plt

def generate_budget_tracker_chart(total_budget, amount_spent):
    """Generates a horizontal bar chart to visualize budget spending."""
    
    # Data
    labels = ['Budget Status']
    spent = [amount_spent]
    total = [total_budget]
    remaining = total_budget - amount_spent
    
    fig, ax = plt.subplots(figsize=(10, 2))

    # Plot the total budget bar (background)
    ax.barh(labels, total, color='lightgray', label=f'Total Budget: ₹{total_budget:,.2f}')

    # Plot the spent amount bar (foreground)
    # Color changes if you're over budget
    bar_color = 'green' if amount_spent <= total_budget else 'red'
    ax.barh(labels, spent, color=bar_color, label=f'Spent: ₹{amount_spent:,.2f}')

    # Add text to show remaining amount
    ax.text(total_budget, 0, f' Left: ₹{remaining:,.2f} ', va='center', ha='right', color='white',
            bbox=dict(boxstyle='round,pad=0.3', fc='blue', ec='none'))

    # Formatting
    ax.set_yticks([]) # Hide y-axis labels
    ax.set_xlim(0, total_budget * 1.1) # Set x-axis limit slightly larger than budget
    ax.set_title('Monthly Budget Progress')
    ax.legend(loc='lower right')
    
    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('monthly_budget.png')
