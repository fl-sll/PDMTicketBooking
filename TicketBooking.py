class Booking:
    def __init__(self,destination:str = "",tickets:int = 0):
        self.__destination = destination
        self.__tickets = tickets
        self.__price = 0
        self.__stock = 0
    
    def _PriceList(self):
        if self.__destination == "Cirebon" or self.__destination == "cirebon":
            self.__price = 50000
            self.__stock = 20
        elif self.__destination == "Yogyakarta" or self.__destination == "yogyakarta":
            self.__price = 100000
            self.__stock = 25
        elif self.__destination == "Surabaya" or self.__destination == "surabaya":
            self.__price = 200000
            self.__stock = 30
        else:
            self.__price = 0
            self.__stock = 0
            
    def set_destination(self):
        self.__destination = input("Enter your destination: ")
        
    def set_tickets(self):
        try:
            tickets = int(input("Enter number of tickets to be order: "))
        except:
            print("Please input a number!")
        self.__tickets = tickets
                        
    def get_destination(self):
        return self.__destination
    
    def get_price(self):
        return self.__price
    
    def get_tickets(self):
        return self.__tickets
    
    def get_stock(self):
        return self.__stock - self.get_tickets()
    
    def total_cost(self):
        return self.__tickets * self.__price
    
    def __str__(self):
        print(f"{self.get_tickets()} tickets to {self.get_destination()} at {'{:,.2f}'.format(self.get_price())} per ticket successfully ordered.\
                \nThe total cost for your order = {'{:,.2f}'.format(self.total_cost())}") 

def display_list():
    print("Destinations".ljust(10), "Price".center(15), "Stocks".rjust(8))
    print("---------------------------------------")
    print("Cirebon".ljust(10), "50000".center(19), "20".rjust(4))
    print("Yogyakarta".ljust(10), "100000".center(19), "25".rjust(4))
    print("Surabaya".ljust(10), "200000".center(19), "30".rjust(4))

def main():
    display_list()
    user_order = Booking()
    while True:
        user_order.set_destination()
        user_order._PriceList()
        price = user_order.get_price()
        stocks = user_order.get_stock()
        if price == 0:
            print("Sorry there's no ticket for your destination!")
            print("---------------------------------------------\n")
            print("Enter 'Y' to change your destination")
            print("Enter any other key to cancel")
            print("---------------------------------------------")
            user_choice = input("Would you like to change your destination? ")
            if user_choice.upper() == "Y":
                continue
            else:
                print("Thank you for using our service.")
                break
        else:
            while True:
                user_order.set_tickets()
                tickets = user_order.get_tickets()
                if tickets <= 0:
                    print("Sorry the number of ticket can't be negative!")
                    print("---------------------------------------------\n")
                    print("Enter 'Y' to change the number of tickets")
                    print("Enter any other key to cancel")
                    print("---------------------------------------------")
                    user_choice = input("Would you like to change the number of tickets to be order? ")
                    if user_choice.upper() == "Y":
                        continue
                    else:
                        print("Thank you for using our service")
                        return
                else:
                    if stocks <= 0:
                        print(f"Ticket for your destination is less than {tickets}")
                        print("---------------------------------------------\n")
                        print("Enter '1' to change your destination")
                        print("Enter '2' to change the number of tickets")
                        print("Enter any other key to cancel")
                        print("---------------------------------------------")
                        user_choice = input("Would you like to change the number of tickets to be order? ")
                        if user_choice == 1:
                            break
                        elif user_choice == 2:
                            continue
                        else:
                            print("Thank you for using our service.")
                            return
                    else:
                        stocks -= tickets
                        user_order.__str__()
                        print(f"Stock of tickets to {user_order.get_destination().capitalize()} remaining: {stocks}")
                        print("---------------------------------------------\n")
                        print("Enter 'Y' to order more tickets")
                        print("Enter any other key to cancel")
                        print("---------------------------------------------")
                        user_choice = input("Would you like to order more tickets? ")
                        if user_choice.upper() == "Y":
                            break
                        else:
                            print("Thank you for using our service.")
                            return

main()