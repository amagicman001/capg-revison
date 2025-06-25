## Please do not change the skelecton code given here. Write your code only in the provided places alone.

class InvalidBookIDException(Exception):
    message=""
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
        