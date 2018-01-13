import csv
import os

class WhalesData:

    data_base = ""

    def __init__(self, data_base):
        self.create_path(data_base)
        self.read_csv()

    def create_path(self, data_base):
        self.data_base = data_base

    def read_csv(self):
        oos = os.name
        if oos == 'nt':
            base = self.data_base + '\\train.csv\\train.csv'
        else:
            base = self.data_base + '/train.csv/train.csv'
        print(base)

    def get_path(self):
        return self.data_base
