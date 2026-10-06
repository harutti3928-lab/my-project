# Setup

この環境における開発環境のセットアップ・確認方法をまとめる。

基本的には、

- **VS Code**
- **Python**
- **venv**
- **pip**
- **Git**
- **GitHub**

を使う。

---

## 0. VS Code・フォルダ・仮想環境

<details>
<summary><b>VS Codeで開くフォルダは？</b></summary>

基本的には、

```text
C:\dev\my-project
```

をVS Codeで開いて作業する。

ターミナルを開いたときも、

```powershell
PS C:\dev\my-project>
```

となっているのが基本。

</details>

<details>
<summary><b>my-project のフォルダ構成は？</b></summary>

```text
my-project/
├── .venv/
├── docs/
├── Project_A~Z/
├── matsuo-lab/
├── README.md
├── .gitignore
└── requirements.txt
```

主な役割は以下。

- **`.venv/`**  
  この `my-project` 専用のPython仮想環境。

- **`docs/`**  
  Setupなどのドキュメントを保存する。

- **`Project_A~Z/`**  
  機械学習などの各プロジェクト。

- **`matsuo-lab/`**  
  松尾研関連のコード・課題など。

- **`README.md`**  
  プロジェクト全体の説明。

- **`.gitignore`**  
  Gitで管理しないファイルを指定する。

- **`requirements.txt`**  
  Pythonパッケージとそのバージョンを記録する。

> **重要**
>
> `.venv` は基本的に直接編集しない。  
> `pip` を使ってパッケージをインストールすると、自動的に中身が変更される。

</details>

---

# 1. Python仮想環境

<details>
<summary><b>現在の仮想環境がどの.venvをアクティベートしているのかを確認するには？</b></summary>

PowerShellで、

```powershell
$env:VIRTUAL_ENV
```

を実行する。

### 成功例

```text
C:\dev\my-project\.venv
```

と表示されれば、この仮想環境が現在アクティベートされている。

また、ターミナルの左側に `(.venv)` が表示されることも目印になる。

</details>

<details>
<summary><b>Pythonの場所とバージョンを確認するには？</b></summary>

### Pythonの場所

```powershell
where.exe python
```

### 出力例

```text
C:\dev\my-project\.venv\Scripts\python.exe
C:\Users\harut\AppData\Local\Programs\Python\Python312\python.exe
```

一番上に表示されたパスのpythonが基本的には `python` コマンドで呼ばれて使われている。

### Pythonのバージョン

```powershell
python --version
```

### 出力例

```text
Python 3.12.10
```

</details>


<details>
<summary><b>pipの場所とバージョンを確認するには？</b></summary>

```powershell
python -m pip --version
```

### 出力例

```text
pip 26.2.1 from C:\dev\my-project\.venv\Lib\site-packages\pip (python 3.12)
```

場所とバージョンを一気に確認できる。

</details>


<details>
<summary><b>pipの基本的な使い方は？</b></summary>

基本的には、

```powershell
python -m pip
```

という形で使う。こうすることで、**現在使用しているPythonに対応したpipを確実に使える。**

### パッケージをインストール

```powershell
python -m pip install numpy matplotlib pandas
```

### インストール済みパッケージを確認

```powershell
python -m pip list
```

### 特定のパッケージを確認

```powershell
python -m pip show numpy
```

### アップデート

```powershell
python -m pip install --upgrade numpy
```

### アンインストール

```powershell
python -m pip uninstall numpy
```

### requirements.txt に現在の環境を保存

```powershell
python -m pip freeze > requirements.txt
```

### requirements.txt から一括インストール

```powershell
python -m pip install -r requirements.txt
```

</details>


<details>
<summary><b>VS Codeでターミナルを開くと .venv が自動でActivateされるのはなぜ？</b></summary>

VS CodeのPython拡張機能が、

> このプロジェクトではどのPythonを使うか

を管理している。

確認するには、

```text
Ctrl + Shift + P
```

を押して、

```text
Python: Select Interpreter
```

を検索する。

例えば、

```text
Python 3.12.10 ('.venv': venv)
```

のようなInterpreterが選択されていればよい。

実体は、

```text
C:\dev\my-project\.venv\Scripts\python.exe
```

となる。

---

VS Codeの設定には、

```text
Python › Terminal: Activate Environment
```

という項目がある。

これが有効なら、新しくターミナルを開いたときにVS Codeが自動的に `.venv` をActivateする。

大まかな流れは、

```text
my-project をVS Codeで開く
        ↓
.venv のPythonをInterpreterとして選択
        ↓
VS Codeで新しいターミナルを開く
        ↓
.venv が自動でActivateされる
        ↓
(.venv) PS C:\dev\my-project>
```

