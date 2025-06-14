
from pathlib import Path
import sys
# Ensure the parent directory is in the system path
sys.path.append (str((Path(__file__).resolve().parent))) #Add root directory to import path
# Import the create_app function from the app package

from app.__init__  import create_app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)

print(app.url_map)  # Print the URL map to verify routes


# This file is used to run the application.