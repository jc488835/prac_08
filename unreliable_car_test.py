from unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Prius 1", 100, 50)
    car.drive(40)
    print(car)


if __name__ == '__main__':
    main()
