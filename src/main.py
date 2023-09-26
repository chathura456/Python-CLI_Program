from input_functions import (
    get_athlete_name, get_training_plan, get_current_weight,
    get_weight_category, get_competitions_count, get_private_coaching_hours
)
from calculation_functions import (
    calculate_monthly_fee, calculate_private_coaching_cost,
    calculate_competition_fee, compare_weight_to_category, calculate_total_cost
)
from output_functions import (
    display_athlete_name, display_itemized_costs,
    display_total_cost, display_weight_comparison
)


def main():
    # Gather input from the user
    athlete_name = get_athlete_name()
    training_plan = get_training_plan()
    current_weight = get_current_weight()
    weight_category = get_weight_category()
    competitions_count = get_competitions_count(training_plan)
    private_coaching_hours = get_private_coaching_hours()

    # Perform calculations
    monthly_fee = calculate_monthly_fee(training_plan)
    private_coaching_cost = calculate_private_coaching_cost(private_coaching_hours)
    competition_fee = calculate_competition_fee(training_plan, competitions_count)
    total_cost = calculate_total_cost(monthly_fee, private_coaching_cost, competition_fee)
    weight_comparison_message = compare_weight_to_category(current_weight, weight_category)

    # Display results to the user
    display_athlete_name(athlete_name)
    display_itemized_costs(monthly_fee, private_coaching_cost, competition_fee)
    display_total_cost(total_cost)
    display_weight_comparison(weight_comparison_message)


if __name__ == "__main__":
    main()
