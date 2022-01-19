# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender (M or F): ')
    birthdate = input('Enter your birthdate(YYYY-MM-DD): ')
    weight_pounds = int(input('Enter your weight in U.S. pounds: '))
    height_inches = int(input('Enter your height in U.S. inches: '))
    
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate)
    weight_kg = kg_from_lb(weight_pounds)
    weight_stone = stone_from_kg(weight_kg)
    height_cm = cm_from_in(height_inches)
    height_m = height_cm / 100
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Print the results for the user to see.
    print(age, weight_kg, weight_stone, height_cm, height_m, bmi, bmr)
    
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return pounds * 0.45359237


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches * 2.54


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return weight / (height / 100) ** 2


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    
    if gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
        
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        
    return bmr
    
def stone_from_kg(kg):
    """Convert a mass in kilograms to stone.
    Parameter kg: a mass in kilograms.
    Return: the mass in stone.
    """
    return kg * 0.15747317


# Call the main function so that
# this program will start executing.
main()