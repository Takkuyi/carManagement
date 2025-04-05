"use client";

import React, { useState } from 'react';

// ステータスと優先度の型定義
type StatusType = '未対応' | '対応中' | '完了';
type PriorityType = '高' | '中' | '低';

// カラーマップの型定義
interface ColorMap {
  [key: string]: string;
}

const EnhancedDashboard = () => {
  const [isSidebarCollapsed, setSidebarCollapsed] = useState(false);
  
  // データ定義
  const vehicleStatusData = [
    { name: '運行中', value: 18, color: '#4CAF50' },
    { name: '待機中', value: 4, color: '#2196F3' },
    { name: '整備中', value: 2, color: '#FFC107' }
  ];

  const recentAlerts = [
    { id: 1, vehicle: 'TRK-001', type: 'オイル交換', dueDate: '2025/4/15', priority: '高' as PriorityType, status: '未対応' as StatusType },
    { id: 2, vehicle: 'TRK-003', type: 'タイヤ交換', dueDate: '2025/4/20', priority: '中' as PriorityType, status: '対応中' as StatusType },
    { id: 3, vehicle: 'TRK-005', type: '車検', dueDate: '2025/5/10', priority: '高' as PriorityType, status: '未対応' as StatusType }
  ];

  const recentMaintenance = [
    { id: 1, date: '2025/3/10', vehicle: 'TRK-002', type: 'エンジンオイル交換', status: '完了' as StatusType, cost: 15000 },
    { id: 2, date: '2025/2/28', vehicle: 'TRK-004', type: 'ブレーキパッド交換', status: '完了' as StatusType, cost: 32000 },
    { id: 3, date: '2025/3/15', vehicle: 'TRK-001', type: 'エアフィルター交換', status: '完了' as StatusType, cost: 8000 }
  ];

  const toggleSidebar = () => {
    setSidebarCollapsed(!isSidebarCollapsed);
  };

  const getPriorityBadge = (priority: PriorityType) => {
    const colorMap: ColorMap = {
      '高': 'bg-red-100 text-red-800',
      '中': 'bg-yellow-100 text-yellow-800',
      '低': 'bg-blue-100 text-blue-800'
    };
    return <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${colorMap[priority]}`}>{priority}</span>;
  };

  const getStatusBadge = (status: StatusType) => {
    const colorMap: ColorMap = {
      '未対応': 'bg-red-100 text-red-800',
      '対応中': 'bg-yellow-100 text-yellow-800',
      '完了': 'bg-green-100 text-green-800'
    };
    return <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${colorMap[status]}`}>{status}</span>;
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* メインコンテンツエリア */}
      <div className="flex-1 overflow-auto">
        <main className="max-w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
          {/* 統計カード */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
            <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-blue-500">
              <div className="flex items-center">
                <div className="flex-shrink-0 bg-blue-100 p-3 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0" />
                  </svg>
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500 truncate">総車両数</p>
                  <p className="text-2xl font-semibold text-gray-900">24台</p>
                </div>
              </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-green-500">
              <div className="flex items-center">
                <div className="flex-shrink-0 bg-green-100 p-3 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
                  </svg>
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500 truncate">今月の配送数</p>
                  <p className="text-2xl font-semibold text-gray-900">1,248件</p>
                </div>
              </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-yellow-500">
              <div className="flex items-center">
                <div className="flex-shrink-0 bg-yellow-100 p-3 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500 truncate">今月の燃料費</p>
                  <p className="text-2xl font-semibold text-gray-900">¥845,200</p>
                </div>
              </div>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-sm border-l-4 border-red-500">
              <div className="flex items-center">
                <div className="flex-shrink-0 bg-red-100 p-3 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div className="ml-5">
                  <p className="text-sm font-medium text-gray-500 truncate">整備アラート</p>
                  <p className="text-2xl font-semibold text-gray-900">5件</p>
                </div>
              </div>
            </div>
          </div>

          {/* グラフプレースホルダー */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
            <div className="lg:col-span-2 bg-white p-4 rounded-lg shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold">月間運行実績</h3>
                <div className="flex space-x-2">
                  <select className="border rounded p-1 text-sm text-gray-600">
                    <option>2025年</option>
                    <option>2024年</option>
                  </select>
                  <button className="bg-blue-50 hover:bg-blue-100 text-blue-600 font-semibold text-xs px-3 py-1 rounded">
                    詳細を表示
                  </button>
                </div>
              </div>
              <div className="h-80 bg-gray-50 flex items-center justify-center">
                <div className="text-center">
                  <div className="text-gray-400">ここにグラフが表示されます</div>
                  <div className="mt-2 text-sm text-gray-500">（recharts ライブラリが必要です）</div>
                </div>
              </div>
            </div>

            <div className="bg-white p-4 rounded-lg shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold">車両稼働状況</h3>
                <div>
                  <p className="text-sm text-gray-500">総車両数: 24台</p>
                </div>
              </div>
              <div className="h-80 bg-gray-50 flex flex-col items-center justify-center">
                {/* 簡易円グラフの代わり */}
                <div className="flex items-center space-x-2 mb-4">
                  <div className="w-32 h-32 rounded-full border-8 border-gray-200 relative">
                    <div className="absolute inset-0 rounded-full border-8 border-t-green-500 border-r-blue-500 border-b-yellow-500 border-l-green-500 transform -rotate-45"></div>
                  </div>
                </div>
                <div className="flex space-x-4">
                  {vehicleStatusData.map((item, index) => (
                    <div key={index} className="flex items-center">
                      <div className="w-4 h-4 rounded-full mr-1" style={{ backgroundColor: item.color }}></div>
                      <span className="text-sm">{item.name}: {item.value}台</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* 車両燃料消費グラフ */}
          <div className="mb-6">
            <div className="bg-white p-4 rounded-lg shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold">車両別燃料消費量 (L) - 今月</h3>
                <button className="bg-blue-50 hover:bg-blue-100 text-blue-600 font-semibold text-xs px-3 py-1 rounded">
                  全期間表示
                </button>
              </div>
              <div className="h-64 bg-gray-50 flex items-center justify-center">
                <div className="text-center">
                  <div className="text-gray-400">ここに棒グラフが表示されます</div>
                  <div className="mt-2 text-sm text-gray-500">（recharts ライブラリが必要です）</div>
                </div>
              </div>
            </div>
          </div>

          {/* アラートと最近の整備 */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="bg-white p-4 rounded-lg shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold">整備アラート</h3>
                <button className="text-sm text-blue-600 hover:text-blue-800">すべて表示</button>
              </div>
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">車両</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">整備内容</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">期日</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">優先度</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">状態</th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {recentAlerts.map(alert => (
                      <tr key={alert.id}>
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{alert.vehicle}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{alert.type}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{alert.dueDate}</td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          {getPriorityBadge(alert.priority)}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          {getStatusBadge(alert.status)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            <div className="bg-white p-4 rounded-lg shadow-sm">
              <div className="flex justify-between items-center mb-4">
                <h3 className="text-lg font-semibold">最近の整備記録</h3>
                <button className="text-sm text-blue-600 hover:text-blue-800">すべて表示</button>
              </div>
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">日付</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">車両</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">整備内容</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">状態</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">費用</th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {recentMaintenance.map(record => (
                      <tr key={record.id}>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{record.date}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{record.vehicle}</td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{record.type}</td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          {getStatusBadge(record.status)}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">¥{record.cost.toLocaleString()}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default EnhancedDashboard;