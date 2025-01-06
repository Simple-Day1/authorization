class DomainError(Exception):
    def __init__(self, massage: str = 'Dommain error occured'):
        self.massage = massage