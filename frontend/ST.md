fronend/
├── app/
│   ├── layout.tsx                 # メインレイアウト
│   ├── page.tsx                   # トップページ（ダッシュボード）
│   ├── vehicles/                  # 車両関連ページ
│   │   ├── page.tsx               # 車両一覧ページ
│   │   ├── [id]/                  # 動的ルーティング
│   │   │   ├── page.tsx           # 車両詳細ページ
│   │   │   └── edit/
│   │   │       └── page.tsx       # 車両編集ページ
│   │   └── new/
│   │       └── page.tsx           # 新規車両登録ページ
│   ├── maintenance/               # 整備関連ページ
│   │   ├── page.tsx               # 整備記録一覧ページ
│   │   ├── [id]/                  # 動的ルーティング
│   │   │   ├── page.tsx           # 整備詳細ページ
│   │   │   └── edit/
│   │   │       └── page.tsx       # 整備編集ページ
│   │   └── new/
│   │       └── page.tsx           # 新規整備記録登録ページ
│   └── globals.css                # グローバルスタイル
├── components/                    # 共通コンポーネント
│   ├── ui/                        # UI共通コンポーネント
│   │   ├── Navbar.tsx             # ナビゲーションバー
│   │   └── Footer.tsx             # フッター
│   ├── dashboard/                 # ダッシュボード関連コンポーネント
│   │   ├── StatCard.tsx           # 統計情報カード
│   │   └── MaintenanceAlert.tsx   # 整備アラート
│   ├── vehicles/                  # 車両関連コンポーネント
│   │   ├── VehicleList.tsx        # 車両一覧テーブル
│   │   ├── VehicleForm.tsx        # 車両登録/編集フォーム
│   │   └── VehicleDetail.tsx      # 車両詳細表示
│   └── maintenance/               # 整備関連コンポーネント
│       ├── MaintenanceList.tsx    # 整備記録一覧テーブル
│       ├── MaintenanceForm.tsx    # 整備記録登録/編集フォーム
│       └── MaintenanceDetail.tsx  # 整備記録詳細表示
├── lib/                           # ユーティリティ関数など
│   ├── api.ts                     # API通信用関数
│   └── types.ts                   # 型定義
├── public/                        # 静的ファイル
│   └── ...
├── next.config.js                 # Next.js設定
├── package.json
└── tsconfig.json