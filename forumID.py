import requests
import json

with open("token.txt", "r") as f:
    token = f.read()


# Zoho OAuthトークンとスコープIDを設定します
oauth_token = token
scope_id = 536351000000002008

# ネットワーク内の最近のフォーラム投稿を取得するAPIのURL
url = f'https://connect.zoho.com/pulse/api/recentBlogs?scopeID={scope_id}&pageIndex=1&limit=1'

# Authorizationヘッダーを設定します
headers = {
    'Authorization': f'Zoho-oauthtoken {oauth_token}',
}

# APIリクエストを発行します
response = requests.get(url, headers=headers)

# レスポンスが成功した場合
if response.status_code == 200:
    # レスポンスデータをJSON形式で取得します
    data = json.loads(response.text)

    # フォーラムのIDを取得します
    forum_id = data['recentBlogs']['blogs'][0]['id']

    # フォーラムのIDを表示します
    print(f'Forum ID: {forum_id}')

else:
    print(f'Request failed with status code {response.status_code}')
