# vicuna

集群管理工具

## 开发

生成安装依赖
```
pip freeze > requirement.txt
```

## 安装

创建虚拟环境

- python3 :
```
python3 -m venv venv
. venv/bin/activate
```

- python2 :
```
python2 -m virtualenv venv
. venv/bin/activate
```

安装
```
pip install -e .
```

## 运行

```
export FLASK_APP=vicuna
export FLASK_ENV=development
flask init-db
flask run
```

Open http://127.0.0.1:5000 in a browser

## 测试

```
pip install '.[test]'
pytest
```

Run with coverage report:
```
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```