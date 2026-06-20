# AI-Powered Competitive Programming System

AI-Powered Competitive Programming System は、  
**問題分類 → テンプレート選択 → コード生成 → Docker 実行**  
という一連の流れを自動化する、Linux（Ubuntu / WSL2）ネイティブの AI 開発環境です。

このプロジェクトは、競技プログラミング問題を AI が理解し、  
最適なテンプレートを選択し、安定したコードを生成する  
“構造化コード生成 AI” を目指しています。

---

## 🚀 Features（特徴）

### ✔ 1. 問題分類 AI（Problem Classifier）
- 自然言語の問題文を解析し、問題タイプを自動推定  
- 累積和 / 条件分岐 / 配列処理 / 文字列処理 / 数学系 / 探索 / 一般 に分類

### ✔ 2. テンプレート管理システム（Template Engine）
- 問題タイプごとに最適化されたテンプレートを適用  
- [CODE] / [EXPLANATION] タグで構造を強制  
- コード生成の安定性が大幅に向上

### ✔ 3. コーディング AI（Coding Engine）
- テンプレートに基づき LLM がコードを生成  
- 計算量（Big-O）を必ず説明文に付与  
- コードブロックや閉じタグの混入を防止

### ✔ 4. Docker 実行環境
- 生成されたコードを安全に実行  
- ホスト環境を汚さない  
- Python 実行に対応（他言語は今後拡張）

---

## 🧱 System Architecture（システム構成）

Problem Text  
↓  
Problem Classifier  
↓  
Template Engine  
↓  
Coding AI  
↓  
Docker Execution  

---

## 📦 Requirements（必要環境）

- Ubuntu / WSL2  
- Python 3.12+  
- Docker  
- Ollama（ローカル LLM 推論エンジン）  
- Python 仮想環境（venv）

---

## 🔧 Setup（セットアップ手順）

### 1. Clone this repository
bash
git clone https://github.com/<yourname>/AI-Powered-apps.git
cd AI-Powered-apps

### 2. Create Python virtual environment
bash
python3 -m venv venv
source venv/bin/activate

### 3. Install Python dependencies
bash
pip install ollama streamlit

### 4. Install Ollama (Ubuntu)
bash
curl -fsSL https://ollama.com/install.sh | sh

### 5. Pull required models
bash
ollama pull llama3.1

### 6. Build Docker image
bash
docker build -t code-runner .

▶️ Run（実行方法）
bash
streamlit run app.py
AI が以下を自動で行います：

問題文の解析

問題タイプの分類

テンプレート選択

コード生成

Docker 実行

結果表示

📁 Directory Structure（ディレクトリ構成）
コード
AI-Powered-apps/
│
├── app.py                   # Web UI（Streamlit）
├── templates.py             # テンプレート管理システム
├── problem_classifier.py    # 問題分類AI
├── Dockerfile               # Docker 実行環境
├── README.md                # このファイル
└── .gitignore

🛑 .gitignore（重要）
コード
venv/
__pycache__/
.ollama/
*.log
.DS_Store

🗺 Roadmap（今後の予定）
[ ] LLM ベース問題分類器の導入

[ ] テンプレートの自動最適化

[ ] Rust / C++ / Go の実行環境対応

[ ] 自動修正 AI（Fix Engine）の再導入

[ ] Web UI の改善（テンプレート選択ログなど）

📜 License
MIT License
自由に利用・改変・商用利用できます。

👤 Author
トオル|FPxコーダー
Ubuntu / Docker / AI 自動化開発
競技プログラミング向け AI システム構築中
