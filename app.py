import json

from Cars_package.menu import menu , load_cars_from_file

file_path = 'cars.json'



garage_cars = load_cars_from_file(file_path)

if __name__=="__main__":
    menu(garage_cars)

