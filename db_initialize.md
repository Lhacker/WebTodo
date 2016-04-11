```sh
$ pip install mysqlclient
```

create mysql user
```sql
$ mysql -u root -p

> create user 'django'@'localhost' identified by 'XXXXX';
> select User, Host, Password from mysql.user;
```

create database && grant
```sql
> create database todo character set utf8;
> grant all on todo.* to 'django'@'localhost';
> grant all on test_todo.* to 'django'@'localhost';
> \q
```

```sql
$ mysql -u django -p todo

> show tables;
> \q
```

