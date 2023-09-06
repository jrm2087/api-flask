from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "chair",
                "price": 87.99
            }
        ]
    }
]


@app.get("/store")  # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}


if __name__ == '__main__':
    app.run()
