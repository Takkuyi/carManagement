import axios from 'axios';
import { Vehicle, MaintenanceRecord } from './types';

// APIのベースURL
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000/api';
const api = axios.create({ baseURL: API_URL });

// 車両関連API
export const vehicleApi = {
  // 全車両取得
  getAll: async (): Promise<Vehicle[]> => {
    const response = await api.get('/vehicles');
    return response.data;
  },

  // 特定車両取得
  getById: async (id: number | string): Promise<Vehicle> => {
    const response = await api.get(`/vehicles/${id}`);
    return response.data;
  },

  // 車両追加
  create: async (vehicle: Omit<Vehicle, 'id'>): Promise<Vehicle> => {
    const response = await api.post('/vehicles', vehicle);
    return response.data;
  },

  // 車両更新
  update: async (id: number | string, vehicle: Partial<Vehicle>): Promise<Vehicle> => {
    const response = await api.put(`/vehicles/${id}`, vehicle);
    return response.data;
  },

  // 車両削除
  delete: async (id: number | string): Promise<void> => {
    await api.delete(`/vehicles/${id}`);
  }
};

// 整備記録関連API
export const maintenanceApi = {
  // 全整備記録取得
  getAll: async (): Promise<MaintenanceRecord[]> => {
    const response = await api.get('/maintenance-records');
    return response.data;
  },

  // 車両ごとの整備記録取得
  getByVehicleId: async (vehicleId: number | string): Promise<MaintenanceRecord[]> => {
    const response = await api.get(`/vehicles/${vehicleId}/maintenance-records`);
    return response.data;
  },

  // 特定整備記録取得
  getById: async (id: number | string): Promise<MaintenanceRecord> => {
    const response = await api.get(`/maintenance-records/${id}`);
    return response.data;
  },

  // 整備記録追加
  create: async (record: Omit<MaintenanceRecord, 'id'>): Promise<MaintenanceRecord> => {
    const response = await api.post('/maintenance-records', record);
    return response.data;
  },

  // 整備記録更新
  update: async (id: number | string, record: Partial<MaintenanceRecord>): Promise<MaintenanceRecord> => {
    const response = await api.put(`/maintenance-records/${id}`, record);
    return response.data;
  },

  // 整備記録削除
  delete: async (id: number | string): Promise<void> => {
    await api.delete(`/maintenance-records/${id}`);
  }
};

export default {
  vehicle: vehicleApi,
  maintenance: maintenanceApi
};