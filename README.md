# event_notification_bot

## Doer-org/idea

[おしゃべり定期通知Bot #24 ](https://github.com/Doer-org/idea/issues/24)

discordのイベント(もくもく会や定期LT会など)の通知をするbot

## Getting Started

docker起動
```
docker-compose up -d --build
```

pythonコンテナに入る
```
docker-compose exec python3 bash
```

コンテナ内で実行して, 問題ないか確認する
```
python main.py hello
```

```hello docker!``` と表示されたらok

コンテナから抜ける時は ```exit```コマンドを打ちましょう


## References
- [DockerとDocker ComposeでPythonの実行環境を作成する](https://zuma-lab.com/posts/docker-python-settings)
- [dockerで簡易にpython3の環境を作ってみる](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)
- [Pythonで実用Discord Bot(discordpy解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)
- [python-dotenvを使って環境変数を設定する)
- [discord.py Discord botユーザを作成し、トークンを取得する手順](https://cod-sushi.com/discord-py-token/)