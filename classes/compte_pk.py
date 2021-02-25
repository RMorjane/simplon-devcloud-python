class Compte:

    def __init__(self,cpnum,cplib):
        self.num = cpnum
        self.lib = cplib

    def display(self):
        print(self.num,self.lib)

    def set_num(self,cpnum):
        self.num = cpnum

    def get_num(self):
        return self.num

    def set_lib(self,cplib):
        self.lib = cplib

    def get_lib(self):
        return self.lib