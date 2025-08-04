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
	* `sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`
	* Setup database,e.g. Postgre/MySQL: `sudo -u postgres psql` (Create database, create user and grant all priviledges, alter encoding and timezone role)
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

  3. Run server and check required dependencies then Install the dependencies
  Description: Install the required Python packages specified in the project's requirements.txt file.
  Command:
  ```
  pip install -r requirements.txt
  ```
  4. Start the Django Development Server: Description: Start the Django development server to run the web application. Command:
	To run the server via tcp connection 
  ```
    python manage.py runserver 0.0.0.0:5000
  ```
	To run the server via SSL + Gunicorn connection for secure connection
  ```
    gunicorn string_search_server.wsgi:application -c gunicorn.conf.py
  ```
   5. Tests. To execute tests run pytest on any directory or test file
  ```
    pytest
  ```
   6. Running the software as a Linux daemon service
     For production create: `/etc/systemd/system/string_search.service`
  ```
   		[Unit]
		Description=String Search Server Django Service
		After=network.target

		[Service]
		User=www-data
		Group=www-data
		WorkingDirectory=/opt/string_search_server
		ExecStart=/usr/local/bin/gunicorn string_search_server.wsgi:application --bind 0.0.0.0:5000 --certfile=certs/server.crt --keyfile=certs/server.key
		Restart=always

		[Install]
		WantedBy=multi-user.target
  ```

  Then run `sudo systemctl daemon-reload`, `sudo systemctl enable string_search.service` and `sudo systemctl start string_search.service`


## Required Modules
  - ```check requirements.txt file```

## Projects structure

  ### String search server Structure:
string_search_server/
|
|__ config/
|   |
|   |__server_config.ini
|
|__ string_search_server
|   |__ settings.py
|   |__ asgi.py
|   |__ wsgi.py
|   |__ urls.py
|   |__ __init__.py
|
|
|__ 
|   |__ search_app/
|   |__ __init__.py
|   |__ admin.py
|   |__ apps.py
|   |__ models.py
|   |__ search_utils.py
|   |__ ssl_utils.py
|   |__ tests/
|   |__ |__test_views.py
|   |__ |__test_search_utils.py
|   |__ |__test_config.py
|   |   |__ test_ssl_utils.py  
|   | 
|   |__ urls.py
|   |
|   |__ views.py
|
|
|__ data/
|   |__	s.txt files/
|
|
|__ client/
|   |__ client.py
|
|
|__ requirements.py
|
|__ manage.py
|
|__ README.md
|
|__ certs/
|
|__ logs/


## Bugs
At this time, theres no known bugs.

## Author
* Felix Too 
