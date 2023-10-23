from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

def page_not_found():
    return "<h1>Page not found</h1>",404

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=4050)
