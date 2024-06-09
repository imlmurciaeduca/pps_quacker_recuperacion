from model.user import User
from model.quack import Quack
from dao.quack_dao import QuackDAO
from service.user_service import UserService

class QuackService:
    @staticmethod
    def get_quack(id: str):
        return QuackDAO.get_quack(id)
    
    @staticmethod
    def create_quack(author: User, text: str):
        quack = UserService.quack(author, text)
        QuackDAO.create_quack(quack)
        return quack
        
    @staticmethod
    def get_all_quacks():
        return QuackDAO.get_all_quacks()
        
    @staticmethod
    def get_quacks_by_username(username: str, requacks: bool):
        from service.user_service import UserService
        user = UserService.get_user(username)
        if user:
            return user.quacks if requacks else list(filter(lambda quack: (quack.author == username), user.quacks))
        return None
    
    @staticmethod
    def requack(user: User, quack: Quack):
        UserService.requack(user, quack)
        QuackDAO.requack(user.username, quack)