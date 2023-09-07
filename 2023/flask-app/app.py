from flask import Flask, request

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


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


if __name__ == '__main__':
    app.run()
