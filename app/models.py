from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database interactions
db = SQLAlchemy()  # Create a SQLAlchemy instance for database operations
class Job(db.Model):  # Define a Job model for the jobs table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the job
    company = db.Column(db.String(120), nullable=False)  # Company name
    location = db.Column(db.String(120), nullable=True)  # Job location (optional)
    salary = db.Column(db.Float, nullable=True)  # Job salary (optional)
    position = db.Column(db.String(120), nullable=False)  # Job position
    status = db.Column(db.String(50), nullable=False)  # Job status (e.g., applied, interview, offer)
    notes = db.Column(db.Text, nullable=True)  # Additional notes about the job (optional)

    def __repr__(self):
        return f'<Job {self.id} - {self.company} - {self.position}>'
    
    