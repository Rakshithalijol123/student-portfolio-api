from .connection import (
    connect,
    create_database,
)
import bcrypt

from src.config import MONGODB_URL

client = connect(MONGODB_URL)
db = create_database(client=client, db_name="STUDENT-PORTFOLIO-DATABASE")


# --- Create your collections here ---
User = db["User"]

# Write functions which interact with database


def create_user(userData: dict) -> str:
    user = User.insert_one(userData)
    return str(user.inserted_id)


def get_user(username: str) -> str:
    user = User.find_one({"username": username})
    return str(user["password"])


def login(username: str, password: str) -> bool:
    try:
        hashed_password = get_user(username)
        print(hashed_password)
    except:
        return False
    password_status = bcrypt.checkpw(password.encode(
        'utf-8'), hashed_password.encode('utf-8'))
    print(password_status)
    if password_status == False:
        return False
    filter: dict(str) = {"username": username, "password": hashed_password}
    update_user: dict(str) = {"isActive": True}
    try:
        login_user = User.update_one(filter, {"$set": update_user})
        print(f"acknowledged = {login_user.acknowledged} ")
        if login_user.acknowledged:
            return True
        return False
    except:
        return None


def logout(email: str) -> bool:
    filter: dict(str) = {"email": email}
    update_user: dict(str) = {"isActive": False}
    try:
        logout_user = User.update_one(filter, {"$set": update_user})
        if logout_user.acknowledged:
            return True
        return False
    except:
        return False
