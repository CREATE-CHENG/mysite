# mysite
基于vue+django的前后端分离的个人网站。  
https://www.herenye.world

## 安装依赖

```
# python虚拟环境下
$ pip install -r requirements.txt
# vue
$ cd frontend/
$ npm install
```
## 打包项目
```
# frontend目录下
$ npm run build
```
## 运行项目
```
# 数据库迁移
$ python manage.py migrate
# 创建用户
$ python manage.py createsuperuser
# 运行
$ python manage.py runserver
```