となる。

</details>

---

# 2. GitとGitHub

<details>
<summary><b>Gitがインストールされているか・どこにあるか確認するには？</b></summary>

### バージョン確認

```powershell
git --version
```

### 出力例

```text
git version 2.x.x.windows.x
```

Git本体の場所は、

```powershell
where.exe git
```

で確認できる。

### 出力例

```text
C:\Program Files\Git\cmd\git.exe
```

</details>

<details>
<summary><b>Gitのユーザー情報を確認するには？</b></summary>

```powershell
git config --global user.name
```

```powershell
git config --global user.email
```

まとめて確認するなら、

```powershell
git config --global --list
```

例えば、

```text
user.name=xxxxx
user.email=xxxxx@example.com
```

などが表示される。

> **注意**
>
> これはGitのコミットに記録される名前・メールアドレス。
>
> 必ずしも「現在ログインしているGitHubアカウント」と完全に同じ意味ではない。

</details>


<details>
<summary><b>GitHubとの接続先を確認するには？</b></summary>

```powershell
git remote -v
```

### 出力例

```text
origin  https://github.com/USERNAME/my-project.git (fetch)
origin  https://github.com/USERNAME/my-project.git (push)
```

これで、

```text
USERNAME/my-project
```

というGitHubリポジトリにつながっていることが分かる。

`origin` は、

> このローカルGitリポジトリの主な接続先

につけられる一般的な名前。

</details>

<details>
<summary><b>GitHubの認証アカウントを確認するには？</b></summary>

GitHub CLIを使っている場合は、

```powershell
gh auth status
```

で確認できる。

もし、

```text
gh: The term 'gh' is not recognized...
```

などと表示された場合は、GitHub CLIを使っていない可能性がある。

GitHubとの認証には、

- GitHub CLI
- Git Credential Manager
- SSH

など複数の方法がある。

そのため、

```powershell
git config user.name
```

だけでは、GitHubにログインしているアカウントを完全には判断できない。

</details>

<details>
<summary><b>変更されたファイルを確認するには？</b></summary>

```powershell
git status
```

これはGitで最も頻繁に使うコマンドの1つ。

例えば、

```text
modified: Project_A/A1_linear_regression.ipynb
```

と表示されたら、

> 前回のコミット以降、このファイルが変更された

という意味。

何か分からなくなったら、まず

```powershell
git status
```

を実行する。

</details>


<details>
<summary><b>変更をGitHubに保存する基本的な流れは？</b></summary>

基本的には、

```text
編集
 ↓
git status
 ↓
git add
 ↓
git commit
 ↓
git push
```

という流れ。

---

### ① 状態確認

```powershell
git status
```

---

### ② 変更をStageする

すべての変更を対象にする場合、

```powershell
git add .
```

特定のファイルだけなら、

```powershell
git add README.md
```

---

### ③ Commitする

```powershell
git commit -m "Update README"
```

Commitとは、

> この時点の変更内容をGitの履歴として保存する

こと。

---

### ④ GitHubにPushする

```powershell
git push
```

これでローカルのCommitがGitHubにも反映される。

---

### 基本セット

```powershell
git status

git add .

git commit -m "変更内容"

git push
```

</details>


<details>
<summary><b>GitHubの変更をローカルに持ってくるには？</b></summary>

```powershell
git pull
```

を使う。

基本的には、

```text
GitHub
   ↓
git pull
   ↓
自分のPC
```

という方向。

逆に、

```text
自分のPC
   ↓
git push
   ↓
GitHub
```

となる。

したがって、

```text
pull = GitHub → PC
push = PC → GitHub
```

と覚える。

</details>

---

# 3. よく使う確認コマンド

## Python

```powershell
$env:VIRTUAL_ENV
python --version
python -c "import sys; print(sys.executable)"
python -m pip --version
python -m pip list
```

## Git

```powershell
git --version
git status
git remote -v
git config --global user.name
git config --global user.email
```

## GitHub

```powershell
git remote -v
gh auth status
```

---

# 4. トラブルが起きたら

まず以下を確認する。

```powershell
pwd
```

```powershell
$env:VIRTUAL_ENV
```

```powershell
python -c "import sys; print(sys.executable)"
```

```powershell
python -m pip --version
```

```powershell
git status
```

これで、

1. **今どこのフォルダにいるか**
2. **どの仮想環境にいるか**
3. **どのPythonを使っているか**
4. **どのpipを使っているか**
5. **Gitがどの状態か**

を確認する。