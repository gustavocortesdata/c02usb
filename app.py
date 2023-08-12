import random as rd

from flask import Flask
app= Flask(__name__)

@app.route('/', methods=['get'])
def hello_world():
	return {
		"mensaje":"hello"
	}

@app.route('/random', methods=['get'])
def random():
	return {
		"guess": rd.randint(3,20)
	}

app.run(host="0.0.0.0",port=8025)
