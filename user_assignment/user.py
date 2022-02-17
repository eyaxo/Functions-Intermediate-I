class User:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def make_deposit(self,amount):
        self.account_balance += amount

    def display_user_balance(self):
        return(self["name"].account_balance)

vi= User("Vi","Avila")
luna= User("Luna","Avila")
lon= User("Lon","Avila")

vi.make_deposit(250)
vi.make_deposit(140)
vi.make_deposit(3)
vi.make_withdrawal(43)

luna.make_deposit(10)
luna.make_deposit(420)
luna.make_withdrawal(5)
luna.make_withdrawal(30)

lon.make_deposit(50000)
lon.make_withdrawal(10)
lon.make_withdrawal(3)
lon.make_withdrawal(1)

print(vi.account_balance)
print(luna.account_balance)
print(lon.account_balance)