import json

class write_file:
    """Write file data by path name"""

    def __init__(self, file_path) -> None:
        """Contstructor: writes path"""

        self.path = file_path

    def write_file(self, array) -> None:
        """Function: reads data from file"""

        # tmp = []
        # for i in tqdm(range(len(array)), desc="Запись результата в файл"):
        #         tmp.append(array[i].copy())
        json.dump(array, open(self.path,"w",encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)

