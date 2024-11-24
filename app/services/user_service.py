from app.models.user import User
from app.db import db

class UserService:

    def create_user(self, data):
        user = User(
            name=data["name"],
            email=data["email"],
            password=data["password"],  # Hash in real scenarios
            address=data.get("address", "arjun")
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get_user(self, user_id):
        user = User.query.get(user_id)
        print(user.address)
        if not user:
            raise ValueError("No user found")
        return user