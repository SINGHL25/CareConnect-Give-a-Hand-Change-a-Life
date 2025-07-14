import json

def load_causes(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)
    return data

