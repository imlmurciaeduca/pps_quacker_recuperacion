from model.quack import Quack
from mongo import quacks

quacks_cache = dict()

class QuackDAO:
    @staticmethod
    def create_quack(quack: Quack):
        quacks.insert_one({
            '_id': quack.id,
            'author': quack.author,
            'text': quack.text,
            'creation_timestamp': quack.creation_timestamp,
            'requacked_by': [],
            'favs': quack.favs
        })
        quacks_cache[quack.id] = quack
        
    @staticmethod
    def get_quack(quack_id):
        quack = quacks_cache.get(quack_id)
        if not quack:
            quack_data = quacks.find_one({'_id': quack_id})
            if quack_data:
                quack = Quack(author=quack_data['author'], text=quack_data['text'], creation_timestamp=quack_data['creation_timestamp'])
                quack.id = quack_data['_id']
                quack.favs = quack_data['favs']
                quack.requacked_by = quack_data['requacked_by']
                quacks_cache[quack_id] = quack
        return quack
    
    @staticmethod
    def requack(username: str, quack: Quack):
        if quack.author != username:
            quacks.update_one(
                {'_id': quack.id, 'requacked_by': {'$ne': username}},
                {'$push': {'requacked_by': username}}
            )
    
    @staticmethod
    def get_all_quacks():
        return [ QuackDAO.get_quack(quack['_id']) for quack in quacks.find({}) ]