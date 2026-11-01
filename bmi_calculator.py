#!/usr/bin/env python3
"""BMI Calculator — body mass index with WHO category.

Usage:
    python bmi_calculator.py
"""

CATEGORIES = [
    (18.5, "Underweight"),
    (25.0, "Normal weight"),
    (30.0, "Overweight"),
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI = weight (kg) / height (m)^2."""
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return weight_kg / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    """Return the WHO category for a BMI value."""
    for limit, label in CATEGORIES:
        if bmi < limit:
            return label
    return "Obesity"


def main() -> None:
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Weight in kg: "))
        height_cm = float(input("Height in cm: "))
        height_m = height_cm / 100
        bmi = calculate_bmi(weight, height_m)
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"Category: {bmi_category(bmi)}")
    print("Note: BMI is a general guide only — it does not account for")
    print("muscle mass, age, or body composition. Consult a doctor for")
    print("personal health advice.")


if __name__ == "__main__":
    main()
