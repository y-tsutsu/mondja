# DBバックアップ

```
heroku run python manage.py dumpdata app_name --format=json --indent=2 > app_name.json
```

ローカルにapp.jsonが出力される．

# DBリストア

```
heroku run python manage.py loaddata app.json
```

まずはじめにgitでjsonをcommit + pushしておく．ローカルからはリストアできないっぽい．

# サーバー側でdump

```
https://domain-name/dumpdata/app-name/
```

上記にブラウザからアクセスするとjsonがダウンロードできる．
