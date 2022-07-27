from typing import List

"""
When encountering a break-statement in a for-loop, the else case will be
executed at the end of the loop
"""


def print_function(car_states:List[str]):
    for state in car_states:
        if state == 'faulty':
            print("Found faulty car")
            break
        print("Shipping new car!")
    else:
        print("All cars build were ok!")
    print("\n")

if __name__=="__main__":
    cars1 = ['faulty', 'ok', 'ok']
    cars2 = ['ok', 'ok', 'ok']

    print_function(cars1)
    print_function(cars2)