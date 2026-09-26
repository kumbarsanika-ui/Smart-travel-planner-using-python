# Smart Travel Planner

A friendly Python console program for estimating the cost of a trip. It uses
only Python's standard library and stores information in memory; it does not
use a database, files for trip data, web APIs, external packages, or classes.

## Run the Program

```powershell
python smart_travel_planner.py
```

The planner asks for the traveler's name and destination, the number of
travelers and days, transportation cost per traveler, hotel cost per day,
hotel food budget per traveler per day, and activity cost per traveler.
Costs may include cents and cannot be negative. Traveler and day counts must
be whole numbers greater than zero.

Hotel food is entered separately because it is not included in the hotel room
cost. Its total is calculated as the food budget per traveler per day times
the number of travelers times the number of days. Transportation and activity
inputs are per traveler for the whole trip; hotel cost is for the whole group
per day.

## Calculations

- Transportation total = transportation cost per traveler x travelers
- Hotel total = hotel cost per day x days
- Hotel food total = food budget per traveler per day x travelers x days
- Activity total = activity cost per traveler x travelers
- Overall trip cost = transportation + hotel + hotel food + activities
- Cost per traveler = overall trip cost / travelers
- Average daily cost = overall trip cost / days

Each calculation has its own function and returns its result. The collected
traveler details and costs are grouped in dictionaries, then the program
prints a formatted summary with each category and the trip averages.

## Python Concepts Demonstrated

- Variables and data types: strings, integers, and floating-point costs
- Input and type conversion with `input()`, `int()`, and `float()`
- Dictionaries to organize related traveler, cost, and summary information
- Functions with parameters and return values
- Arithmetic operations for trip totals and averages
- Input validation with retry prompts for empty, invalid, and out-of-range values
- Formatted output with f-strings and currency formatting