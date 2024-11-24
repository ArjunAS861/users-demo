from marshmallow import fields, Schema

class CreateUserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    address = fields.String(required=False)

class UserResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.Email()