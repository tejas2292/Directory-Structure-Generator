import os
import json

def get_parent_level(root_dir):
    """
    Get only the top-level files and folders in the directory.
    """
    return {item: None if os.path.isfile(os.path.join(root_dir, item)) else {} for item in os.listdir(root_dir)}

def get_full_hierarchy(root_dir):
    """
    Recursively get the entire directory structure as a nested dictionary.
    """
    directory_structure = {}
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            directory_structure[item] = get_full_hierarchy(item_path)
        else:
            directory_structure[item] = None
    return directory_structure

def save_json_to_output(directory_hierarchy, filename):
    """
    Save the JSON data to the 'output' folder, creating the folder if it doesn't exist.
    """
    output_folder = "output"

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, filename)

    with open(output_path, 'w') as f:
        json.dump(directory_hierarchy, f, indent=4)

    print(f"\nDirectory structure saved to '{output_path}'")

def main():
    # Accept user input for directory path
    root_directory = input("Enter the directory path: ")
    
    # Validate directory path
    if not os.path.isdir(root_directory):
        print("Invalid directory path. Please provide a valid directory.")
        return
    
    # Accept user choice for hierarchy type
    print("\nChoose an option:")
    print("1. Get Parent Level (Only top-level files and folders)")
    print("2. All Hierarchy (Full directory structure)")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        directory_hierarchy = get_parent_level(root_directory)
        output_filename = "parent_level_structure.json"
    elif choice == "2":
        directory_hierarchy = get_full_hierarchy(root_directory)
        output_filename = "full_directory_structure.json"
    else:
        print("Invalid choice. Exiting.")
        return

    # Convert the structure to JSON format
    json_output = json.dumps(directory_hierarchy, indent=4)

    # Print JSON output
    print("\nDirectory Structure:")
    print(json_output)

    # Save JSON to 'output' folder
    save_json_to_output(directory_hierarchy, output_filename)

if __name__ == "__main__":
    main()
