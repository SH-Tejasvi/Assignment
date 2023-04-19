from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello World'
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
@app.route('/health')
def health_check():
    # simulate an error by returning a 500 Internal Server Error response code
    return 'Internal Server Error', 500
