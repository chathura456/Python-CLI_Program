def display_athlete_name(name):
    print(f"\nAthlete's Name: {name}")


def display_itemized_costs(monthly_fee, private_coaching_cost, competition_fee):
    print("\nItemized Costs for the Month:")
    print(f"Training Fee: £{monthly_fee:.2f}")
    print(f"Private Coaching Cost: £{private_coaching_cost:.2f}")
    print(f"Competition Fee: £{competition_fee:.2f}")


def display_total_cost(total_cost):
    print(f"\nTotal Cost for the Month: £{total_cost:.2f}")


def display_weight_comparison(weight_comparison_message):
    print("\nWeight Comparison:")
    print(weight_comparison_message)


def display_error_message(message):
    print(f"\nError: {message}")
