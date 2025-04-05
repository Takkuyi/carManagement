from flask import Blueprint, jsonify, request
from models import db, Mクレート重量マスタ, MコースGマスタ, Mコースマスタ, M取引先マスタ, M増便報告データ, Vehicles, MaintenanceAlerts, MaintenanceRecords, Documents, PartsReplacement

routes_bp = Blueprint("routes", __name__)

# ✅ 全データ取得（GET）
@routes_bp.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = Vehicles.query.all()
    return jsonify([{
        "id": v.id,
        "vehicle_number": v.vehicle_number,
        "license_plate": v.license_plate,
        "vehicle_type": v.vehicle_type,
        "manufacturer": v.manufacturer,
        "model": v.model,
        "year_manufactured": v.year_manufactured,
        "date_acquired": v.date_acquired.strftime("%Y-%m-%d") if v.date_acquired else None,
        "status": v.status,
        "capacity": str(v.capacity) if v.capacity else None,
        "notes": v.notes
    #} for v in vehicles])
    } for v in vehicles]), 200, {"Content-Type": "application/json; charset=utf-8"}

# ✅ 新規登録（POST）
@routes_bp.route("/vehicles", methods=["POST"])
def create_vehicle():
    data = request.json
    new_vehicle = Vehicles(
        vehicle_number=data["vehicle_number"],
        license_plate=data["license_plate"],
        vehicle_type=data["vehicle_type"],
        manufacturer=data["manufacturer"],
        model=data["model"],
        year_manufactured=data["year_manufactured"],
        date_acquired=data.get("date_acquired"),
        status=data["status"],
        capacity=data.get("capacity"),
        notes=data.get("notes")
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle created successfully!"}), 201

# ✅ データ更新（PUT）
@routes_bp.route("/vehicles/<int:id>", methods=["PUT"])
def update_vehicle(id):
    vehicle = Vehicles.query.get(id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    
    data = request.json
    vehicle.vehicle_number = data.get("vehicle_number", vehicle.vehicle_number)
    vehicle.license_plate = data.get("license_plate", vehicle.license_plate)
    vehicle.vehicle_type = data.get("vehicle_type", vehicle.vehicle_type)
    vehicle.manufacturer = data.get("manufacturer", vehicle.manufacturer)
    vehicle.model = data.get("model", vehicle.model)
    vehicle.year_manufactured = data.get("year_manufactured", vehicle.year_manufactured)
    vehicle.date_acquired = data.get("date_acquired", vehicle.date_acquired)
    vehicle.status = data.get("status", vehicle.status)
    vehicle.capacity = data.get("capacity", vehicle.capacity)
    vehicle.notes = data.get("notes", vehicle.notes)

    db.session.commit()
    return jsonify({"message": "Vehicle updated successfully!"})

# ✅ データ削除（DELETE）
@routes_bp.route("/vehicles/<int:id>", methods=["DELETE"])
def delete_vehicle(id):
    vehicle = Vehicles.query.get(id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"message": "Vehicle deleted successfully!"})

# ✅ MaintenanceAlertsデータ取得
@routes_bp.route("/maintenance_alerts", methods=["GET"])
def get_maintenance_alerts():
    alerts = MaintenanceAlerts.query.all()
    return jsonify([{
        "id": alert.id,
        "vehicle_id": alert.vehicle_id,
        "alert_type": alert.alert_type,
        "description": alert.description,
        "due_date": alert.due_date.strftime("%Y-%m-%d") if alert.due_date else None,
        "status": alert.status,
        "priority": alert.priority
    } for alert in alerts])

# ✅ MaintenanceRecordsデータ取得
@routes_bp.route("/maintenance_records", methods=["GET"])
def get_maintenance_records():
    records = MaintenanceRecords.query.all()
    return jsonify([{
        "id": record.id,
        "vehicle_id": record.vehicle_id,
        "maintenance_type": record.maintenance_type,
        "description": record.description,
        "maintenance_date": record.maintenance_date.strftime("%Y-%m-%d") if record.maintenance_date else None,
        "status": record.status,
        "completion_date": record.completion_date.strftime("%Y-%m-%d") if record.completion_date else None,
        "mileage": record.mileage,
        "cost": str(record.cost) if record.cost else None,
        "performed_by": record.performed_by,
        "vendor": record.vendor,
        "next_maintenance_date": record.next_maintenance_date.strftime("%Y-%m-%d") if record.next_maintenance_date else None,
        "notes": record.notes
    } for record in records])

# ✅ Documentsデータ取得
@routes_bp.route("/documents", methods=["GET"])
def get_documents():
    documents = Documents.query.all()
    return jsonify([{
        "id": doc.id,
        "document_type": doc.document_type,
        "title": doc.title,
        "file_path": doc.file_path,
        "vehicle_id": doc.vehicle_id,
        "maintenance_id": doc.maintenance_id,
        "uploaded_at": doc.uploaded_at.strftime("%Y-%m-%d %H:%M:%S") if doc.uploaded_at else None,
        "notes": doc.notes
    } for doc in documents])

# ✅ PartsReplacementデータ取得
@routes_bp.route("/parts_replacement", methods=["GET"])
def get_parts_replacement():
    parts = PartsReplacement.query.all()
    return jsonify([{
        "id": part.id,
        "maintenance_id": part.maintenance_id,
        "part_name": part.part_name,
        "quantity": part.quantity,
        "part_number": part.part_number,
        "cost_per_unit": str(part.cost_per_unit) if part.cost_per_unit else None,
        "total_cost": str(part.total_cost) if part.total_cost else None,
        "notes": part.notes
    } for part in parts])

