from flask import Flask
from routes.home import home_route

# Initialize
app = Flask(__name__)


# execution
app.run(debug=True)