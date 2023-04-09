from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Meu RA é 2201259!'