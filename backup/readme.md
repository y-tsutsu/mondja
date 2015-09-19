# DBバックアップ

```
heroku run python manage.py dumpdata app_name --format=xml > app.xml
```

ローカルにapp.xmlが出力される．xmlの先頭に1行不要行が入っているので手動で削除する．

# DBリストア

```
heroku run python manage.py loaddata app.xml
```

まずはじめにgitでxmlをcommit + pushしておく．ローカルからはリストアできないっぽい．
