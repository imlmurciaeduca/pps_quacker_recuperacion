from flask import Flask, jsonify, request, Response, render_template
from service.user_service import UserService
from service.quack_service import QuackService
from uuid import uuid4
import os

login_dict = dict()

app = Flask(__name__)
app.config['IMAGES_FOLDER'] = os.path.join('static', 'images')

@app.route('/')
def index():
    quacks = QuackService.get_all_quacks()
    quacks = sorted(quacks, key = lambda quack: quack.creation_timestamp, reverse=True)
    return render_template('index.html',imagen=os.path.join(app.config['IMAGES_FOLDER'], 'quacker.webp'), quacks=quacks)

@app.route('/signup', methods=['POST'])
def signup():
    data = dict(request.get_json(force=True))
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return Response(status = 403)
    user = UserService.get_user(username) 
    if not user:
        UserService.create_user(username, password)
        return Response(status = 200)
    else:
        return Response(response='User already exists', status=400)

@app.route('/login', methods=['POST'])
def login():
    data = dict(request.get_json(force=True))
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return Response(status = 403)
    user = UserService.get_user(username)    
    if not user:
        return Response(response='Wrong username or password', status=404)
    else:
        if user not in login_dict.values():
            login_id = str(uuid4())
            login_dict[login_id] = user
        else:
            login_id = list(login_dict.keys())[list(login_dict.values()).index(user)]
        return jsonify({'token': login_id}), 200

@app.route('/<user_token>/quack', methods=['POST'])
def quack(user_token: str):
    user = login_dict.get(user_token)
    if not user:
        return Response(response='Token not valid, did you login?', status=404)
    else:
        data = dict(request.get_json(force=True))
        quack_text = data['quack']
        quack = QuackService.create_quack(user, quack_text)
        return jsonify({'quack_id': quack.id}), 200

@app.route('/<user_token>/requack', methods=['POST'])
def requack(user_token: str):
    user = login_dict.get(user_token)
    data = dict(request.get_json(force=True))
    quack_id = data.get('quack_id')
    
    if not user:
        return Response(response='User token not valid, did you login?', status=404)
    elif not quack_id:
        return Response(response='Please, provide a quack id', status=403)
    
    quack = QuackService.get_quack(quack_id)
    if not quack:
        return Response(response='Quack not found', status=404)
    
    QuackService.requack(user, quack)
    return Response(status=200)
   
@app.route('/<username>', defaults={'all': ''})
@app.route('/<username>/', defaults={'all': ''})
@app.route('/<username>/<all>', methods = ['GET'])
def get_quacks_by_username(username: str, all: str):
    if (all:=all.casefold()) not in ('', 'all'):
        return Response(response='Wrong URL', status = 403)
    quacks = QuackService.get_quacks_by_username(username, all == 'all')[::-1]
    if quacks is not None:
        quacks = [quack.__dict__ for quack in quacks]
        return jsonify(quacks), 200
    return Response(response='User not valid', status=404)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')