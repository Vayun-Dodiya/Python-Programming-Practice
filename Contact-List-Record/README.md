# Python Contact Management System
A robust, error-resistant Command Line Interface (CLI) application for managing personal contacts using a flat-file database.

## 🚀 Key Features
* **Record-Based Storage**: Uses custom markers (`->`) to define data boundaries, ensuring high data integrity during operations.
* **Bulletproof Input Validation**: Implements `try...except` blocks in the menu system to prevent crashes from non-numeric inputs.
* **Advanced Deletion Logic**: Utilizes Pythonic list slicing and exception handling to safely remove records, including edge cases like deleting the final entry in the database.
* **Case-Insensitive Search**: Normalizes all queries and stored data to ensure user-friendly searching.

## 🛠 Technical Skills Demonstrated
* **File I/O**: Efficient use of `with open()` for safe file stream management.
* **Data Structures**: Advanced manipulation of lists and string formatting.
* **Exception Handling**: Professional use of `ValueError` trapping to manage program flow.