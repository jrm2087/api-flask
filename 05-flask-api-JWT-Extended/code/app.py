from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from blacklist import BLACKLIST
from db import db

ACCESS_EXPIRES = timedelta(hours=1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config["JWT_SECRET_KEY"] = "joser_-"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWTManager(app)


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    print('-->', jwt_payload)
    return jwt_payload['sub'] in BLACKLIST


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_refresh_callback(error):
    return jsonify({
        'message': 'The token is not refresh',
        'error': 'refresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has been revoked.',
        'error': 'token_revoked'
    }), 401


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
