import array


def display_parking_layout(parking_array: array) -> array:
    for level in parking_array:
        print(level)


def if_vehicle_in_parking(parking_array: array, vehicle_num: str) -> bool:
    for level in parking_array:
        if vehicle_num in level:
            return True
    return False


def main():
    print("Welcome to Parking")
    parking_level = {0: 'A', 1: 'B'}
    num_levels = 2
    num_slots_per_level = 20

    parking_array = []
    for i in range(num_levels):
        level = [0] * num_slots_per_level
        parking_array.append(level)

    while True:
        option = int(input(
            "Please choose an operation: \n"
            "1. Park a vehicle\n"
            "2. Unpark a vehicle\n"
            "3. Get information about a vehicle\n"
            "4. Display parking layout\n"
            "5. Exit\n"
            "Enter the corresponding number: "
        ))

        if option == 5:
            exit()

        elif option == 4:
            display_parking_layout(parking_array)

        elif option == 1:
            vehicle_num = str(input("Enter the vehicle number:"))

            vehicle_in_parking = if_vehicle_in_parking(parking_array, vehicle_num)

            if vehicle_in_parking:
                print("Vehicle exits in parking.")
                continue

            for level in range(0, num_levels):
                for slot in range(0, num_slots_per_level):
                    if parking_array[level][slot] == 0:
                        parking_array[level][slot] = vehicle_num
                        break
                break

        elif option == 2:
            vehicle_num = str(input("Enter the vehicle number:"))

            vehicle_in_parking = if_vehicle_in_parking(parking_array, vehicle_num)

            if not vehicle_in_parking:
                print("Vehicle does not exits in parking.")
                continue

            for level in range(0, num_levels):
                for slot in range(0, num_slots_per_level):
                    if parking_array[level][slot] == vehicle_num:
                        parking_array[level][slot] = 0
                        if level == 0:
                            print(f"Vehicle un-parked from level: {parking_level[level]} and spot {slot+1}")
                        if level == 1:
                            print(f"Vehicle un-parked from level: {parking_level[level]} and spot {slot+20+1}")

        elif option == 3:
            vehicle_num = str(input("Enter the vehicle number:"))

            vehicle_in_parking = if_vehicle_in_parking(parking_array, vehicle_num)

            if not vehicle_in_parking:
                print("Vehicle does not exits in parking.")
                continue

            for level in range(0, num_levels):
                for slot in range(0, num_slots_per_level):
                    if parking_array[level][slot] == vehicle_num:
                        if level == 0:
                            print({'level': parking_level[level], 'spot': slot+1})
                            break
                        elif level == 1:
                            print({'level': parking_level[level], 'spot': slot+20+1})
                            break

        else:
            print("Operation does not exist.")


if __name__ == '__main__':
    main()
