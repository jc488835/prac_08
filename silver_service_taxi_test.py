from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Prius 1", 100, 2)
    taxi.drive(18)
    print(taxi)


if __name__ == '__main__':
    main()
