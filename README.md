# BMI Calculator (Python)

A small command-line tool that calculates your **Body Mass Index (BMI)** from your weight and height and tells you the WHO weight category.

## How to run

```bash
python bmi_calculator.py
```

Then enter your weight in kilograms and your height in centimetres, for example:

```
Weight in kg: 70
Height in cm: 175
Your BMI is: 22.9
Category: Normal weight
```

## How it works

```
BMI = weight (kg) / height (m)^2
```

Categories used (WHO ranges):

| BMI | Category |
| --- | -------- |
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obesity |

## What was practiced

- Reading and validating user input
- Functions with clear responsibilities (`calculate_bmi`, `bmi_category`)
- Raising `ValueError` for invalid input instead of crashing

## Note

BMI is a general guide only — it does not account for muscle mass, age, or body composition. Consult a doctor for personal health advice.
