FROM python:3.11-slim
WORKDIR /app

# Install minimal Python + mock server dependencies
RUN pip install flask

# Create a simple Flask app
RUN echo "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef hello():\n    return 'Hello Backend'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=8080)" > app.py

EXPOSE 8080
CMD ["python", "app.py"]
