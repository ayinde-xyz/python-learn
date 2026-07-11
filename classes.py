class Vehicle: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 

    def start_engine(self): 
        return f"The {self.year} {self.make} {self.model}'s engine has started." 

    def stop_engine(self): 
        return f"The {self.year} {self.make} {self.model}'s engine has stopped." 

    def honk(self): 
        return "Beep beep!"

class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


    def honk(self):
        print("rumbles along....")



class GolfCart(Vehicle):
    pass
    

mack = Truck("mack", "GC1000", "2004")
golfWagon = GolfCart("TRump", "president", "2023")

myCar = Vehicle("Tesla", "model y", 2003)


print(mack.stop_engine())
print(mack.honk())
print(golfWagon.start_engine())
print(golfWagon.honk())

print(myCar.start_engine())

print("\n\n")

for v in (myCar, mack, golfWagon):
    print(v.start_engine())
    print(v.stop_engine())