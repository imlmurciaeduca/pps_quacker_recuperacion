from uuid import uuid4
from datetime import datetime

class Quack:
    def __init__(self, author: str, text: str, creation_timestamp: datetime) -> None:
        self.id = str(uuid4())
        self.author = author
        self.text = text
        self.creation_timestamp = creation_timestamp
        self.requacked_by = []
        self.favs = 0
    
    def __str__(self) -> str:
        return f'''{self.text}. Autor: {self.author} ({self.creation_timestamp.strftime('%d/%m/%Y, %H:%M:%S')}).
            {len(self.requacked_by)} R | {self.favs} F. ID: {self.id}'''