


def calculate_total_problems_cost(cars):
    problems_dict = {
        "engine": 2000,
        "breaks": 1000,
        "5000 km treatment": 500,
        "10000 km treatment": 1000,
        "filters + oil": 250,
        "gear": 1000
    }
    total_cost = 0
    for car in cars:
        for problem in car["list_of_problems"]:
            if problem in problems_dict:
                total_cost += problems_dict[problem]
    return total_cost
