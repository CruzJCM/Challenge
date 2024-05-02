class Call:
    def __init__(self, type, duration, day, hour, country, city):
        self.type = type
        self.duration = duration
        self.cost = 0
        self.day = day
        self.hour = hour
        self.country = country
        self.city = city

    def calculate_cost(self):
        if self.type == "Local":
            self.cost = self.calculate_cost_local_call()
        elif self.type == "National":
            self.cost = self.calculate_cost_national_call()
        elif self.type == "International":
            self.cost = self.calculate_cost_international_call()
        return self.cost

    def calculate_cost_local_call(self):
        if self.day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] and 8 <= self.hour < 20:
            return self.duration * 0.20
        else:
            return self.duration * 0.10

    def calculate_cost_national_call(self):
        if self.city in ["San Fernando del Valle de Catamarca", "Resistencia", "Rawson", "Cordoba", "Corrientes", "Parana", "Formosa", "San Salvador de Jujuy", "Santa Rosa", "La Rioja", "Mendoza", "Posadas", "Neuquen", "Viedma", "Salta", "San Juan", "San Luis", "Rio Gallegos", "Santa Fe", "Santiago del Estero", "Ushuaia", "San Miguel de Tucuman"]:
            return self.duration * 0.30
        else:
            return self.duration * 0.40

    def calculate_cost_international_call(self):
        if self.country in ["Chile", "Uruguay", "Paraguay", "Bolivia"]:
            return self.duration * 0.50
        else:
            return self.duration * 0.90

class Invoice:
    def __init__(self, basic_charge, month):
        self.month = month
        self.basic_charge = basic_charge
        self.calls = []

    def add_call(self, call):
        self.calls.append(call)

    def calculate_total(self):
        total = self.basic_charge
        for call in self.calls:
            total += call.calculate_cost()
        return total

    def print_invoice(self):
        print("-----------------------------------------------------")
        print("Invoice details:")
        print("Month: ", self.month)
        print("Basic charge: $", self.basic_charge)
        print("Calls made:")
        for call in self.calls:
            print("#. Type:", call.type, ", Duration:", call.duration, "min, Cost: $", call.calculate_cost())
        print("Total to pay: $", self.calculate_total())
        print("-----------------------------------------------------")

# Create a new Invoice object
invoice = Invoice(basic_charge=50.0, month='May')

# Create some Call objects
call1 = Call(type='Local', duration=10, day='Monday', hour=15, country='Argentina', city='Buenos Aires')
call2 = Call(type='National', duration=5, day='Thursday', hour=10, country='Argentina', city='Cordoba')
call3 = Call(type='International', duration=3, day='Saturday', hour=20, country='Chile', city='Santiago')

# Add the Call objects to the Invoice object
invoice.add_call(call1)
invoice.add_call(call2)
invoice.add_call(call3)

# Call the print_invoice method
invoice.print_invoice()


"""
output:

-----------------------------------------------------
Invoice details:
Month:  May
Basic charge: $ 50.0
Calls made:
#. Type: Local , Duration: 10 min, Cost: $ 2.0
#. Type: National , Duration: 5 min, Cost: $ 1.5
#. Type: International , Duration: 3 min, Cost: $ 1.5
Total to pay: $ 55.0
-----------------------------------------------------
"""