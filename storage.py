from collections import OrderedDict
import json


class JsonDatabaseStorage:

    @staticmethod
    def create(model):
        with open('database.json', 'r+') as file:
            # load existing json data into dict
            file_data = json.load(file)
            # add the new data
            file_data.update(model.as_dict())
            # set file current position at offset
            file.seek(0)
            # convert back to json
            json.dump(file_data, file, indent=4)
            return model

    @staticmethod
    def fetch() -> dict:
        with open('database.json', 'r') as file:
            # load existing json data into dict
            file_data = json.load(file)
            return OrderedDict(reversed(list(file_data.items())))

