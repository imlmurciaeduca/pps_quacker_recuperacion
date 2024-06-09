from model.user import User
from dao.user_dao import UserDAO

class UserService:
    @staticmethod
    def get_user(username: str) -> User:
        return UserDAO.get_user(username)
    
    @staticmethod
    def login(user: User, password: str) -> bool:
        return user.password == User.hash_password(user.username, password)
    
    @staticmethod
    def create_user(username: str, password: str) -> User:
        user = UserDAO.get_user(username)
        if not user:
            user = User(username, password)
            UserDAO.create_user(user)
        return None
    
    @staticmethod
    def requack(user: User, quack):
        user._User__requack(quack)
        UserDAO.quack(user, quack.id)
    
    @staticmethod
    def quack(user: User, text: str):
        quack = user._User__quack(text)
        UserDAO.quack(user, quack.id)
        return quack