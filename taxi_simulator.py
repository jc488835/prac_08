from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            current_taxi.start_fare()
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost))
            bill += cost

        print("Bill to date: ${:.2f}".format(bill))
        print(menu)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()
