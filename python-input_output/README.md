# Input/Output

- [0-read_file.py](./0-read_file.py) - Python script that reads a text file (`UTF8`) and prints it to stdout.

- [1-write_file.py](./1-write_file.py) - Python script that writes a string to a text file (`UTF8`) and returns the number of characters written.

- [10-student.py](./10-student.py) - Python script that creates a class `Student` with:
   - Public instance attributes:
      - `first_name`
      - `last_name`
      - `age`
   - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance
      - If `attrs` is a list of strings, only attribute names contained in the list must be retrieved
      - Otherwise, all attributes must be retrieved

- [11-student.py](./11-student.py) - Python script that creates a class `Student` with:
   - Public instance attributes:
      - `first_name`
      - `last_name`
      - `age`
   - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance
      - If `attrs` is a list of strings, only attribute names contained in the list must be retrieved
      - Otherwise, all attributes must be retrieved
    - Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
      - `json` will always be a dictionary
      - A dictionary key will be public attribute name
      - A dictionary value will be the value of the public attribute

- [12-pascal_triangle.py](./12-pascal_triangle.py) - Python script that returns a list of lists of integers representing the Pascal's triangle of `n`:
   - Returns an empty list if `n <= 0`
   - `n` will always be an integer

- [2-append_write.py](./2-append_write.py) - Python script that appends a string at the end of a text file (`UTF8`) and returns the number of characters added. If the file doesn't exist, it should be created.

- [3-to_json_string.py](./3-to_json_string.py) - Python script that returns the JSON representation of an object(string).

- [4-from_json_string.py](./4-from_json_string.py) - Python script that returns an object (Python data structure) represented by a JSON string.

- [5-save_to_json_file.py](./5-save_to_json_file.py) - Python script that writes an Object to a text file, using a JSON representation.

- [6-load_from_json_file.py](./6-load_from_json_file.py) - Python script that creates an Object from a "JSON file".

- [7-add_item.py](./7-add_item.py) - Python script that adds all arguments to a Python list, and then save them to a file. The list must be saved as a JSON representation in a file named `add_item.json`. If the file doesn't exist, it should be created.

- [8-class_to_json.py](./8-class_to_json.py) - Python script that returns the dictionary description with simple data structure(list, dictionary, string, integer and boolean) for JSON serialization of an object.

- [9-student.py](./9-student.py) - Python script that creates a class `Student` with:
   - Public instance attributes:
      - `first_name`
      - `last_name`
      - `age`
   - Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance
