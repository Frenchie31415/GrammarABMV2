import logging

class App:
    def __init__(self):
        self.number = 0
        self.log_set()
    
    def set_number(self, new_num):
        self.number = new_num
        self.log_change()
    
    def add_one(self):
        self.number = self.number + 1
        self.log_change()
    
    def subtract_one(self):
        self.number = self.number - 1
        self.log_change()

    def double(self):
        self.number = self.number * 2
        self.log_change()

    def divide_by_three(self):
        self.number = self.number / 3
        self.log_change()

    def log_set(self):
        logging.basicConfig(filename="AppLog.log",filemode='a',datefmt='%H:%M:%S',level=logging.INFO)
        log_statement = "SET,",str(self.number)
        logging.info(log_statement)
    
    def log_change(self):
        logging.basicConfig(filename="AppLog.log",filemode='a',datefmt='%H:%M:%S',level=logging.INFO)
        log_statement = "CHANGE,",str(self.number)
        logging.info(log_statement)
    
if __name__ == "__main__":
    app = App()
    app.set_number(1)
    app.add_one()