# import_etc_data.py
from app import create_app
from app.etc.csv_import import import_etc_csv

app = create_app()

with app.app_context():
    import_etc_csv("uploads_etc_data/202504031446.csv")  # CSVのパス
