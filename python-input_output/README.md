# Input/Output

- [test_files](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/tree/main/0x0B-python-input_output/test_files) - Directory that contains files for testing Python scripts

- [0-read_file.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/0-read_file.py) - Python script that reads a text file (`UTF8`) and prints it to stdout.

- [1-write_file.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/1-write_file.py) - Python script that writes a string to a text file (`UTF8`) and returns the number of characters written.

- [10-student.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/10-student.py) - Python script that creates a class `Student` with:
   - Public instance attributes:
      - `first_name`
      - `last_name`
      - `age`
   - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance
      - If `attrs` is a list of strings, only attribute names contained in the list must be retrieved
      - Otherwise, all attributes must be retrieved

- [11-student.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/11-student.py) - Python script that creates a class `Student` with:
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

- [12-pascal_triangle.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/12-pascal_triangle.py) - Python script that returns a list of lists of integers representing the Pascal's triangle of `n`:
   - Returns an empty list if `n <= 0`
   - `n` will always be an integer

- [2-append_write.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/2-append_write.py) - Python script that appends a string at the end of a text file (`UTF8`) and returns the number of characters added. If the file doesn't exist, it should be created.

- [3-to_json_string.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/3-to_json_string.py) - Python script that returns the JSON representation of an object(string).

- [4-from_json_string.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/4-from_json_string.py) - Python script that returns an object (Python data structure) represented by a JSON string.

- [5-save_to_json_file.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py) - Python script that writes an Object to a text file, using a JSON representation.

- [6-load_from_json_file.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py) - Python script that creates an Object from a "JSON file".

- [7-add_item.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/7-add_item.py) - Python script that adds all arguments to a Python list, and then save them to a file. The list must be saved as a JSON representation in a file named `add_item.json`. If the file doesn't exist, it should be created.

- [8-class_to_json.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py) - Python script that returns the dictionary description with simple data structure(list, dictionary, string, integer and boolean) for JSON serialization of an object.

- [9-student.py](https://github.com/FatjonMileti/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/9-student.py) - Python script that creates a class `Student` with:
   - Public instance attributes:
      - `first_name`
      - `last_name`
      - `age`
   - Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance
