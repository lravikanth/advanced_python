from dataclasses import dataclass


@dataclass
class Vehicle:
    model: str

    def display(self) -> None:
        print("Veheicle Model: ", self.model)


# three sub classes


class Car(Vehicle):
    def display(self) -> None:
        print("Car Model: ", self.model)


class Plane(Vehicle):
    def display(self) -> None:
        print("Plane Model: ", self.model)


class Baot(Vehicle):
    def display(self) -> None:
        print("Boat Model: ", self.model)


# upper bound: one level reistricting. This gives i.diaplay intellisense
class VehicleRegistry[T: Vehicle]:
    reg: list[T] = []

    def add(self, veh: T) -> None:
        self.reg.append(veh)

    def display(self) -> None:
        for i in self.reg:
            i.display()


bmw = Car("BMW X5")
boeing = Plane("Boeing jet")
yemaha = Baot("Ymaha boat")

# upper bound restricting it to car or plane. Cant add boat.
registry = VehicleRegistry[Car | Plane]()
registry.add(bmw)
registry.add(boeing)

# IDE error. But can add a boat and display it.
# registry.add(yemaha)
registry.display()
