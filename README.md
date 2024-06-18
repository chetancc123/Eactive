# Eactive
=> 1) Flask Application
**My code is in steptech_assignment branch.So please click branch and go to steptech_assignment branch for the code

This is a simple Flask application that allows users to view, add, and get details of users from a MySQL database.

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Database Schema](#database-schema)
3. [Sample Data](#sample-data)
4. [Dependencies](#dependencies)
5. [Git Workflow and Contribution](#git-workflow-and-contribution)

## Setup Instructions

### Prerequisites

- Python 3.x
- MySQL
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository_name.git
   cd your_repository_name
   

=> 2)Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux

=> 3)Install the dependencies:
    pip install -r requirements.txt

=> 4)Set up the MySQL database and create a .env file with your database credentials:
    DB_HOST=localhost
    DB_USER=your_mysql_username
    DB_PASSWORD=your_mysql_password
    DB_NAME=your_database_name

=>5)Run the Flask application:
    flask run


##Database Schema
The users table has the following columns:

id (int, primary key)
name (varchar)
email (varchar)
role (varchar)

SQL to Create the Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(100)
);


##Dependencies
The application requires the following Python packages:

Flask
Flask-MySQLdb
python-dotenv
You can install these dependencies using the provided requirements.txt file.


##Git Workflow and Contribution
Git Workflow

1.Initialize a new Git repository:
    git init
    
2.Create a branch named steptech_assignment:
    git checkout -b steptech_assignment
    
3.Make necessary commits as you implement the Flask API and database functionality:
    git add .
    git commit -m "Initial commit with Flask app, templates, and static files"
    
4.Push your branch to a remote Git repository:
    git remote add origin https://github.com/your_username/your_repository_name.git
    git push -u origin steptech_assignment


##How to Contribute

1.Fork the repository.

2.Create a new branch for your feature or bugfix:
    git checkout -b feature_name
    
3.Make your changes and commit them with a descriptive message:
    git add .
    git commit -m "Add new feature"
    
4.Push your branch to your forked repository:
    git push origin feature_name
    
5.Open a pull request on the main repository, describing your changes and why they should be merged.



