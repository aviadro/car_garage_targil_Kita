from Problems_package.problem_menu import print_problems


def list_of_cars(cars):
    for car in cars:
        print(f"car number is: {car["car_number"]}.  the problems are: {car["list_of_problems"]}")

def add_car(cars):
    c_num = input("please enter the car number: ")
    for car in cars:
        if c_num == car["car_number"]:
            print("the car is already in the garage..")
            return
    print_problems()

    problems_dict = {
        "engine": 2000,
        "breaks": 1000,
        "5000 km treatment": 500,
        "10000 km treatment": 1000,
        "filters + oil": 250,
        "gear": 1000,
    }

    problems_entered = set()
    price = 0

    while True:
        problems = input("please enter your problems: to finish enter -1 ").lower()
        if problems == "-1":
            break
        elif problems in problems_dict:
            if problems in problems_entered:
                print("already entered this problem..")
            else:
                price += problems_dict[problems]
                problems_entered.add(problems)
        else:
            print("Invalid command input")

    while True:
        answer = input(
            f"The price of this fix is: {price} NIS. do you wish to proceed? yes/no "
        ).lower()
        if answer == "no":
            print("good bye")
            break
        elif answer == "yes":
            new_car = {"car_number": c_num, "list_of_problems": list(problems_entered)}
            cars.append(new_car)
            print("Car added successfully.")
            break
        else:
            print("Invalid input")


def delete_car(cars):
    car_number = input("enter the car number to delete.. ")
    for car in cars:
        if car["car_number"] == car_number:
            cars.remove(car)
            print(f"Car with number {car_number} has been removed.")
            return
    print(f"Car with number {car_number} not found.")



def search_car(cars):
    car_number = input("enter the car number to search.. ")
    for car in cars:
        if car["car_number"] == car_number:
            print(f"car number is: {car["car_number"]}.  the problems are: {car["list_of_problems"]}")
            return
    print(f"Car with number {car_number} not found.")
