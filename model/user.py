from datetime import datetime
from hashlib import sha256

class User:
    __APPEND = 'GaD*ZGWOyxLBLppb0qPHe!VXKt4CW9F8@ABw0O2dymYy8OkRqna0yZeTwIbM4kbjFXM1*xtTPU6SKm%DZfQQSNqOwbqyF#caATMGhMPuFvsohkyjyQZOBNGR!w2!uw'
    
    def __init__(self, username: str, password: str = None):
        self.username = username
        self.password = User.hash_password(username, password) if password else None
        self.quacks = []
    
    def __quack(self, text: str):
        from model.quack import Quack
        timestamp = datetime.now()
        quack = Quack(author=self.username, text=text, creation_timestamp=timestamp)
        self.quacks.append(quack)
        return quack
        
    def __requack(self, quack):
        if quack not in self.quacks:
            self.quacks.append(quack)
            quack.requacked_by.append(self.username)
            
    @staticmethod
    def hash_password(username: str, plain_password: str):
        return sha256((username + plain_password + User.__APPEND).encode()).hexdigest()
    
    def __str__(self) -> str:
        quacks_str = '\n'.join([f'\t{quack}' for quack in self.quacks])
        return f'''{self.username}. Quacks:\n{quacks_str}
    '''