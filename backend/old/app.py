from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models import db # models.py からインポート
from config import DevelopmentConfig, ProductionConfig
from datetime import datetime
from flask_login import login_bp  # `flask_login.py` から Blueprint をインポート
from routes import routes_bp
import os


app = Flask(__name__)
CORS(app)  # フロントエンドと通信できるように CORS 設定
app.register_blueprint(login_bp)  # `/api/login` を有効化
app.config['JSON_AS_ASCII'] = False

# 環境変数 `FLASK_ENV` をチェックして設定を切り替え
env = os.environ.get("FLASK_ENV", "development")  # デフォルトは開発環境
if env == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

print(f"🚀 現在の環境: {env}")  # 環境確認のためログ出力

# ✅ Flask に DB を登録（重要！）
db.init_app(app)
app.register_blueprint(routes_bp)

# ✅ アプリのコンテキスト内でテーブルを作成（必要なら）
with app.app_context():
    db.create_all()

#@app.route("/")
#def index():
#    社員リスト = M_社員マスタ.query.all()
#    return render_template("index.html", 社員リスト=社員リスト)

if __name__ == "__main__":
    app.run(debug=True)