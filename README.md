# claude-code-project

## 概要

Claude Code を試すための最小構成の Python スタータープロジェクトです。
シンプルな関数とテストだけを含んでいます。

## 構成

```
.
├── README.md          # このファイル
├── .gitignore         # Git の除外設定
├── conftest.py        # pytest 用（リポジトリルートを import パスに追加）
├── src/
│   └── main.py        # greet() 関数とエントリポイント
└── tests/
    └── test_main.py   # greet() のテスト
```

## 使い方

プログラムの実行（リポジトリルートで）:

```bash
python src/main.py
# => Hello, world!
```

テストの実行（pytest が必要です）:

```bash
pip install pytest
pytest
```
