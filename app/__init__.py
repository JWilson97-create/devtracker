from flask import Flask
from app.routes.jobs import job_routes
from app.database import db, init_db

def create_app():
    app = Flask(__name__) # Create a Flask application instance
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # Set the database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
    init_db(app)  # Initialize the database with the Flask app context
    
    app.register_blueprint(job_routes)  # Register the job routes blueprint
    return app  # Return the Flask application instance 

    
    # Load configuration from a config file or objefrom flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes.jobs import job_routes
    app.register_blueprint(job_routes, url_prefix="/jobs")

    db.init_app(app)
    return app
