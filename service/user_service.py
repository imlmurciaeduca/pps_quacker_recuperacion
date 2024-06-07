from model.user import User

users_cache = dict()

class UserService:
    @staticmethod
    def get_user(username: str) -> User:
        return users_cache.get(username)
    
    @staticmethod
    def login(user: User, password: str) -> bool:
        return user.password == User.hash_password(user.username, password)
    
    @staticmethod
    def create_user(username: str, password: str) -> User:
        user = users_cache.get(username)
        if not user:
            user = User(username, password)
            users_cache[username] = user
        return None
    
    @staticmethod
    def requack(user: User, quack):
        user._User__requack(quack)