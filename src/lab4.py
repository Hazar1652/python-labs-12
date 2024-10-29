class Car:

    def __init__(self, engine_power=None, brand=None, max_speed=None, price=0, owner_name="Unknown"):
        self.__engine_power = engine_power
        self._brand = brand
        self.__max_speed = max_speed
        self.price = price
        self.owner_name = owner_name

    def get_engine_power(self):
        return self.__engine_power

    def get_brand(self):
        return self._brand

    def get_max_speed(self):
        return self.__max_speed

    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power

    def set_brand(self, brand):
        self._brand = brand

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def __str__(self):
        return f"Car: {self._brand}, Power: {self.__engine_power} HP, Max Speed: {self.__max_speed} km/h, Price: {self.price}, Owner: {self.owner_name}"

    # def __str__(self):
    #     return f"Max Speed:{self.__max_speed} km/h "

    def __repr__(self):
        return f"Car({self.__engine_power}, '{self._brand}', {self.__max_speed}, {self.price}, '{self.owner_name}')"

    def __del__(self):
        print(f"Car object {self._brand} destroyed.")

def main():
    car1 = Car(300, "BMW", 290, 50000, "Nazar")
    car2 = Car(350, "Ferrari", 320, 150000, "Vlad")
    car3 = Car()



    print(car1)
    print(car2)
    print(car3)

    print(f"Brand: {car1.get_brand()}, Engine Power: {car1.get_engine_power()} HP, Max Speed: {car1.get_max_speed()} km/h, Price: {car1.price}, Owner: {car1.owner_name}")
    print(f"Brand: {car2.get_brand()}, Engine Power: {car2.get_engine_power()} HP, Max Speed: {car2.get_max_speed()} km/h, Price: {car2.price}, Owner: {car2.owner_name}")
    print(f"Brand: {car3.get_brand()}, Engine Power: {car3.get_engine_power()} HP, Max Speed: {car3.get_max_speed()} km/h, Price: {car3.price}, Owner: {car3.owner_name}")
    print(f"Max speed of {car1.get_brand()}: {car1.get_max_speed()} km/h")
    print(f"Max speed of {car2.get_brand()}: {car2.get_max_speed()} km/h")

main()








