from sqlite3 import IntegrityError
from xml.dom import ValidationErr

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from marshmallow.validate import Validator

from app.schemas.user_schema import CreateUserSchema, UserResponseSchema
from app.services.user_service import UserService

user_blueprint = Blueprint("users",__name__, url_prefix="/users")
user_service = UserService()

@user_blueprint.route('/', methods=['POST'])
def create_user():
    try:
        data = CreateUserSchema().load(request.json)
        user = user_service.create_user(data)
        return jsonify(UserResponseSchema().dump(user)), 201
    except ValidationError as error:
        return jsonify({ "errors" : error.messages}),400
    except Exception as error:
        return jsonify({"errors": "email is already present"}), 400


@user_blueprint.route('/<int:user_id>')
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        return jsonify(UserResponseSchema().dump(user)), 200
    except Exception as e:
        print(e)
        return {}, 404
