from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database interactions
from app.database import db  # Import the database initialization function
db = SQLAlchemy()  # Create a SQLAlchemy instance for database operations
class Job(db.Model):  # Define a Job model for the jobs table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the job
    company = db.Column(db.String(100), nullable=False)  # Company name
    location = db.Column(db.String(100), nullable=True)  # Job location (optional)
    salary = db.Column(db.Float, nullable=True)  # Job salary (optional)
    position = db.Column(db.String(100), nullable=False)  # Job position
    status = db.Column(db.String(50), nullable=False)  # Job status (e.g., applied, interview, offer)
    notes = db.Column(db.Text, nullable=True)  # Additional notes about the job (optional)


from flask import Blueprint, request, jsonify
from app.database import db
from app.models.job import Job

# Blueprint for job-related routes
job_routes = Blueprint('job_routes', __name__)

@job_routes.route('', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@job_routes.route('', methods=['POST'])
def add_job():
    data = request.get_json()
    job = Job(
        company=data['company'],
        position=data['position'],
        location=data.get('location', ''),
        salary=data.get('salary', 0),
        status=data.get('status', ''),
        notes=data.get('notes', '')
    )
    db.session.add(job)
    db.session.commit()
    return jsonify({'message': 'Job added successfully!'}), 201

@job_routes.route('/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = Job.query.get_or_404(job_id)
    data = request.get_json()
    job.company = data.get('company', job.company)
    job.position = data.get('position', job.position)
    job.location = data.get('location', job.location)
    job.salary = data.get('salary', job.salary)
    job.status = data.get('status', job.status)
    job.notes = data.get('notes', job.notes)
    db.session.commit()
    return jsonify({'message': 'Job updated successfully!'})

@job_routes.route('/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully!'}), 204



    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "salary": self.salary,
            "status": self.status,
            "notes": self.notes
        }

