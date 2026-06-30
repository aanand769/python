class Atm :
    
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self) :
        user_input = input("""
1.create Pin
2.check balance
3.change pin
4.Withdraw balance
""")
        
        if user_input == '1' :
            self.create_pin()
        elif user_input == '2' :
            self.check_balance()
        elif user_input == '3' :
            self.change_pin()
        elif user_input == '4' :
            self.withdraw_bal()
        else:
            print('Please give valid input :)')
            
    def create_pin(self):
        user_pin = input('Please enter pin: ')
        self.pin = user_pin
        
        user_balance = int(input('please enter balance amount: '))
        self.balance = user_balance
        
        print('Pin created successfully :)')
        
        self.menu()
        
    def check_balance(self):
        check_pin = input('Please enter your pin: ')
        if check_pin == self.pin : 
            print(f'Your account balance is: {self.balance}')
        else:
            print('Wrong Pin :(')
            
        self.menu()
    
    def change_pin(self):
        check_pin = input('Please enter you existing PIN')
        if check_pin == self.pin :
            new_pin = input('Please enter your new pin')
            self.pin = new_pin
            print('PIN changed Successfully :)')
        else:
            print('Wrong PIN :(')
            
        self.menu()
        
    def withdraw_bal(self):
        check_pin = input('Please enter your pin: ')
        if check_pin == self.pin :
            withdraw_amt = int(input('Enter Amount: '))
            if withdraw_amt <= self.balance :
                self.balance = self.balance - withdraw_amt
                print(f'Withdrawal done, current balance: {self.balance}')
            else: 
                print('Insuficient balance :(')
        else:
            print('Wrong PIN :(')
            
        self.menu()
        

#creating Object
obj1 = Atm()
        

    
    


    