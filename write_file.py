import json

class write_file:
    """Write file data by path name"""

    def __init__(self, file_path) -> None:
        """Contstructor: writes path"""

        self.path = file_path

    def write_file(self, array) -> None:
        """Function: reads data from file"""

        json.dump(array, open(self.path,"w",encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)

