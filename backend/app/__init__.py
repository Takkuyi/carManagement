import os
from flask import Flask
from flask_migrate import Migrate  # ← これが必要！
from .extensions import db, cors, login_manager
from .config import DevelopmentConfig, ProductionConfig
from .vehicle.models import Vehicle
from app.vehicle.routes import bp_vehicle
from app.Hluggage.routes import routes_bp as hluggage_bp
from app.Hluggage.models import CrateWeights, CourseGroups, Courses, Clients, LoadingData, LoadingMethods
from app.Hluggage import models as hluggage_models

migrate = Migrate()  # ← Flask-Migrate のインスタンス作成

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    # 環境変数から設定を切り替え
    env = os.environ.get("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    print(f"🚀 現在の環境: {env}")

    # Flask拡張の初期化
    db.init_app(app)
    cors.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  
    app.register_blueprint(bp_vehicle)

    # Blueprint登録
    from .auth.routes import login_bp
    from .etc.routes import routes_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(hluggage_bp, url_prefix="/hluggage")

    #with app.app_context():
    #    db.create_all()

    return app

import app.Hluggage.models