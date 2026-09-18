# Project Z
## Python Development Environment

Python / VS Code / Git / GitHubを使った
Pythonプロジェクトの構築・管理方法を整理する。

## Contents

1. Python_VSCode_GitHub.md
2. Project_Setup.md
3. Virtual_Environment_and_Packages.md
4. Git_and_GitHub.md

## FAQ

・どのpythonを使っているのか確認する方法は？
A. where.exe python
として、Topに表示されるものがそのターミナルで使用しているPythonの位置です。

・venv内のライブラリ一覧を確認する方法は？
A. python -m pip list
とすることで、その仮想環境内にあるライブラリの一覧とその各バージョンもわかります。

・VScodeの拡張機能とは？ライブラリとの違いは？
A. 拡張機能を入れることで、

コードの色付け
補完
エラー検出
デバッグ
Pythonインタープリターの選択
仮想環境の検出
Jupyter Notebookの実行

など、VS CodeからPythonを使いやすくする機能を提供するが、Python本体などは本体のPCから仮想環境なりに持って行かないといけない。