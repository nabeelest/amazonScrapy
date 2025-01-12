
import json
import os

def save_to_json(query, products, output_dir="public\output"):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{query}.json")
    try:
        with open(file_path, "w") as file:
            json.dump(products, file, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data: {e}")
