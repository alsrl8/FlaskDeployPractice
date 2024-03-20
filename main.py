from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to my Flask application!'


@app.route('/health')
def health():
    # Health check logic here
    # This is a simple example where we just return a JSON response indicating everything is okay.
    return jsonify({"status": "healthy", "message": "Application is running smoothly."})


if __name__ == '__main__':
    app.run(debug=True)
