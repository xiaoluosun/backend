# 安装依赖项

```Shell
cd backend
pip install -r requirements.txt
```

## 安装mysql
安装完成后到config.py修改配置

```Shell
# mysql自己下载安装包吧
安装MySQL成功后：
1. 修改config.py下mysql配置

```

## 安装mongodb

```Shell
1. mongodb安装
brew install mongodb

2. mongodb启动(可以修改下面mongod.conf的ip)
mongod --config /usr/local/etc/mongod.conf

3. config.py下MONGODB配置

```

### 启动

```Shell
# debug
python run.py server

# 生产环境
gunicorn -c gunconfig.py run:app --preload
```
