import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as file:
        list_of_dict = json.load(file)
    total_sum = sum([item["score"] * item["weight"] for item in list_of_dict])
    return round(total_sum, 3)

print(task())
