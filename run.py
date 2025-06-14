import sys
from pathlib import Path
# Ensure the parent directory is in the system path
sys.path.append(str(Path(__file__).resolve().parent.resolve())) #Add root directory to import path
# Import the create_app function from the app package

from app import create_app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)

    # This file is used to run the application.