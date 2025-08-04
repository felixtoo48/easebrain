# String Search Server
The Project is a standardized introductory task for Software Engineers at Algorithmic Sciences specifically as the second step of the interview process.

#### Functionalities of the project:
* Checking execution times of searching one line strings from different files 
* Benchmarking different algorithms
* SSL and Tcp connection between client and server
* Checking both True/False option's execution times for Reread on query while quering the server  


## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using Django (version 5.2.4)


## Installation

### How to runthe project
  	* To get started, install python3 development tools on your virtual machine.
	* `sudo apt-get update`
	* Setup database: MySQL: `sudo mysql -u root -p` (Create database, create user and grant all priviledges, alter encoding and timezone role)
		`CREATE DATABASE crm_db;`
		`CREATE USER 'crm_dbuser'@'localhost' IDENTIFIED BY 'Password@Here1234';`
		`GRANT ALL PRIVILEGES ON crm_db.* TO 'crm_dbuser'@'localhost';`
		` FLUSH PRIVILEGES`
	* Install virtual environment and install django
	* `sudo -H pip3 install --upgrade pip` then `sudo -H pip3 install virtualenv`
	* Create directory and install django
	* Run django app: `python manage.py makemigrations` then `python manage.py migrate`
	* Run app: `python manage.py runserver 0.0.0.0:5000`

 
  1. navigate to the Project directory: Change your current working directory to the root directory of Django Project.
  Command:
  ```
  cd <project_directory>
  ```
      And import the zip file for the project (repository) already shared

  2. create a Virtual Environment Description: Create a virtual environment to isolate dependencies for the project. Command:
  Command:
  ```
    python -m venv .venv 
  ```
  3. Activate the Virtual Environment: Description: Activate the virtual environment to use its isolated Python environment.
  Command:
  Mac(Linux):
  ```
    source venv/bin/activate
  ```

  4. Run server and check required dependencies then Install the dependencies
  Description: Install the required Python packages specified in the project's requirements.txt file.
  Command:
  ```
  pip install -r requirements.txt
  ```
  5. Start the Django Development Server: Description: Start the Django development server to run the web application. Command:
	To run the server via tcp connection 
  ```
    python manage.py runserver 0.0.0.0:5000
  ```
	To run the server via SSL + Gunicorn connection for secure connection
  ```
    gunicorn string_search_server.wsgi:application -c gunicorn.conf.py
  ```
   6. Tests. To execute tests run pytest on any directory or test file
  ```
    pytest
  ```
   7. Run the client.py file on separate terminal, for testing queries between client and server

   8. Running the software as a Linux daemon service

     For production create: `/etc/systemd/system/string_search.service`
NB: Configuration used is for local pc
  ```
 [Unit]
Description=String Search Server Django Service
After=network.target

[Service]
User=felix
Group=www-data
WorkingDirectory=/home/felix/Algorithmic_sciences/String_Search_Server/string_search_server
ExecStart=/home/felix/Algorithmic_sciences/String_Search_Server/venv/bin/gunicorn string_search_server.wsgi:application \
  --bind 0.0.0.0:5000 \
  --certfile=certs/server.crt \
  --keyfile=certs/server.key
Restart=always
Environment="PATH=/home/felix/Algorithmic_sciences/String_Search_Server/venv/bin"

[Install]
WantedBy=multi-user.target
  ```

  Then run `sudo systemctl daemon-reload`, `sudo systemctl enable string_search.service` and `sudo systemctl start string_search.service`


## Required Modules
  - ```check requirements.txt file```

## Projects structure

  ### String search server Structure:


## Bugs
At this time, theres no known bugs.

## Author
* Felix Too 
