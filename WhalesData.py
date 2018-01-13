
class WhalesData:

    data_base = ""

    def __init__(self, data_base):
        self.create_path(data_base)

    def create_path(self, data_base):
        self.data_base = data_base

    def get_path(self):
        return self.data_base
