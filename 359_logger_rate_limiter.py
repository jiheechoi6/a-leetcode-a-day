class Logger:

    def __init__(self):
        self.history = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if(message in self.history and (timestamp - self.history[message]) < 10):
            return False
        else:
            self.history[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
