from flask import Flask
app = Flask(__name__)  # Initialize Flask app

# New line
@app.route("/")  # Define a route for the homepage
def home():
    return "<h1>Welcome to My Flask App!</h1><p>This is a simple Flask application.</p>"

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode