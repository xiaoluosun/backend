# 安装依赖项

```Shell
cd backend
pip install -r requirements.txt
```

## 启动

```Shell
# debug
python run.py server

# 生产环境
gunicorn -c gunconfig.py run:app --preload
```
