from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database interactions
db = SQLAlchemy()  # Create a SQLAlchemy instance for database operations
def init_db(app):
    """Initialize the database with the Flask app context."""
    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
    with app.app_context():  # Create an application context
        db.create_all()  # Create all database tables defined by models
        # This will create the tables in the database if they do not exist
        # If you want to drop all tables and recreate them, you can uncomment the next line

