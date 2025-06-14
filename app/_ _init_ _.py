from flask import Flask
from app.routes.jobs import job_routes
from app.database import db, init_db
from app.config import Config  # Import configuration settings if needed



def create_app():
    app = Flask(__name__) # Create a Flask application instance
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # Set the database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
    init_db(app)  # Initialize the database with the Flask app context
    app.register_blueprint(job_routes)  # Register the job routes blueprint
    return app  # Return the Flask application instance 



   
