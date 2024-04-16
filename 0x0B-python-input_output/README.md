## 0x0B. Python - Input/Output

**Key Takeaways:**

- Benefits of Python programming
- File handling basics: opening, writing, and reading files
- Understanding JSON, serialization, and deserialization
- Converting data between Python and JSON formats

**0. Read file**

- Function: 'read_file(filename="")'
- Reads a text file (UTF8) and prints its content to stdout
- Implemented with the 'with' statement

**1. Number of lines**

- Function: 'number_of_lines(filename="")'
- Returns the number of lines in a text file
- Utilizes the 'with' statement

**2. Read n lines**

- Function: 'read_lines(filename="", nb_lines=0)'
- Reads and prints n lines of a text file (UTF8)
- If nb_lines <= 0 or >= total lines, reads the entire file
- Uses the 'with' statement

**3. Write to a file**

- Function: 'write_file(filename="", text="")'
- Writes a string to a text file (UTF8) and returns characters written
- Implemented with the 'with' statement

**4. Append to a file**

- Function: 'append_write(filename="", text="")'
- Appends a string to the end of a text file (UTF8) and returns added characters
- Creates the file if it doesn't exist
- Utilizes the 'with' statement

**5. To JSON string**

- Function: 'to_json_string(my_obj)'
- Returns the JSON representation of an object (string)

**6. From JSON string to Object**

- Function: 'from_json_string(my_str)'
- Returns a Python data structure represented by a JSON string

**7. Save Object to a file**

- Function: 'save_to_json_file(my_obj, filename)'
- Writes an Object to a text file using JSON representation
- Implemented with the 'with' statement

**8. Create object from a JSON file**

- Function: 'load_from_json_file(filename)'
- Creates an Object from a JSON file
- Uses the 'with' statement

**9. Load, add, save**

- Script: Adds arguments to a Python list and saves them to a JSON file
- Utilizes 'save_to_json_file' and 'load_from_json_file'

**10. Class to JSON**

- Function: 'class_to_json(obj)'
- Returns dictionary description for JSON serialization of an object

**11. Student to JSON**

- Class: 'Student'
- Defines a student with attributes: first_name, last_name, age
- Method: 'to_json()' retrieves a dictionary representation

**12. Student to JSON with filter**

- Class: 'Student'
- Defines a student with attributes: first_name, last_name, age
- Method: 'to_json(attrs=None)' retrieves a filtered dictionary representation

**13. Student to disk and reload**

- Class: 'Student'
- Defines a student with attributes: first_name, last_name, age
- Methods: 'to_json(attrs=None)' and 'reload_from_json(json)'
- Enables saving and reloading student attributes from disk

**14. Pascal's Triangle**

- Function: 'pascal_triangle(n)'
- Returns Pascal’s triangle of n as a list of lists of integers