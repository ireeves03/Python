# Define variables for kilogram values
kg_value_1 = 25
kg_value_2 = 60
kg_value_3 = 38
kg_value_4 = 120

# Conversion factor: 1 kilogram = 2.20462 pounds
conversion_factor = 2.20462

# Calculate pounds for each kilogram value
lbs_1 = kg_value_1 * conversion_factor
lbs_2 = kg_value_2 * conversion_factor
lbs_3 = kg_value_3 * conversion_factor
lbs_4 = kg_value_4 * conversion_factor

# Output the results
print(f"\n{kg_value_1} kilograms is equal to {lbs_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {lbs_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {lbs_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {lbs_4:.2f} pounds.")
print()