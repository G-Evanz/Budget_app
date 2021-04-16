class budget():

    database = {}

    def __init__ (self, name, food, clothing, entertainment):
    
        self.name = name
        self.ledger = list()
        self.funds = 0
        
    def __str__(self):
        ledger_list = ""
        for list_item in self.ledger:
            amnt = list_item.get("amount")
            descrpt = list_item.get("description")

    def deposit(self):
        """Deposit Funds"""
        self.ledger.append("amount", "description")
        self.funds += amnt
        
    def withdraw(self):
        """Withdraw Funds"""
        if self.funds(amount):
            anount *= -1
            self.ledger.append({"amount": amount, "description": description})
            self.funds += amount
            return True
        else:
            return False
        
    def get_balance(self):
        """"Get Current Balance"""
        return self.funds

    def transfer(self, amount, budget_category):
        """Transfer Funds between Categories."""
        if self.funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount, "description": f"Transfer to {budget_category.name}"})
            budget_category.ledger.append({"amount": amount * -1, "description": f"Transfer from {self.name}"})
            self.funds += amount
            budget_category.funds -= amount
            return True
        else:
            return False