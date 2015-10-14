# DBバックアップ

```
heroku run python manage.py dumpdata app_name --format=json --indent=2 > app.json
```

ローカルにapp.jsonが出力される．

# DBリストア

```
heroku run python manage.py loaddata app.json
```

まずはじめにgitでjsonをcommit + pushしておく．ローカルからはリストアできないっぽい．
