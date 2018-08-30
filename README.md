# landing_page
使用flask搭建的 landing page系统

### 安装环境
```
pip3 install -r requirements.txt
```

### 初始化数据库

```
python3 tools/init.py
```

### 运行
```
python3 app.py
```

### 访问

```
http://localhost:8080
```

### 管理

用户名：admin
密码：123456

你可以自定义管理密码，如把admin的密码更改为888888：

```
python3 tools/change_admin_passwd.py -p 888888
```

```
http://localhost:8080
```
