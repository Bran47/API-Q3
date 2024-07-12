class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, num_seats):
        super().__init__(registration_number, make, model)
        self.num_seats = num_seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f"Car: Registration Number = {vehicle.registration_number}, Make = {vehicle.make}, Model = {vehicle.model}, Seats = {vehicle.num_seats}")
            elif isinstance(vehicle, Truck):
                print(f"Truck: Registration Number = {vehicle.registration_number}, Make = {vehicle.make}, Model = {vehicle.model}, Cargo Capacity = {vehicle.cargo_capacity}")
            elif isinstance(vehicle, Motorcycle):
                print(f"Motorcycle: Registration Number = {vehicle.registration_number}, Make = {vehicle.make}, Model = {vehicle.model}, Engine Capacity = {vehicle.engine_capacity}")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None

# Example usage:
if __name__ == "__main__":
    # Create some vehicles
    car1 = Car("KBZ924V", "PORSCHE", "911", 5)
    truck1 = Truck("KBS546U", "MERCEDES", "S750", 2500)
    motorcycle1 = Motorcycle("KCD567T", "SUZUKI", "K360", 1000)

    # Create a fleet and add vehicles
    fleet = Fleet()
    fleet.add_vehicle(car1)
    fleet.add_vehicle(truck1)
    fleet.add_vehicle(motorcycle1)

    # Display all vehicles in the fleet
    fleet.display_all_vehicles()

    # Search for a vehicle by registration number
    search_result = fleet.search_vehicle("KBS546U")
    search_result = fleet.search_vehicle("KBZ924V")
    if search_result:
        print(f"Vehicle found: Registration Number = {search_result.registration_number}, Make = {search_result.make}, Model = {search_result.model}")
    else:
        print("Vehicle not found.")
