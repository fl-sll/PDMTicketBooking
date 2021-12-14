class Booking:
    def __init__(self,destination:str,tickets:int):
        self.__destination = destination
        self.__tickets = tickets
        self.__price = 0
        self.__stock = 0
    
    def _PriceList(self):
        if self.__destination == "Cirebon":
            self.__price = 50000
            self.__stock = 20
        elif self.__destination == "Yogyakarta":
            self.__price = 100000
            self.__stock = 25
        elif self.__destination == "Surabaya":
            self.__price = 200000
            self.__stock = 30
        else:
            self.__price = 0
            self.__stock = 0
    
    def get_destination(self):
        return self.__destination
    
    def get_price(self):
        return self.__price
    
    def get_tickets(self):
        return self.__tickets
    
    def get_stock(self):
        return self.__stock
    
    def total_cost(self):
        return self.__tickets * self.__price
    
    def __str__(self):
        print(f"{self.__tickets} tickets to {self.__destination.capitalize()} at {'{:,.2f}'.format(self.__price)} per ticket. Total Cost = {'{:,.2f}'.format(self.total_cost())}") 

def display_list():
    print("Destinations".ljust(10), "Price".center(10), "Stocks".rjust(10))
    print("Cirebon".ljust(10), "50000".center(15), "20".rjust(10))
    print("Yogyakarta".ljust(10), "100000".center(15), "25".rjust(10))
    print("Surabaya".ljust(10), "200000".center(15), "30".rjust(10))

def main():
    display_list()
    destination = input("Enter your destination: ")
    tickets = int(input("Enter number of tickets: "))
    d = Booking(destination, tickets)
    d._PriceList()
    stocks = d.get_stock()
    run = True
    while run:
        if d.get_price == 0:
            choice = input("Do you want to cancel (Y/N)? ")
            if choice == "Y" or "y":
                run = False
            elif choice == "N" or "n":
                destination = input("Please re-enter your destination: ")
                run = True
        else:
            if stocks <= 0:
                stocks -= tickets
                print("Tickets ordered is more than stock")
                choice = input("Do you want to cancel (Y/N)? ")
                if choice == "Y" or "y":
                    run = False
                elif choice == "N" or "n":
                    tickets = int(input("Please re-enter amount of tickets ordered: "))
                    run = True
            else:
                stocks -= tickets
                d.__str__()
                print(f"Stock of tickets to {d.get_destination().capitalize()} remaining: {stocks}")
                run = False

main()