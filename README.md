# AI-Powered Competitive Programming System

AI-Powered Competitive Programming System は、  
**問題生成AI → テストケース生成AI → コーディングAI → 自動修正AI → Docker 実行**  
という一連の流れを自動化する、Linux（Ubuntu / WSL2）ネイティブの AI 開発環境です。

このプロジェクトは、競技プログラミング問題を AI が自動生成し、  
テストケースを作成し、コードを生成し、実行し、必要に応じて修正する  
“育つコーディング AI” を目指しています。

---

## 🚀 Features（特徴）

### ✔ 1. 問題生成 AI（Problem Generator）
- 競技プログラミング形式の問題文を自動生成  
- 入力形式 / 出力形式 / 制約 / サンプルを含む

### ✔ 2. テストケース生成 AI（Testcase Generator）
- 問題文を解析し、複数のテストケースを自動生成  
- エッジケースも考慮

### ✔ 3. コーディング AI（Coding Engine）
- 問題文から最適なアルゴリズムを推論  
- Python コードを生成  
- 計算量（Big-O）をコメントで説明

### ✔ 4. 自動修正 AI（Fix Engine）
- Docker 実行時のエラーを解析  
- コードを自動修正し再実行

### ✔ 5. Docker 実行環境
- 生成されたコードを安全に実行  
- ホスト環境を汚さない

---

## 🧱 System Architecture（システム構成）

Problem Generator
↓
Testcase Generator
↓
Coding AI
↓
Docker Execution
↓
Fix Engine (Error → 修正 → 再実行)


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

	```bash
	git clone https://github.com/<yourname>/AI-Powered-apps.git
	cd AI-Powered-apps

### 2. Create Python virtual environment
	```bash
	python3 -m venv venv
	source venv/bin/activate

### 3. Install Python dependencies
	```bash
	pip install ollama

### 4. Install Ollama (Ubuntu)
	```bash
	curl -fsSL https://ollama.com/install.sh | sh

### 5. Pull required models
	```bash
	ollama pull llama3.1
	ollama pull mistral
	ollama pull codellama

### 6. Build Docker image
	```bash
	docker build -t code-runner .

### ▶️ Run（実行方法）
	```bash
	source venv/bin/activate
	python3 run_code.py

	AI が以下を自動で行います：

	問題文の生成（または外部ファイルから読み込み）

	テストケース生成

	コード生成

	Docker で実行

	エラーがあれば修正

	再実行

### 📁 Directory Structure（ディレクトリ構成）

AI-Powered-apps/
│
├── run_code.py              # メイン実行ファイル
├── run.py                   # 補助スクリプト
├── code.py                  # AI が生成するコードの保存先
├── testcase_generator.py    # テストケース生成AI
├── problem_generator.py     # 問題生成AI
├── Dockerfile               # Docker 実行環境
├── README.md                # このファイル
└── .gitignore               # venv / .ollama / cache を除外

### 🛑 .gitignore（重要）
	venv/
	__pycache__/
	.ollama/
	*.log
	.DS_Store


### 🗺 Roadmap（今後の予定）
	[ ] 難易度別問題生成（Easy / Medium / Hard）

	[ ] 自動評価スコアリング

	[ ] Web UI 化

	[ ] AI 同士の自己対話によるコード改善

	[ ] Rust / C++ など他言語対応

### 📜 License
	MIT License
	自由に利用・改変・商用利用できます。

### 👤 Author
	t.s

	Ubuntu / Docker / AI 自動化開発

	競技プログラミング向け AI システム構築中