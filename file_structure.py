 
import os

project_name = "large-scale-data-processing"

# Create project directories
if not os.path.exists(project_name):
    os.makedirs(project_name)
    os.makedirs(os.path.join(project_name, "src"))
    os.makedirs(os.path.join(project_name, "input"))
    os.makedirs(os.path.join(project_name, "output"))

# Define file paths
dockerfile_path = os.path.join(project_name, "Dockerfile")
requirements_path = os.path.join(project_name, "requirements.txt")
master_script_path = os.path.join(project_name, "src", "master.py")
worker_script_path = os.path.join(project_name, "src", "worker.py")

# Create empty files
open(dockerfile_path, "w").close()
open(requirements_path, "w").close()
open(master_script_path, "w").close()
open(worker_script_path, "w").close()
