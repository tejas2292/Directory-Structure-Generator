# Directory-Structure-Generator

Directory-Structure-Generator is a Python tool that scans a given directory and generates a hierarchical JSON structure of all folders and files. It provides two modes:

1. **Parent Level** – Shows only the top-level folders and files.
2. **All Hierarchy** – Recursively scans all subdirectories.

The JSON output provides a clear view of the directory's structure, making it useful for documentation, analysis, and file management.

---

## Features

- **Two scanning modes**:
  - **Parent Level**: Only lists top-level files and folders.
  - **All Hierarchy**: Recursively scans all folders and files.
- **Stores output in an `output/` folder**, creating it if it doesn't exist.
- **Easy-to-use command-line interface**.
- **Generates JSON output**, making it easy to parse programmatically.

---

## Example Outputs

### **1. Parent Level Output**

If the directory contains:

```
/my_directory
  ├── folder1
  ├── folder2
  ├── file1.txt
  ├── file2.txt
```

The output JSON (`output/parent_level_structure.json`) will be:

```json
{
  "folder1": {},
  "folder2": {},
  "file1.txt": null,
  "file2.txt": null
}
```

### **2. Full Hierarchy Output**

If `folder1` and `folder2` contain additional files:

```
/my_directory
  ├── folder1
  │   ├── subfolder1
  │   ├── subfolder2
  │   │   ├── file3.txt
  ├── folder2
  │   ├── file4.txt
  ├── file1.txt
  ├── file2.txt
```

The output JSON (`output/full_directory_structure.json`) will be:

```json
{
  "folder1": {
    "subfolder1": {},
    "subfolder2": {
      "file3.txt": null
    }
  },
  "folder2": {
    "file4.txt": null
  },
  "file1.txt": null,
  "file2.txt": null
}
```

---

## Prerequisites

- **Python 3.x** is required. Check your version using:
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

1. **Run the script:**

   ```bash
   python directory_scanner.py
   ```

   or

   ```bash
   python3 directory_scanner.py
   ```

2. **Enter the directory path when prompted**:

   ```
   Enter the directory path: /path/to/your/directory
   ```

3. **Choose an option**:

   ```
   1. Get Parent Level (Only top-level files and folders)
   2. All Hierarchy (Full directory structure)
   ```

   Enter `1` or `2` based on the required depth.

4. **Output**:
   - The directory hierarchy is displayed in the terminal.
   - The JSON output is saved in the **`output/` folder**:
     - **Parent Level Output:** `output/parent_level_structure.json`
     - **Full Hierarchy Output:** `output/full_directory_structure.json`

---

## Example

```bash
python directory_scanner.py
```

```
Enter the directory path: C:\Users\Tejas\Documents
Choose an option:
1. Get Parent Level (Only top-level files and folders)
2. All Hierarchy (Full directory structure)
Enter your choice (1 or 2): 2
```

Output (Saved in `output/full_directory_structure.json`):

```json
{
  "Projects": {
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

- **Operating Systems**: Works on **Windows**, **macOS**, and **Linux**.
- **Python Versions**: Compatible with **Python 3.x**.

---

## Customisation

You can modify the script to:

- **Exclude hidden files or folders**.
- **Include additional metadata** like file size, creation date, etc.
- **Save the output in other formats** (e.g., YAML, XML).

---

## Contributing

Contributions are welcome! If you'd like to contribute:

1. **Fork the repository**
2. **Create a new branch** (`feature/new-feature`)
3. **Commit your changes** (`git commit -m 'Add new feature'`)
4. **Push to the branch** (`git push origin feature/new-feature`)
5. **Open a pull request**

---

## Author

- **Tejas** - Developer and Maintainer of Directory-Structure-Generator.

---
