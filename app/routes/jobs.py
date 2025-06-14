from flask import Blueprint, request, jsonify
from app.database import db
from app.models.job import Job

# Create a Blueprint for job routes
job_routes = Blueprint('job_routes', __name__)

@job_routes.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@job_routes.route('/jobs', methods=['POST'])
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

@job_routes.route('/jobs/<int:job_id>', methods=['PUT'])
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

@job_routes.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully!'}), 204

@job_routes.route('/')
def home():
    return 'Welcome to the Job Tracker API! Use the /jobs endpoint to manage your job listings.'

