"use client";

import React, { useState } from 'react';

const MenuScreen = () => {
  const [activeMenu, setActiveMenu] = useState('dashboard');

  // メニュー項目
  const menuItems = [
    { id: 'dashboard', name: 'ダッシュボード', icon: '📊' },
    { id: 'vehicles', name: '車両管理', icon: '🚚' },
    { id: 'maintenance', name: '整備記録', icon: '🔧' },
    { id: 'drivers', name: 'ドライバー管理', icon: '👤' },
    { id: 'reports', name: 'レポート', icon: '📄' },
    { id: 'settings', name: 'システム設定', icon: '⚙️' },
  ];

  // ダッシュボードコンテンツ
  const renderDashboard = () => (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">ダッシュボード</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 bg-blue-100 rounded-lg">
          <h3 className="font-medium">稼働中の車両</h3>
          <p className="text-2xl font-bold">12 / 15</p>
        </div>
        <div className="p-4 bg-yellow-100 rounded-lg">
          <h3 className="font-medium">整備中の車両</h3>
          <p className="text-2xl font-bold">2</p>
        </div>
        <div className="p-4 bg-green-100 rounded-lg">
          <h3 className="font-medium">今月の走行距離</h3>
          <p className="text-2xl font-bold">12,345 km</p>
        </div>
      </div>
      
      <div className="p-4 bg-white rounded-lg shadow">
        <h3 className="font-medium mb-2">今後の整備予定</h3>
        <table className="min-w-full">
          <thead>
            <tr className="border-b">
              <th className="text-left py-2">車両番号</th>
              <th className="text-left py-2">整備内容</th>
              <th className="text-left py-2">予定日</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b">
              <td className="py-2">品川 100あ 1234</td>
              <td className="py-2">定期点検</td>
              <td className="py-2">2025/03/10</td>
            </tr>
            <tr className="border-b">
              <td className="py-2">品川 200い 5678</td>
              <td className="py-2">オイル交換</td>
              <td className="py-2">2025/03/15</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );

  // 車両管理コンテンツ
  const renderVehicles = () => (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold">車両管理</h2>
        <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
          新規車両登録
        </button>
      </div>
      
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                車両番号
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                車種
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                メーカー
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                ステータス
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                操作
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {[1, 2, 3].map((item) => (
              <tr key={item} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap">
                  品川 {100 * item}あ {1234 + item}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {item === 1 ? '2トントラック' : item === 2 ? '4トントラック' : '軽トラック'}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {item === 1 ? 'いすゞ' : item === 2 ? '日野' : 'スズキ'}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full 
                    ${item === 2 ? 'bg-yellow-100 text-yellow-800' : 'bg-green-100 text-green-800'}`}>
                    {item === 2 ? '整備中' : '稼働中'}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <button className="text-blue-600 hover:text-blue-900 mr-3">詳細</button>
                  <button className="text-blue-600 hover:text-blue-900">修理記録</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );

  const renderContent = () => {
    switch(activeMenu) {
      case 'dashboard':
        return renderDashboard();
      case 'vehicles':
        return renderVehicles();
      default:
        return <div className="p-4">コンテンツは準備中です</div>;
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* サイドバーメニュー */}
      <div className="w-64 bg-gray-800">
        <div className="p-4">
          <h1 className="text-white text-xl font-bold">卓ちゃんシステム</h1>
        </div>
        <nav className="mt-5">
          <ul>
            {menuItems.map((item) => (
              <li key={item.id}>
                <button
                  className={`w-full flex items-center px-4 py-3 text-sm ${
                    activeMenu === item.id 
                      ? 'bg-gray-900 text-white' 
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                  }`}
                  onClick={() => setActiveMenu(item.id)}
                >
                  <span className="mr-3">{item.icon}</span>
                  {item.name}
                </button>
              </li>
            ))}
          </ul>
        </nav>
        <div className="absolute bottom-0 w-64 px-4 py-3 bg-gray-800 border-t border-gray-700">
          <div className="flex items-center">
            <div className="flex-shrink-0 h-8 w-8 rounded-full bg-gray-600 flex items-center justify-center text-white">
              👤
            </div>
            <div className="ml-3">
              <p className="text-sm font-medium text-white">管理者</p>
              <button className="text-xs text-gray-300 hover:text-white">ログアウト</button>
            </div>
          </div>
        </div>
      </div>
      
      {/* メインコンテンツエリア */}
      <div className="flex-1 overflow-auto">
        <header className="bg-white shadow">
          <div className="px-4 py-4 sm:px-6 lg:px-8">
            <h2 className="text-lg font-semibold text-gray-900">
              {menuItems.find(item => item.id === activeMenu)?.name || ''}
            </h2>
          </div>
        </header>
        <main className="p-6">
          {renderContent()}
        </main>
      </div>
    </div>
  );
};

export default MenuScreen;