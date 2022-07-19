from flask import Flask
#from dotenv import load_dotenv 
#load_dotenv() 
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, {os.getenv("SECRET_NAME")}, the menaing of life is {os.getenv("MEANING_OF_LIFE")}'
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
