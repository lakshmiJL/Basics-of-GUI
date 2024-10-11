class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"The {self.year} {self.make} {self.model}'s engine has been stopped.")
        else:
            print("The engine is already stopped.")

# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Test the methods
car1.start_engine()
car2.start_engine()
car2.stop_engine()
car1.stop_engine()
