'''Class to read a .json file'''

import json

class Reader:
    '''
    Reads and stores json specified in filepath data in 
    self.out

    return: None
    '''
    def __init__(self, filepath=str) -> None:
        with open(filepath, "r", encoding="utf-8") as stream:
            self.out = json.loads(stream)
