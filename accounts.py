class Accounts():
    def __init__(self,account_id,account_holder,blance=0):
        self.account_id =account_id
        self.account_holder= account_holder
        self.blance = blance

    def deposit(self,amount):
        amount+= self.blance
        return f"{amount} sucessfuly deposit!"
    def with_drawal(self,amount):
        if amount >0 and amount <= self.blance:
            self.blance-=amount
            return f"{amount } is successfully with drawed"
        elif amount<=0:
            return f"invalid with drawal please enter positive nom"
        else:
            return f"sorry insufficient blance"

    def check_balance(self):
        return self.blance
class Saving_account(Accounts):
    def __init__(self,account_id,account_holder,blance=0,interest_rate=0.02):
        super().__init__(account_id,account_holder,blance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        interest = self.interest_rate*self.blance
        self.blance+= interest

class Bank():
    def __init__(self):
        self.account= []

    def create_account(self,account_id,account_holder,account_type='saving'):
        if account_type=='saving':
            account=Saving_account(account_id,account_holder)
        else:
            account =Accounts(account_id,account_holder)
        self.account.append(account)
        return account
    def get_account(self,account_id):
        for accounts in self.account:
            if accounts.account_id == account_id: # Compare account_id with account.account_id
                return accounts
        return None

