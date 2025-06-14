from flask import Blueprint, request, jsonify # Import necessary Flask modules
from .models import db, Job  # Import the database and Job model

job_routes = Blueprint ('job_routes', __name__)  # Create a Blueprint for job routes
@job_routes.route('/jobs', methods=['GET'])  # Define a route to get all jobs

def get_jobs():
    jobs = Job.query.all()  # Query all jobs from the database
    return jsonify([{
        'id': job.id,
        'company': job.company,
        'position': job.position,
        'location': job.location,
        'salary': job.salary,  # Assuming salary is a field in the Job model
        'status': job.status,
        'notes': job.notes,
    } for job in jobs])

@job_routes.route('/jobs', methods=['POST'])  # Define a route to create a new job
def add_job():
    data = request.get_json()  # Get the JSON data from the request
    job = Job(
        company=data['company'],
        position=data['position'],
        location=data.get('location', ''),  # Use an empty string if location is not provided
        salary=data.get('salary', 0),  # Use 0 if salary is not provided
        status=data['status'],
        notes=data.get('notes', '')  # Use an empty string if notes are not provided
    )
    db.session.add(job)
    db.session.commit()
    return jsonify({'message': 'Job added successfully!'}), 201

@job_routes.route('/jobs/<int:job_id>', methods=['PUT'])  # Define a route to update a job
def update_job(job_id):
    job = Job.query.get_or_404(job_id)  # Get the job by ID or return a 404 error if not found
    data = request.get_json()  # Get the JSON data from the request
    job.company = data['company']
    job.position = data['position']
    job.location = data.get('location', job.location)
    job.salary = data.get('salary', job.salary)
    job.status = data['status']
    job.notes = data.get('notes', '')
    db.session.commit()
    return jsonify({'message': 'Job updated successfully!'})

@job_routes.route('/jobs/<int:job_id>', methods=['DELETE'])  # Define a route to delete a job
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)  # Get the job by ID or return a 404 error if not found
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully!'}), 204
