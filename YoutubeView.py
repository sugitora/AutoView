import os
from dotenv import load_dotenv
import webbrowser

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からURLを取得
url = os.getenv('MY_WEBSITE_URL')

# URLが設定されている場合、デフォルトのウェブブラウザで開く
if url:
    webbrowser.open(url)
else:
    print("URLが.envファイルに設定されていません。")