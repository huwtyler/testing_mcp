# Task 17: Give something a go
# Requirements: Create a file which has a simple mathematical equation
# to calculate the circumference of a circle

import math


def calculate_circumference(radius):
    """Calculate the circumference of a circle given its radius.
    
    Formula: C = 2 * π * r
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The circumference of the circle
    """
    return 2 * math.pi * radius


if __name__ == "__main__":
    # Example usage
    r = 5
    circumference = calculate_circumference(r)
    print(f"A circle with radius {r} has circumference {circumference:.2f}")
