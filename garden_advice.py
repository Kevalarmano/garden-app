"""
garden_advice.py

This program provides gardening advice based on the month entered by the user.
The logic has been refactored into reusable functions and hardcoded branching
has been replaced with dictionaries for better maintainability.
"""

from typing import Dict


# ----------------------------
# CONSTANTS (no hardcoded if-chains)
# ----------------------------

MONTH_TO_SEASON: Dict[int, str] = {
    12: "summer", 1: "summer", 2: "summer",
    3: "autumn", 4: "autumn", 5: "autumn",
    6: "winter", 7: "winter", 8: "winter",
    9: "spring", 10: "spring", 11: "spring",
}

SEASON_ADVICE: Dict[str, str] = {
    "summer": "Water plants early in the morning and mulch to retain moisture.",
    "autumn": "Plant bulbs and enrich soil with compost.",
    "winter": "Protect sensitive plants from frost and reduce watering.",
    "spring": "Start sowing seeds and fertilise to support new growth."
}


# ----------------------------
# FUNCTIONS
# ----------------------------

def parse_month_input(user_input: str) -> int:
    """
    Convert and validate user input.
    Raises ValueError if the input is not a valid month (1-12).
    """
    month = int(user_input.strip())
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    return month


def get_season(month: int) -> str:
    """
    Return the season for a given month.
    """
    return MONTH_TO_SEASON[month]


def get_advice(season: str) -> str:
    """
    Return gardening advice for the given season.
    """
    return SEASON_ADVICE.get(season, "No advice available.")


def main() -> None:
    """
    Main program logic.
    """
    user_input = input("Enter the month number (1-12): ")

    try:
        month = parse_month_input(user_input)
        season = get_season(month)
        advice = get_advice(season)

        print(f"\nSeason: {season.capitalize()}")
        print(f"Advice: {advice}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
