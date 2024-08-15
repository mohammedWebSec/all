import sys
from fractions import Fraction

def solve_equation(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_to_least_fraction(decimal):
    fraction = Fraction(decimal).limit_denominator()
    return f"{fraction.numerator}/{fraction.denominator}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py expression")
        sys.exit(1)

    expression = sys.argv[1]
    result = solve_equation(expression)
    if result is not None:
        fraction = convert_to_least_fraction(result)
        
        print(f"{fraction}")

