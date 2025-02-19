import json
import os

def load_json(file_path):
    """
    Load JSON data from a file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_directories(old_dir, new_dir):
    """
    Recursively compare two directory structures.
    Returns items that are present in old_dir but missing in new_dir.
    """
    differences = {}

    for key, value in old_dir.items():
        # If the key is not in the new directory, add it to differences
        if key not in new_dir:
            differences[key] = value
        else:
            # If it's a folder (i.e., its value is a dictionary), recurse
            if isinstance(value, dict) and isinstance(new_dir[key], dict):
                sub_diff = compare_directories(value, new_dir[key])
                if sub_diff:  # Only add non-empty differences
                    differences[key] = sub_diff

    return differences

def main():
    # Provide the paths of the two JSON files
    old_json_file = input("Enter the path of the old directory JSON file: ")
    new_json_file = input("Enter the path of the new directory JSON file: ")

    # Check if both files exist
    if not os.path.exists(old_json_file) or not os.path.exists(new_json_file):
        print("Invalid file path(s). Please provide valid JSON file paths.")
        return

    # Load JSON data
    old_directory = load_json(old_json_file)
    new_directory = load_json(new_json_file)

    # Compare directories
    differences = compare_directories(old_directory, new_directory)

    # Print differences
    print("\nFiles and folders present in the old directory but missing in the new one:")
    print(json.dumps(differences, indent=4))

    # Save differences to a file
    output_file = 'missing_in_new_directory.json'
    with open(output_file, 'w') as f:
        json.dump(differences, f, indent=4)
    
    print(f"\nDifferences saved to '{output_file}'")

if __name__ == "__main__":
    main()
