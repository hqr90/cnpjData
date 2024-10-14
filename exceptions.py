# cnpjData/exceptions.py

class APIException(Exception):
    def __init__(self, status, message):
        super().__init__(f"APIException: Status {status} - {message}")
        self.status = status
        self.message = message

class RateLimitException(APIException):
    def __init__(self, status, message):
        super().__init__(status, message)
        self.message = "Limite de requisições atingido."
