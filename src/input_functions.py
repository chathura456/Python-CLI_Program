from constants import WEIGHT_CATEGORIES


def get_athlete_name():
    while True:
        name = input("Enter the athlete's name: ").strip()  # Remove any leading or trailing whitespace
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
        elif not all(char.isalpha() or char.isspace() for char in name):
            print("Name should only contain alphabets and spaces. Please enter a valid name.")
        else:
            return name


def get_training_plan():
    while True:
        print("\nTraining Plans:")
        print("- Beginner (2 Sessions per week) – Weekly fee: £25.00")
        print("- Intermediate (3 Sessions per week) – Weekly fee: £30.00")
        print("- Elite (5 Sessions per week) – Weekly fee: £35.00")
        plan = input("Enter the training plan (Beginner, Intermediate, Elite): ").lower()
        if plan in ["beginner", "intermediate", "elite"]:
            return plan.capitalize()  # Return the capitalized version for consistency
        else:
            print("Invalid choice. Please select from Beginner, Intermediate, or Elite.")


def get_current_weight():
    while True:
        try:
            weight = float(input("Enter the athlete's current weight in kg: "))
            return weight
        except ValueError:
            print("Invalid weight. Please enter a valid number.")


def get_weight_category():
    while True:
        print("\nWeight Categories:")
        for category, weight in WEIGHT_CATEGORIES.items():
            if category == "Heavyweight":
                print(f"- {category}: Unlimited (over {weight}kg)")
            else:
                print(f"- {category}: Up to {weight}kg")
        category = input("Enter the competition weight category: ").lower()
        valid_categories = [cat.lower() for cat in WEIGHT_CATEGORIES.keys()]
        if category in valid_categories:
            return category.capitalize()  # Return the capitalized version for consistency
        else:
            print(f"Invalid choice. Please select from {', '.join(WEIGHT_CATEGORIES.keys())}.")


def get_competitions_count(training_plan):
    if training_plan not in ["Intermediate", "Elite"]:
        print("Only Intermediate and Elite athletes can enter competitions.")
        return 0
    while True:
        try:
            count = int(input("Enter the number of competitions entered this month: "))
            return count
        except ValueError:
            print("Invalid count. Please enter a valid number.")


def get_private_coaching_hours():
    while True:
        try:
            hours = int(input("Enter the number of hours for private coaching (0-5): "))
            if 0 <= hours <= 5:
                return hours
            else:
                print("Invalid input. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number of hours.")
