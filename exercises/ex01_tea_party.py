"""EX01 - Tea Party"""

__author__ = "730465719"


import math


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print(f"A Cozy Tea Party for {guests} People!")
    tea_bag_count = tea_bags(guests)
    treat_count = treats(guests)
    print(f"Tea Bags: {tea_bag_count}")
    print(f"Treats: {treat_count}")
    cost_total = cost(tea_bag_count, treat_count)
    print(f"Cost: ${cost_total}")
    

def tea_bags(people: int) -> int:
    """Returns number of tea bags needed based on number of people attending"""
    return 2 * people


def treats(people: int) -> int:
    """Computes number of treats needed based on the number of teas guests are expecting to drink"""
    return math.ceil(1.5 * tea_bags(people))


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea bags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))