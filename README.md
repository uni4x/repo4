# AIニュース集約アプリ

## 概要
AIニュース集約アプリは、Djangoを使用して構築されたWebアプリケーションで、さまざまなソースからAI関連のニュース記事をスクレイピングし、ユーザーフレンドリーなインターフェースで表示します。ユーザーは特定の記事を検索し、各記事の詳細情報を表示することができます。

## 機能
- VentureBeat、ScienceDaily、AI NewsからAIニュース記事をスクレイピング
- タイトル、概要、公開日を表示
- キーワードで記事を検索する機能
- 記事の詳細情報と元のソースへのリンクを表示
- 記事のページネーション（ページ分割）機能
- ユーザー認証（登録およびログイン）
- 記事をブックマークし、ユーザープロフィールページに表示
- 記事へのコメント機能（編集および削除も可能）
- Googleソーシャルログイン統合

## インストール

### 必要条件
- Python 3.6以上
- Django 3.0以上
- Django REST Framework

### セットアップ
1. リポジトリをクローンする
    ```bash
    git clone https://github.com/yourusername/ai-news-aggregator.git
    cd ai-news-aggregator
    ```

2. 仮想環境を作成してアクティブにする
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
    ```

3. 依存関係をインストールする
    ```bash
    pip install -r requirements.txt
    ```

4. データベースをセットアップする
    ```bash
    python manage.py migrate
    ```

5. 管理サイトにアクセスするためのスーパーユーザーを作成する
    ```bash
    python manage.py createsuperuser
    ```

6. ソーシャル認証を設定する：
   - Google Developer Consoleにアクセスし、新しいプロジェクトを作成し、OAuth 2.0のクレデンシャル（クライアントIDとクライアントシークレット）を取得します。
   - これらのクレデンシャルを`settings.py`ファイルに追加します。
    ```python
    SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'SCOPE': [
                'profile',
                'email',
            ],
            'AUTH_PARAMS': {
                'access_type': 'online',
            },
            'OAUTH_PKCE_ENABLED': True,
            'APP': {
                'client_id': 'YOUR_CLIENT_ID',
                'secret': 'YOUR_CLIENT_SECRET',
                'key': ''
            }
        }
    }
    ```

7. 開発サーバーを起動する
    ```bash
    python manage.py runserver
    ```

8. アプリケーションにアクセスする `http://127.0.0.1:8000/`

## 使用方法

### ニュース記事のスクレイピング
複数のソースからAIニュース記事をスクレイピングするには、次のコマンドを実行します：
    ```bash
    python manage.py scrape_all_news
    ```

### 記事のアクセス
- 記事一覧を見るには、`http://127.0.0.1:8000/news/articles/`に移動します。
- 検索バーを使用してキーワードで記事を検索できます。
- 記事のタイトルをクリックして、詳細情報と元のソースにアクセスできます。

### ユーザー機能
- 登録、ログイン、アカウント管理ができます。
- 記事をブックマークし、プロフィールページで表示できます。
- 記事にコメントを追加し、編集、削除できます。

### 管理サイト
- 管理サイトにアクセスするには、`http://127.0.0.1:8000/admin/`に移動し、記事、コメント、ユーザーを管理します。

## コントリビューション

コントリビューションは大歓迎です！このリポジトリをフォークし、新機能、拡張機能、バグ修正のためにプルリクエストを送信してください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細についてはLICENSEファイルを参照してください。

## お問い合わせ

ご質問やフィードバックがありましたら、your-email@example.comまでご連絡ください。

### 追加情報

- これはポートフォリオです。