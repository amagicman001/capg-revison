class InvalidRequestIdException(Exception):
    message=""
    def __init__(self,message):
        self.message=message

    
