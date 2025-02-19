# Directory-Structure-Generator

Directory-Structure-Generator is a Python tool that recursively scans a given directory and generates a hierarchical JSON structure of all folders and files within it. The JSON output provides a clear view of the directory's structure, making it useful for documentation, analysis, and file management purposes.

---

## Features

- Recursively scans the specified directory and all its subdirectories.
- Generates a JSON representation of the folder and file hierarchy.
- Saves the output as `directory_structure.json` in the project directory.
- Simple and easy-to-use command-line interface.

---

## Example Output

```json
{
  "folder1": {
    "subfolder1": {
      "file1.txt": null,
      "file2.txt": null
    },
    "subfolder2": {
      "file3.txt": null
    }
  },
  "folder2": {
    "file4.txt": null
  },
  "file5.txt": null
}
```

In the JSON output:

- Folder names are represented as keys.
- Subdirectories are nested as child dictionaries.
- Files are shown with `null` values.

---

## Prerequisites

- Python 3.x is required to run this script. Check your version using:
  ```bash
  python --version
  ```
  or
  ```bash
  python3 --version
  ```

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tejas2292/Directory-Structure-Generator.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Directory-Structure-Generator
   ```

---

## Usage

1. **Run the script using the Python interpreter:**

   ```bash
   python directory_structure.py
   ```

   or

   ```bash
   python3 directory_structure.py
   ```

2. **Provide the directory path when prompted**:

   ```
   Enter the directory path: /path/to/your/directory
   ```

3. **Output**:
   - The directory hierarchy will be displayed on the terminal in JSON format.
   - The same JSON output will be saved as `directory_structure.json` in the project folder.

---

## Example

```bash
python directory_structure.py
```

```
Enter the directory path: C:\output
```

Output:

```json
{
  "Project": {
    "src": {
      "main.py": null,
      "utils.py": null
    },
    "docs": {
      "README.md": null
    },
    "requirements.txt": null
  }
}
```

---

## Compatibility

- **Operating Systems**: Works on Windows, macOS, and Linux.
- **Python Versions**: Compatible with Python 3.x.

---

## Customisation

You can easily modify the script to:

- Exclude hidden files or folders.
- Include additional file metadata like size or creation date.
- Save the output in different formats (e.g., YAML or XML).

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. **Fork the repository**
2. **Create a new branch** (`feature/new-feature`)
3. **Commit your changes** (`git commit -m 'Add new feature'`)
4. **Push to the branch** (`git push origin feature/new-feature`)
5. **Open a pull request**

---

## Author

- **Tejas** - Developer and Maintainer of Directory-Structure-Generator.

---
