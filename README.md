# IT Asset Management
Make your IT Asset Management process simple and controlled. This web-based, runs on Apache complete application for tracking computer equipment, software licenses, and accessories in the organization, will make it happen.

<img src="https://cdn3d.iconscout.com/3d/premium/thumb/asset-allocation-3d-icon-download-in-png-blend-fbx-gltf-file-formats--money-management-portfolio-diversification-risk-classes-capital-preservation-investment-pack-business-icons-7863809.png?f=webp" width="350" height="350" />

## Table Of Contents
1. [Introduction](#1-introduction)<br>
2. [Code Explanation and Data Structure](#2-code-explanation-and-data-structure)<br>
    [2.1 Python Application Review](#21-python-application-review)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.1.1 Data Structure Design](#211-data-structure-design)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.1.2 Main Menu Functions](#212-main-menu-functions)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.1.3 Input Validations](#213-input-validations)<br>
    [2.2 Web Development Using Flask](#22-web-development-using-flask)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.2.1 Application Structure](#221-application-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.2.2 HTML Template System](#222-html-template-system)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.2.3 Other Features](#223-other-features)<br>
    [2.3 Containerization with Docker](#23-containerization-with-docker)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.3.1 Dockerfile](#231-dockerfile)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.3.2 Operating With Docker](#232-operating-with-docker)<br>
    [2.4 AWS Cloud Architecture](#24-aws-cloud-architecture)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.4.1 CloudFormation Template Structure](#241-cloudformation-template-structure)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.4.2 EC2 Launch Template](#242-ec2-launch-template)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.4.3 Automated Deployment Script](#243-automated-deployment-script)<br>
    [2.5 Project Files](#25-project-files)<br>
3. [Deployment and Implementation](#3-deployment-and-implementation)<br>
    [3.1 Getting Started](#31-getting-started)<br>
    [3.2 Cloning Github Repository](#32-cloning-github-repository)<br>
    [3.3 Testing Python Application in Local Environment](#33-testing-python-application-in-local-environment)<br>
    [3.4 Testing Webserver Application in Local Environment](#34-testing-webserver-application-in-local-environment)<br>
    [3.5 Migration to Webserver Using Flask and Docker Container](#35-migration-to-webserver-using-flask-and-docker-container)<br>
    [3.6 AWS Setup and Cloud Deployment](#36-aws-setup-and-cloud-deployment)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3.6.1 Setting AWS Lab Credentials](#361-setting-aws-lab-credentials)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3.6.2 Running Automated Deployment Script](#362-running-automated-deployment-script)<br>
    [3.7 Web Application Access and HA Testing via AWS GUI](#37-web-application-access-and-ha-testing-via-aws-gui)<br>
4. CI/CD Pipeline(#4-ci-cd-pipeline)<br>
5. [License](#5-license)<br>
6. [Authors](#6-authors)<br>
7. [Feedback](#7-feedback)<br>

## 1. Introduction
Why we decided to made this application? The answer is pretty simple - every IT department needs asset tracking.<br>
It prevents equipment loss, tracks costs, manages assignments in every organization.

## 2. Code Explaination and Data Structure
Architecture Evolution of the Project:
- Python Application Pure Code Developing
- Code Integration to Webserver Using Flask
- Containerization With Docker
- Migration The Environment to AWS With High Availability

### 2.1 Python Application Review
#### 2.1.1 Data Structure Design
Python Pure Code contains *`main.py`* with main menu UI, *`functions.py`* for all core logic and *`demo.py`* for dummy data pre-loading.
There are two different dabatases (Python dictionaries) exists in *`functions.py`* with relationships by *`assigned_to`* links items to users. There is fast lookup by users/items ID's.
```python
# Users Database
users_db["1"] = {"name": "Brandon Guidelines", "items": []}
users_db["2"] = {"name": "Carnegie Mondover", "items": []}
users_db["3"] = {"name": "John Doe", "items": []}

# Items Database
items_db["1"] = {
    "id": "1", "main_category": "Assets", "sub_category": "Laptop", "manufacturer": "Dell", "model": "XPS", "price": 5000, "quantity": 1, "status": "In Stock", "assigned_to": None
}
items_db["2"] = {
    "id": "2", "main_category": "Assets", "sub_category": "Laptop", "manufacturer": "Lenovo", "model": "X1 Carbon", "price": 8300, "quantity": 1, "status": "In Stock", "assigned_to": None
}
items_db["3"] = {
    "id": "3", "main_category": "Assets", "sub_category": "PC", "manufacturer": "Asus", "model": "Desktop Intel Core i9 14900KS", "price": 14900, "quantity": 1, "status": "In Stock", "assigned_to": "1"
}
```

#### 2.1.2 Main Menu Functions
- *`Add New Item`* - Validates category selection, generates unique item ID, creates item record and updates global item ID counter<br>
- *`Delete Item`* - Searches item by ID, removes from user's item list in case it assigned to him and deletes from items database<br>
- *`Modify Item`* - Loads existing item data by item ID, allows editing manufacturer, model and price data<br>
- *`Assign Item`* - Validates items and user exist, checks if item not already assigned, updates item status to "Assigned" and adds item ID to user's items list<br>
- *`Add New User`* - Generates unique user ID, creates user record and updates global user ID counter<br>
- *`Show All Users`* - Shows all existing users list<br>
- *`Show All Items by the User`* - Shows all assigned items to specific user by user ID<br>
- *`Show All Stock Items`* - Shows all existing stock items list<br>
- *`Calculate Stock by Categories`* - Calculates all stock items price by categories<br>

#### 2.1.3 Input Validations
There are multiple input validation patterns:
- Numeric Validation
```python
if not price.isdigit(): # Checking if the user entered numeric value into the input line above
    print("❌ Error: Entered value for the price must be numeric.")   # Printing Error Message
    return  # Exit the function in this phase (return to main menu)
```
- Category Validation
```python
if sub_category.lower() not in ["pc", "laptop"]:    # In case the User's choise is not equal the sub category prompt
    print("❌ Error: Error: Invalid Item has been chosen.")  # Error Message Printing
    return  # Exit the function in this phase (return to main menu)
```
- Existence Validation
```python
    if not users_db:    # In case there are no users exists in the Users Database
        print("❌ Error: There are no users existing in the database.") ## Printing Error Message 
```
- Item Assignment Status Validation
```python
if items_db[item_id]["status"] == "Assigned":   # Checking if the Item's Status is "Assigned"
    print(f"❌ Error: The item `{items_db[item_id]["sub_category"]} {items_db[item_id]["manufacturer"]} {items_db[item_id]["model"]}` with the ID `{item_id}` is already assigned to another user.")    # Printing Error Message because the item is already assigned to another user
    return  # Exit the function in this phase (return to main menu)
```
### 2.2 Web Development Using Flask
Migration phase to web-server using Flask module has been choosen because Flask is a great solution for small or medium applications, it doesn't force specific structure and it's easy to convert existing Python login.

#### 2.2.1 Application Structure
*```app.py```* - Main Flask Application
```python
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages
```
Route Pattern Example:
```python
@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    global item_id_counter
    if request.method == "POST":
        # Process form submission
        return redirect(url_for("add_item"))
    # Show form
    return render_template("add_item.html", menu_links=get_menu_links())
```

#### 2.2.2 HTML Template System
HTML template pages were pre-created for each menu item function. *```base.html```* page uses as a template for all pages and *```index.html```* page for the home page with users and items databases calculated statistics. Python code via Flask module is integrated and running on them based on menu function has chosen.

#### 2.2.3 Other Features
- Flash Messages System
```python
flash(f"Item with ID {item_id} deleted.", "success")
flash(f"No item found with ID {item_id}.", "danger")
```
- Required Fields Validation
```html
<form method="POST">
  <div class="mb-3">
    <label for="sub_category" class="form-label">Sub Category</label>
    <select class="form-select" id="sub_category" name="sub_category" required>
      <option value="">Select a main category</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary">Add Item</button>
</form>
```
- Main and Sub-Categories Validation
```html
  <div class="mb-3">
    <label for="main_category" class="form-label">Main Category</label>
    <select class="form-select" id="main_category" name="main_category" required onchange="updateSubcategories()">
      <option value="">Choose category</option>
      <option value="Assets">Assets</option>
      <option value="Accessories">Accessories</option>
      <option value="Licenses">Licenses</option>
    </select>
  </div>

  <div class="mb-3">
    <label for="sub_category" class="form-label">Sub Category</label>
    <select class="form-select" id="sub_category" name="sub_category" required>
      <option value="">Select a main category</option>
    </select>
  </div>
```
- Numeric Validation
```html
  <div class="mb-3">
    <label for="price" class="form-label">Price per Unit (₪)</label>
    <input type="number" class="form-control" id="price" name="price" min="0" step="0.01" required />
  </div>
```

### 2.3 Containerization with Docker
Containerization using Docker provides same environment everywhere, the application runs independently of host system, it works on any Docker-enabled system and it's easy to run multiple instances with it.

#### 2.3.1 Dockerfile
*```Dockerfile```* was created with all relevant commands for "one-click" environment creation. Port 31415 is used for web application.
```python
# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-flask \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /var/www/it-asset-management

# Copy website files from the correct path
COPY website/ ./

# Install Flask using pip (backup)
RUN pip3 install flask

# Expose port 31415 web access
EXPOSE 31415

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run when container starts
CMD ["python3", "-m", "flask", "run", "--port=31415"]
```
#### 2.3.2 Operating With Docker
Follow the commands below in order to build image using Dockerfile, run container based on the image and verify running afterward:
- *`docker build -f docker/Dockerfile -t it-asset-management .`* to build image based on Dockerfile
- *`docker run -d -p 31415:31415 --name my-app it-asset-management`* to run container based on the image
- *`docker ps`* and *`curl http://localhost:31415`* to verify running

### 2.4 AWS Cloud Architecture
Amazon Web Services platform has been chosen for cloud hosting of the web-server including HA (High Availability) feature using AWS tools:
- Load Balancer
- Auto Scaling Group
- Multiple EC2 Instances
- Multiple Availability Zones

#### 2.4.1 CloudFormation Template Structure
*```cloudformation.yaml```* file contains all relevant configuration for the above mentioned features to deploy:
- *`Network Infrastructure`* - Isolated network environment with multiple subnets located in different avialability zones with direct internet access for web servers
```yaml
VPC: 10.0.0.0/16
PublicSubnet1: 10.0.1.0/24 (AZ-1)
PublicSubnet2: 10.0.2.0/24 (AZ-2)
InternetGateway: Internet access
```
- *`Security Groups`* - Least privilege access
```yaml
LoadBalancerSG: Port 80 from anywhere
WebServerSG: Port 31415 from LoadBalancer only
```
- *`Auto Scaling Group`* - Always 2 or more instances properly running for HA including health check for replacing failed instances
```yaml
MinSize: 2
MaxSize: 4
DesiredCapacity: 2
HealthCheckType: ELB
```
- *`Application Load Balancer`* - Splits users requests sends to web servers across instances via sending traffic to healthy instances only
```yaml
Scheme: internet-facing
HealthCheckPath: /
HealthCheckInterval: 30s
```

#### 2.4.2 EC2 Launch Template
Launch Template for EC2 instances is used for creating new instances in order to automatically replace failed instances, which can increase capacity automatically as well.

```shell
#!/bin/bash
# AWS Academy compatible startup script

# Update system and install requirements
yum update -y
yum install -y docker git

# Start Docker
service docker start
chkconfig docker on
usermod -a -G docker ec2-user

# Clone repository and build app (no ECR dependency)
cd /home/ec2-user
git clone https://github.com/dcoacher/it-asset-management.git
cd it-asset-management

# Build Docker image from source
docker build -f docker/Dockerfile -t it-asset-management .

# Run the application
docker run -d -p 31415:31415 --restart unless-stopped --name it-asset-app it-asset-management
```

### 2.4.3 Automated Deployment Script
*`deploy.sh`* is an Automated AWS Deployment Script which has been used as a part of DevOps flow in order to automate the deployment process to cloud environment. As a result we have the same infrastructure available, which can be deployed to test environments every time it needs.<br>
The script gets data of AWS account ID, creates ECR repository for Docker image, builds and pushs Docker image and deploys CloudFormation infrastructure using *`cloudformation.yaml`* configuration file as well.

```bash
#!/bin/bash
# IT Asset Management AWS Deployment Script

echo "=== Getting AWS Account ID ==="
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo "Account ID: $ACCOUNT_ID"

echo "=== Creating ECR Repository ==="
aws ecr create-repository --repository-name it-asset-management --region us-east-1 || echo "Repository already exists"

echo "=== Building Docker Image ==="
docker build -f docker/Dockerfile -t it-asset-management .

echo "=== Logging into ECR ==="
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

echo "=== Tagging and Pushing Image ==="
IMAGE_URI="$ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/it-asset-management:latest"
docker tag it-asset-management:latest $IMAGE_URI
docker push $IMAGE_URI
```

### 2.5 Project Files
- :file_folder: *`.github/workflows`* directory contains CICD pipeline files
    - :page_facing_up: *`CICD.yaml`* CICD pipeline configuration file
- :file_folder: *`aws`* directory contains data relevant to AWS deployment
    - :page_facing_up: *`cloudformation.yaml`* configuration file for CloudFormation in AWS environment
- :file_folder: *`cicd`* directory contains CICD pipelines related files
    - :page_facing_up: *`Dockerfile`* configuration file for Docker environment CICD deployment
    - :page_facing_up: *`demo.py`* contains pre-created and loaded dummy data for demonstration purposes
    - :page_facing_up: *`functions.py`* contains functions for reusable logic of the main file
    - :page_facing_up: *`main.py`* is the main project file (modified for CICD pipeline)
    - :page_facing_up: *`requirements.txt`* Python related environment dependencies required for installation
    - :page_facing_up: *`test_main.py`* Pytest file for main.py as a part of CICD process
- :file_folder: *`docker`* directory contains Dockerfile
    - :page_facing_up: *`Dockerfile`* configuration file for Docker environment AWS deployment
- :file_folder: *`python`* directory contains pure Python code:
    - :page_facing_up: *`main.py`* is the main project file
    - :page_facing_up: *`functions.py`* contains functions for reusable logic of the main file
    - :page_facing_up: *`demo.py`* contains pre-created and loaded dummy data for demonstration purposes
- :file_folder: *`scripts`* directory contains script files
    - :page_facing_up: *`deploy.sh`* AWS deployment automation script
- :file_folder: *`website`* directory contains website data like HTML pages etc.
    - :file_folder: *`templates`* pre-rendered .html webpages
        - :page_facing_up: *`add_item.html`*
        - :page_facing_up: *`add_user.html`*
        - :page_facing_up: *`assign_item.html`*
        - :page_facing_up: *`base.html`*
        - :page_facing_up: *`delete_item.html`*
        - :page_facing_up: *`index.html`*
        - :page_facing_up: *`modify_item_form.html`* 
        - :page_facing_up: *`modify_item_select.html`*
        - :page_facing_up: *`show_stock_items.html`* 
        - :page_facing_up: *`show_user_items_select.html`*
        - :page_facing_up: *`show_user_items.html`*
        - :page_facing_up: *`show_users.html`*
        - :page_facing_up: *`stock_by_categoeirs.html`*
    - :page_facing_up: *`app.py`* main webserver file
    - :page_facing_up: *`data.py`* database data webserver file
    - :page_facing_up: *`demo.py`* dummy pre-loaded data webserver file

## 3. Deployment and Implementation
### 3.1 Getting Started
Before starting, ensure to check your environment is ready to go:
- AWS CLI Installed - *[AWS CLI install and update instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)*
- Docker Installed and Running - *[Install Docker Engine](https://docs.docker.com/engine/install/)*
- Git Installed - *[Git Downloads](https://git-scm.com/downloads)*
- Python Installed - *[Download Python](https://www.python.org/downloads/)*
- AWS Sandbox Lab is Running - *[AWS Academy Login](https://awsacademy.instructure.com/)*
- Verify that Python installation path is added to Windows Environment Variables

### 3.2 Cloning Github Repository
*`Git Bash`* application or *`Visual Studio Code terminal`* will be used for the deployment in the next steps:
- *`mkdir Documents/technion-midterm-project`* to create a clean workspace for demonstration
- *`cd Documents/technion-midterm-project`* to change work directory
- *`git clone https://github.com/dcoacher/it-asset-management.git`* to clone git repository
- *`cd it-asset-management`* to change work directory
- *`ls -la`* to display project structure

### 3.3 Testing Python Application in Local Environment
Test Python application in local environment in order to check it's workability:
- Open the project directory folder in Visual Studio Code
- Run the *`main.py`* application file from *`python`* folder

### 3.4 Testing Webserver Application in Local Environment
Test Webserver application running on Flask in local environment in order to check it's workability:
- *`pip install flask`* for Flask module installation in Visual Studio Code
- Run the *`app.py`* application file from *`website`* folder
- Browse *`http://localhost:31415`*

### 3.5 Migration to Webserver Using Flask and Docker Container
Migrate the Python application to Apache webserver using Flask module and Docker Containerization and perform test in local environment:
- *`docker build -f docker/Dockerfile -t it-asset-management .`* to build image based on Dockerfile
- *`docker run -d -p 31415:31415 --name my-app it-asset-management`* to run container based on the image
- *`curl http://localhost:31415`* to verify running
- *`docker stop my-app && docker rm my-app`* for cleanup performing

### 3.6 AWS Setup and Cloud Deployment
#### 3.6.1 Setting AWS Lab Credentials
- *`export AWS_ACCESS_KEY_ID=<access-key-data>`* to export AWS access key value
- *`export AWS_SECRET_ACCESS_KEY=<secret-key-data>`* to export AWS secret key value
- *`export AWS_SESSION_TOKEN=<token-data>`* to export AWS Session token value
- *`export AWS_DEFAULT_REGION=us-east-1`* to set up the default region value
- *`aws sts get-caller-identity`* to verify workability

#### 3.6.2 Running Automated Deployment Script
- *`bash scripts/deploy.sh`* to complete environment deploying using automation script
- Wait up to 5-10 minutes for all environment creation

### 3.7 Web Application Access and HA Testing via AWS GUI
 - Retrieve Load Balancer URL via AWS GUI and access cloud application
 - Take a look on EC2 instances running
 - Test HA by stopping one instance (verify that another one new instance will be created to replace stopped/failed instance)
 - Access cloud application again in order to check workability
 - Check Auto Scaling policy

## 4. CI/CD Pipeline
CICD Process Support added to this project.<br>
Trigger: *`Push`*
Process:
- Step 1: Python Pure Code Checkout using Pytest:
    - Test Condition 1: Exit flow from Main Menu (q)
    - Test Condition 2: Invalid menu option check in Main Manu
- Step 2: Docker Image Build (Docker Hub)
- Step 3: Deploy Using Docker Hub Image

## 5. License
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://github.com/dcoacher/it-asset-management/blob/main/LICENSE)

## 6. Authors
This project is a result of the great collaboration of the two developers:
- Desmond Coacher - [@dcoacher](https://github.com/dcoacher)
- Artiom Krits - [@ArtiomKrits92](https://github.com/ArtiomKrits92)

## 7. Feedback
If you have any feedback, feel free to contact us via email: 
- [Desmond Coacher](mailto:dcoacher@outlook.com)
- [Artiom Krits](mailto:artiomkrits92@gmail.com)

