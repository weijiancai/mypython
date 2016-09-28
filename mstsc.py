import os
import cPickle as pickle


class Mstsc:
    def __init__(self):
        self.mstscDataFile = "mstsc.data"
        f = file(self.mstscDataFile, 'r')
        self.list = pickle.load(f)
