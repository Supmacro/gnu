## Usage
```
rpm -evh mariadb-libs-5.5.56-2.el7.x86_64 --nodeps
rpm -ivh mysql-8.0.23...

mysqld --initialize
chown mysql:mysql /var/lib/mysql -R
systemctl start mysqld
systemctl status mysqld

////
mysql> alter user "root"@"localhost" identified by "password";
mysql> create user 'root'@'%' identified with mysql_native_password by 'password';
mysql> grant all privileges on *.* to 'root'@'%' with grant option;
```

