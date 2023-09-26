from constants import TRAINING_FEES, PRIVATE_TUITION_FEE, COMPETITION_FEE, WEIGHT_CATEGORIES


def calculate_monthly_fee(training_plan):
    weekly_fee = TRAINING_FEES.get(training_plan, 0)
    return weekly_fee * 4  # Assuming a month consists of 4 weeks


def calculate_private_coaching_cost(hours):
    return hours * PRIVATE_TUITION_FEE


def calculate_competition_fee(training_plan, competitions_count):
    if training_plan in ["Intermediate", "Elite"]:
        return competitions_count * COMPETITION_FEE
    return 0  # Beginner athletes can't enter competitions


def compare_weight_to_category(current_weight, weight_category):
    upper_limit = WEIGHT_CATEGORIES.get(weight_category, float('inf'))
    if current_weight <= upper_limit:
        return f"The athlete's current weight is within the {weight_category} category."
    else:
        return f"The athlete's current weight exceeds the {weight_category} category limit."


def calculate_total_cost(monthly_fee, private_coaching_cost, competition_fee):
    return monthly_fee + private_coaching_cost + competition_fee
