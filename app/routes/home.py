from flask import Blueprint 

home_routes = Blueprint('home_routes', __name__)
@home_routes.route('/')
def home():
    return 'Welcome to the Job Tracker API! Use the /jobs endpoint to manage your job listings.'

