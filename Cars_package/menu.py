import json
from Cars_package.actions import list_of_cars, add_car, delete_car, search_car
from Problems_package.problems import calculate_total_problems_cost

file_path = 'cars.json'

def save_cars_to_file(cars, filename):
    with open(filename, 'w') as json_file:
        json.dump(cars, json_file, indent=4)

def load_cars_from_file(filename):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []


def menu(my_cars):
    while True:
        print(f" Currently there are {len(my_cars)} cars . The current profit is: {calculate_total_problems_cost(my_cars)} (sum of all cars treatments)")
        print("1-add")
        print("2-list")
        print("3-search")
        print("4-delete")
        print("5-exit")
        selection = input("your command?")
        if selection == "1":
            add_car(my_cars)
            save_cars_to_file(my_cars, file_path)
        if selection == "2":
            list_of_cars(my_cars)
        if selection == "3":
            search_car(my_cars)
        if selection == "4":
            delete_car(my_cars)
            save_cars_to_file(my_cars, file_path)
        if selection == "5":
            save_cars_to_file(my_cars, file_path)
            print("goodbye")
            break
        else:
            print ("invalid selection..")