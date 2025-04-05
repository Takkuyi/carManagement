from app.extensions import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(64), unique=True, nullable=False)  # 車両番号
    registration_number = db.Column(db.String(64))  # 登録番号
    chassis_number = db.Column(db.String(64))       # 車台番号
    vehicle_type = db.Column(db.String(64))         # 車両の種類
    car_type = db.Column(db.String(64))             # 自動車の種別
    usage = db.Column(db.String(64))                # 用途
    ownership = db.Column(db.String(64))            # 自家用事業用の別
    ownership_type = db.Column(db.String(64))       # 所有形態
    body_style = db.Column(db.String(64))           # 車体の形状
    car_name = db.Column(db.String(64))             # 車名
    model = db.Column(db.String(64))                # 型式
    engine_model = db.Column(db.String(64))         # 原動機の型式
    length = db.Column(db.Float)                    # 長さ
    width = db.Column(db.Float)                     # 幅
    height = db.Column(db.Float)                    # 高さ
    vehicle_weight = db.Column(db.Float)            # 車両重量
    gross_weight = db.Column(db.Float)              # 車両総重量
    max_load_capacity = db.Column(db.Float)         # 最大積載量
    max_load = db.Column(db.Float)                  # 最大積載量（別名が存在）
    seating_capacity = db.Column(db.Integer)        # 定員
    classification = db.Column(db.String(64))       # 車両区分（軽・普通・大型など）
    name = db.Column(db.String(64))                 # 所有者の氏名（または名称）
    gross_vehicle_weight = db.Column(db.Float)      # 車両総重量（電子車検証用）
    capacity = db.Column(db.Float)                  # 容量（電子車検証より）

    # ETC利用情報とのリレーションは外部キー制約なしで対応予定（必要に応じてJOINのみ）

    @staticmethod
    def from_csv_row(row):
        def to_float(val):
            try:
                return float(val)
            except (ValueError, TypeError):
                return None

        def to_int(val):
            try:
                return int(val)
            except (ValueError, TypeError):
                return None

        return Vehicle(
            vehicle_number=row.get("CarId"),
            registration_number=row.get("RegistrationNumber"),
            chassis_number=row.get("VehicleId"),
            vehicle_type=row.get("VehicleType"),
            car_type=row.get("Use"),
            usage=row.get("Usage"),
            ownership=row.get("OwnKind"),
            ownership_type=row.get("UseType"),
            body_style=row.get("BodyType"),
            car_name=row.get("CarName"),
            model=row.get("Model"),
            engine_model=row.get("EngineModel"),
            length=to_float(row.get("Length")),
            width=to_float(row.get("Width")),
            height=to_float(row.get("Height")),
            vehicle_weight=to_float(row.get("VehicleWeight")),
            gross_weight=to_float(row.get("TotalWeight")),
            max_load_capacity=to_float(row.get("MaxLoadCap")),
            max_load=to_float(row.get("MaxLoad")),
            seating_capacity=to_int(row.get("Capacity")),
            classification=row.get("CarKind"),
            name=row.get("UserName"),
            gross_vehicle_weight=to_float(row.get("GVWR")),
            capacity=to_float(row.get("Displacement"))
        )
