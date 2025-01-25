class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def calculation_bills(self, total_bill, total_days):
        return
        
class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class FlatematesBillSplitter:
    def __init__(self):
        self.faltemates = []
        
    def add_flatemate(self, name, days_in_house):
        flate_mate = Flatmate(name, days_in_house)
        self.faltemates.append(flate_mate)
        # print(self.faltemates)
        
    def show_flatemates(self):
        print("\nList of Flatmates:")
        for flatemate in self.faltemates:
            print(f"Name: {flatemate.name}, Days Stayed: {flatemate.days_in_house}")


# Here is the main function
if __name__ == "__main__":
    splitter = FlatematesBillSplitter()
    
    print("Enter details for flatmates:")
    n = int(input("How many flatmates? "))
    
    for i in range(n):
        name = input(f"Name of the flatemate: ")
        while True:
            try:
                days = int(input(f"Days {name} stayed (must be <= 31): "))
                if 1 <= days <= 31:
                    break
                else:
                    print("Error: Days must be between 1 and 31.")
            except ValueError:
                print("Error: Please enter a valid number.") 
                       
        splitter.add_flatemate(name, days)
    
    splitter.show_flatemates()