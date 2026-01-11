class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and an optional description.
        If no description is given, it should default to an empty string.
        The method should append an object to the ledger list in the form of
        {'amount': amount, 'description': description}.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        A withdraw method that accepts an amount and an optional description.
        If the withdrawal is successful, it should store the amount as a negative number.
        Returns True if the withdrawal succeeded, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        A get_balance method that returns the current category balance.
        """
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        """
        A transfer method that accepts an amount and another Category instance.
        It withdraws from the current category and deposits into the other.
        Returns True if the transfer is successful, False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        A check_funds method that accepts an amount and returns False if it
        exceeds the balance or True otherwise.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        String representation of the Category object.
        """
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']

        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    """
    Creates a bar chart showing percentage spent in each category.
    """
    chart = "Percentage spent by category\n"
    
    # Calculate total spent per category
    spent_per_category = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        spent_per_category.append(spent)
        
    total_spent = sum(spent_per_category)
    
    # Calculate percentages
    percentages = []
    for spent in spent_per_category:
        percentage = (spent / total_spent) * 100
        percentages.append(int(percentage // 10) * 10)

    # Build the chart
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add category names vertically
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len -1:
            chart += "\n"

    return chart
