"""A friendly, built-in-only travel budget planner for the console."""

import math


def get_non_empty_text(prompt):
    """Return text that contains at least one non-space character."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter something so we can add it to your trip plan.")


def get_positive_integer(prompt):
    """Return an integer greater than zero, retrying invalid input."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number, such as 1 or 4.")
            continue
        if value > 0:
            return value
        print("That number must be greater than zero.")


def get_non_negative_cost(prompt):
    """Return a finite cost that is zero or greater."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid amount, such as 25 or 19.50.")
            continue
        if math.isfinite(value) and value >= 0:
            return value
        print("Cost must be a finite number that is not negative.")


def calculate_transportation_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_hotel_cost(cost_per_day, travel_days):
    return cost_per_day * travel_days


def calculate_hotel_food_cost(food_per_traveler_per_day, traveler_count, travel_days):
    return food_per_traveler_per_day * traveler_count * travel_days


def calculate_activity_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_overall_cost(transportation, hotel, food, activities):
    return transportation + hotel + food + activities


def calculate_cost_per_traveler(overall_cost, traveler_count):
    return overall_cost / traveler_count


def calculate_average_daily_cost(overall_cost, travel_days):
    return overall_cost / travel_days


def collect_trip_information():
    """Collect trip details and organize related values in dictionaries."""
    print("=" * 54)
    print("             SMART TRAVEL PLANNER")
    print("       Let's make your next trip easier to plan!")
    print("=" * 54)
    print("Enter your trip details below. Costs can include cents.\n")

    traveler = {
        "name": get_non_empty_text("Traveler name: "),
        "destination": get_non_empty_text("Destination: "),
        "count": get_positive_integer("Number of travelers: "),
        "days": get_positive_integer("Number of travel days: "),
    }
    costs = {
        "transportation_per_traveler": get_non_negative_cost(
            "Transportation cost per traveler for the trip: "
        ),
        "hotel_per_day": get_non_negative_cost("Hotel cost per day: "),
        "food_per_traveler_per_day": get_non_negative_cost(
            "Hotel food budget per traveler, per day: "
        ),
        "activities_per_traveler": get_non_negative_cost(
            "Activity cost per traveler for the trip: "
        ),
    }
    return traveler, costs


def build_trip_summary(traveler, costs):
    """Calculate and return the trip details and all budget totals."""
    totals = {
        "transportation": calculate_transportation_cost(
            costs["transportation_per_traveler"], traveler["count"]
        ),
        "hotel": calculate_hotel_cost(costs["hotel_per_day"], traveler["days"]),
        "food": calculate_hotel_food_cost(
            costs["food_per_traveler_per_day"], traveler["count"], traveler["days"]
        ),
        "activities": calculate_activity_cost(
            costs["activities_per_traveler"], traveler["count"]
        ),
    }
    totals["overall"] = calculate_overall_cost(
        totals["transportation"], totals["hotel"], totals["food"], totals["activities"]
    )
    totals["per_traveler"] = calculate_cost_per_traveler(
        totals["overall"], traveler["count"]
    )
    totals["per_day"] = calculate_average_daily_cost(totals["overall"], traveler["days"])
    return {"traveler": traveler, "totals": totals}


def display_trip_summary(summary):
    """Print a tidy, friendly summary of the planned trip."""
    traveler = summary["traveler"]
    totals = summary["totals"]
    print("\n" + "=" * 54)
    print("                  YOUR TRIP SUMMARY")
    print("=" * 54)
    print(f"Traveler        : {traveler['name']}")
    print(f"Destination     : {traveler['destination']}")
    print(f"Travelers       : {traveler['count']}")
    print(f"Travel days     : {traveler['days']}")
    print("-" * 54)
    print(f"Transportation  : ${totals['transportation']:,.2f}")
    print(f"Hotel stay      : ${totals['hotel']:,.2f}")
    print(f"Hotel food      : ${totals['food']:,.2f}")
    print(f"Activities      : ${totals['activities']:,.2f}")
    print("-" * 54)
    print(f"TOTAL TRIP COST : ${totals['overall']:,.2f}")
    print(f"Cost per traveler: ${totals['per_traveler']:,.2f}")
    print(f"Average per day : ${totals['per_day']:,.2f}")
    print("=" * 54)
    print("Have a wonderful trip!")


def main():
    traveler, costs = collect_trip_information()
    summary = build_trip_summary(traveler, costs)
    display_trip_summary(summary)


if __name__ == "__main__":
    main()