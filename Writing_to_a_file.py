import json
from pathlib import Path
from add_orders import discount_percentages

AAA = Path(__file__).order_management / "order.json"


def writing_to_json():
    new_dict = discount_percentages()
    with open(AAA, "w", encoding="utf-8") as file:
        json.dump(new_dict, file, indent=2, ensure_ascii=False)


writing_to_json()
