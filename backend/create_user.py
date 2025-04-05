from app import create_app
from app.extensions import db
from app.auth.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    username = "testuser"
    password = "testpass"
    hashed_pw = generate_password_hash(password)

    # すでに同名ユーザーがいたらスキップ
    if not User.query.filter_by(username=username).first():
        user = User(username=username, password_hash=hashed_pw)
        db.session.add(user)
        db.session.commit()
        print(f"✅ ユーザー '{username}' を作成しました")
    else:
        print(f"⚠️ ユーザー '{username}' はすでに存在しています")
