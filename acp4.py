def convert_length(value, from_unit, to_unit):
    # Conversion rates to meters
    units_to_meters = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'foot': 0.3048,
        'inch': 0.0254,
        'mile': 1609.34,
        'yard': 0.9144
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in units_to_meters or to_unit not in units_to_meters:
        return "❌ Invalid unit entered."

    # Convert from input unit to meters, then meters to target unit
    value_in_meters = value * units_to_meters[from_unit]
    converted_value = value_in_meters / units_to_meters[to_unit]

    return converted_value

# Get user input
print("📏 Length Converter")
value = float(input("Enter value to convert: "))
from_unit = input("From unit (e.g., meter, inch, kilometer): ")
to_unit = input("To unit (e.g., foot, mile, centimeter): ")

result = convert_length(value, from_unit, to_unit)

if isinstance(result, str):
    print(result)
else:
    print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")
