import os
import json

def get_directory_structure(root_dir):
    """
    Recursively get the directory structure as a nested dictionary.
    """
    directory_structure = {}
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            directory_structure[item] = get_directory_structure(item_path)
        else:
            directory_structure[item] = None
    return directory_structure

def main():
    # Specify the root directory to scan
    root_directory = input("Enter the directory path: ")
    
    # Check if the directory exists
    if not os.path.isdir(root_directory):
        print("Invalid directory path. Please provide a valid directory.")
        return

    # Get the directory structure
    directory_hierarchy = get_directory_structure(root_directory)

    # Convert the structure to JSON format
    json_output = json.dumps(directory_hierarchy, indent=4)

    # Print the JSON output
    print(json_output)

    # Save to a JSON file (optional)
    output_file = 'directory_structure.json'
    with open(output_file, 'w') as f:
        f.write(json_output)
    
    print(f"\nDirectory structure saved to '{output_file}'")

if __name__ == "__main__":
    main()
