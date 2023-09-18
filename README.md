# Api with Python and Flask
Python y Flask.

## Install Flask
```py
pip install flask
```

## Install Flask-RESTful
```py
pip install flask-restful
```

## Install Dependencies from txt file
```py
pip install -r requirements.txt
```

## List Dependencies
```py
pip freeze
```

## Virtual envs
```py
pip install virtualenv
virtualenv venv --python=python3.5

Linux or Mac:
source venv/bin/activate

deactivate

Windows:
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

## commands Flask
```py
flask run

flask db init

flask db migrate

flask db upgrade
```

## commands Docker
```py
docker build -t rest-apis-flask-python .

docker run -p 5005:5000 rest-apis-flask-python

docker run -dp 5005:5000 rest-apis-flask-python

docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api

docker build -t flask-api-app .
docker run -dp 5015:5000 -w /app -v "$(pwd):/app" flask-api-app
```


