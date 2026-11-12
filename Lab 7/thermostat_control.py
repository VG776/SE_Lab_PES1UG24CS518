import math

def parse_setpoint(text):
    if text is None or not isinstance(text, str):
        return None
    text = text.strip()
    if len(text) < 2:
        return None
    unit = text[-1].upper()
    if unit not in ('C', 'F'):
        return None
    try:
        value = float(text[:-1])
        if math.isnan(value) or math.isinf(value):
            return None
    except (ValueError, TypeError):
        return None
    if unit == 'F':
        value = (value - 32) * 5 / 9
    return round(value, 1)

def average_temperature(readings_csv):
    if readings_csv is None or not isinstance(readings_csv, str):
        return None
    parts = readings_csv.split(',')
    values = []
    for r in parts:
        r = r.strip()
        if not r:
            return None
        try:
            val = float(r)
            if math.isnan(val) or math.isinf(val):
                return None
            values.append(val)
        except (ValueError, TypeError):
            return None
    if not values:
        return None
    return sum(values) / len(values)

def schedule_slot(time_text):
    if time_text is None or not isinstance(time_text, str):
        return None
    parts = time_text.strip().split(':')
    if len(parts) != 2:
        return None
    try:
        hour = int(parts[0].strip())
        minute = int(parts[1].strip())
    except (ValueError, TypeError):
        return None
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        return None
    if hour < 6:
        return 'night ' + parts[1].strip()
    return 'day ' + str(minute)

def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    result = parse_setpoint(user_input)
    print("Setpoint in Celsius:", result)

    print("\n==== Running average_temperature ====")
    user_input = input("Enter sensor readings as CSV (e.g. 20.5,21,22.5): ")
    result = average_temperature(user_input)
    print("Average Temperature:", result)

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    result = schedule_slot(user_input)
    print("Schedule Slot:", result)

if __name__ == "__main__":
    main()
