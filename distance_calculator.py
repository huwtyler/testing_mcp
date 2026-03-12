# Python script to calculate distance between two latitude and longitudes.
# lat and lon should be passed in, it will make a distance calculation
# and return the value in meters.

import math
import sys


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on Earth
    using the Haversine formula.

    Args:
        lat1: Latitude of the first point in decimal degrees.
        lon1: Longitude of the first point in decimal degrees.
        lat2: Latitude of the second point in decimal degrees.
        lon2: Longitude of the second point in decimal degrees.

    Returns:
        Distance between the two points in meters.
    """
    EARTH_RADIUS_METERS = 6_371_000

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return EARTH_RADIUS_METERS * c


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python distance_calculator.py <lat1> <lon1> <lat2> <lon2>")
        sys.exit(1)

    lat1, lon1, lat2, lon2 = map(float, sys.argv[1:5])
    distance = calculate_distance(lat1, lon1, lat2, lon2)
    print(f"{distance:.2f}")
