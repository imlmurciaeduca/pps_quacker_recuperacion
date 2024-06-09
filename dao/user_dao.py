from model.user import User
from mongo import users

users_cache = dict()

class UserDAO:
    @staticmethod
    def create_user(user: User):
        if user.password:
            users.insert_one({
                '_id': user.username,
                'password': user.password,
                'quacks': []
            })
        
    @staticmethod
    def get_user(username: str):
        from dao.quack_dao import QuackDAO
        user = users_cache.get(username)
        if not user:
            user_data = users.find_one({'_id': username})
            if user_data:
                user = User(username=user_data['_id'])
                user.password = user_data['password']
                user.quacks = [ QuackDAO.get_quack(quack_id) for quack_id in user_data['quacks'] ]
                users_cache[username] = user
        return user
    
        
    @staticmethod
    def quack(user: User, quack_id):
        users.update_one(
            {'_id': user.username, 'quacks': {'$ne': quack_id}},
            {'$push': {'quacks': quack_id}}
        )
    