carManagement/
├── frontend/                      # Next.js用のディレクトリ 
│   ├── app                        
│   │   ├── page.tsx               # トップページ（ダッシュボード）
│   │   ├── layout.tsx             # メインレイアウト
│   │   ├── login                  
│   │   ├── maintenance            
│   │   ├── vehicles               
│   ├── components                 
│   ├── lib                        
│   ├── public                     
│   └── globals.css                # グローバルスタイル
│
├── backend/                       # Flask用のディレクトリ
│   ├── app                        # APIモジュール用のディレクトリ
│   │   ├── auth                   # 認証処理モジュール
│   │   ├── etc                    # ETCデータ管理用モジュール
│   │   ├── vehicle                # 車両データ管理用モジュール
