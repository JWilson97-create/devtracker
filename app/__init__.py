from flask import Flask
from .routes import job_routes
from .database import init_db

def create_app():
    app = Flask(__name__) # Create a Flask application instance
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # Set the database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources
    init_db(app)  # Initialize the database with the Flask app context
    app.register_blueprint(job_routes)  # Register the job routes blueprint
    return app  # Return the Flask application instance 

    
    # Load configuration from a config file or obje