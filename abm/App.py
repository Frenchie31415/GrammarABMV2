import logging

class App:
    def __init__(self):
        self.number = 0
        self.filename = "AppLog"
        self.log_set()

    def set_filename(self,name):
        self.filename = name
    
    def set_number(self, new_num):
        self.number = new_num
        self.log_change()
    
    def add_one(self):
        self.number = self.number + 1
        self.log_change()
    
    def subtract_one(self):
        self.number = self.number - 1
        self.log_change()

    def half(self):
        self.number = self.number / 2
        self.log_change()

    def triple(self):
        self.number = self.number * 3
        self.log_change()

    def log_set(self):
        file = self.filename + '.log'
        logging.basicConfig(filename=file,filemode='a',datefmt='%H:%M:%S',level=logging.INFO)
        log_statement = "SET",str(self.number)
        logging.info(log_statement)
    
    def log_change(self):
        file = self.filename + '.log'
        logging.basicConfig(filename=file,filemode='a',datefmt='%H:%M:%S',level=logging.INFO)
        log_statement = "CHANGE",str(self.number)
        logging.info(log_statement)
    
if __name__ == "__main__":
    app = App()
    app.set_number(1)
    app.add_one()