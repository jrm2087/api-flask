# Aip with Python and Flask
Python y Flask.

## Install Flask
```py
pip install flask
```

## Install Flask
```py
pip install flask-restful
```

## List
```py
pip  freeze
```

## Virtual envs
```py
pip install virtualenv
virtualenv venv --python=python3.5

Linux or Mac:
source venv/bin/activate

deactivate

windows:
./venv/Scripts/activate.bat

```

## Conda environment
```py
conda create -n flask python==3.8
```

## Migrate db
```py
set FLASK_APP=file.py
flask db init
flask db migrate -m "coment"
flask db upgrade
```


