from model.user import User
from model.quack import Quack

quacks_cache = dict()

class QuackService:
    @staticmethod
    def get_quack(id: str):
        return quacks_cache.get(id)
    
    @staticmethod
    def create_quack(author: User, text: str):
        quack = author._User__quack(text)
        quacks_cache[quack.id] = quack
        return quack
        
    @staticmethod
    def get_all_quacks():
        return list(quacks_cache.values())
        
    @staticmethod
    def get_quacks_by_username(username: str, requacks: bool):
        from service.user_service import UserService
        user = UserService.get_user(username)
        if user:
            return user.quacks if requacks else list(filter(lambda quack: (quack.author == username), user.quacks))
        return None
    
    @staticmethod
    def requack(user: User, quack: Quack):
        from service.user_service import UserService
        UserService.requack(user, quack)