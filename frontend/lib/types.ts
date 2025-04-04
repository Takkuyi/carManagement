export type VehicleStatus = '運行中' | '整備中' | '待機中' | '廃車';

export interface Vehicle {
  id: number;
  vehicle_number: string;
  license_plate: string;
  vehicle_type: string;
  manufacturer: string;
  model: string;
  year_manufactured: number;
  date_acquired: string;
  capacity?: number;
  status: VehicleStatus;
  notes?: string;
  created_at?: string;
  updated_at?: string;
}

export type MaintenanceType = '定期点検' | '故障修理' | 'オイル交換' | 'タイヤ交換' | 'その他';
export type MaintenanceStatus = '計画中' | '進行中' | '完了' | 'キャンセル';

export interface MaintenanceRecord {
  id: number;
  vehicle_id: number;
  maintenance_type: MaintenanceType;
  description: string;
  maintenance_date: string;
  completion_date?: string;
  mileage?: number;
  cost?: number;
  performed_by?: string;
  vendor?: string;
  status: MaintenanceStatus;
  next_maintenance_date?: string;
  notes?: string;
  created_at?: string;
  updated_at?: string;
  parts?: PartReplacement[];
}

export interface PartReplacement {
  id: number;
  maintenance_id: number;
  part_name: string;
  part_number?: string;
  quantity: number;
  cost_per_unit?: number;
  total_cost?: number;
  notes?: string;
  created_at?: string;
}

export type AlertStatus = '未対応' | '対応中' | '完了';
export type AlertPriority = '低' | '中' | '高';

export interface MaintenanceAlert {
  id: number;
  vehicle_id: number;
  alert_type: string;
  description: string;
  due_date: string;
  status: AlertStatus;
  priority: AlertPriority;
  created_at?: string;
  updated_at?: string;
  vehicle?: Vehicle;
}

export interface Document {
  id: number;
  vehicle_id?: number;
  maintenance_id?: number;
  document_type: string;
  title: string;
  file_path: string;
  uploaded_at?: string;
  notes?: string;
}