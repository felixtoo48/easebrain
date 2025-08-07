# String Search Server
This project is a standardized introductory task for Software Engineers at Algorithmic Sciences, representing the second step of the interview process.

#### Functionalities:
* Benchmarking multiple search algorithms across various file sizes. 
* Comparing performance with REREAD_ON_QUERY=TRUE vs FALSE.
* Secure SSL/TCP client-server communication.
* Concurrent requests handling via multi-threaded WSGI
* Unit tests for views, SSL utils, search utilities, and client scripts.


## Environment
* OS: Ubuntu 20.04 LTS
* Framework: Django 5.2.4
* Database: MySQL
* Python Version: 3.11


## Projects structure

  ### String Search Server Structure:

    String_search_server/
      |__ string_search_server/
      |    |__ config/
      |    |  |__ server_config.ini
      |    |  
      |    |__ Search_app/
      |    |   |__ __init__.py
      |    |   |__ models.py
      |    |   |__ admin.py
      |    |   |__ app.py
      |    |   |__ urls.py
      |    |   |__ views.py
      |    |   |__ search_utils.py
      |    |   |__ ssl_utils.py
      |    |   |___threading_utils.py
      |    |   |__ tests/
      |    |        |__ __init__.py
      |    |        |__ test_views.py
      |    |        |__ test_ssl_utils.py
      |    |        |__ test_search_utils.py
      |    |        |__ test_client.py
      |    |        |__ test_threading_utils.py
      |    |
      |    |__ string_search_server/
      |    |   |__ settings.py
      |    |   |__ urls.py
      |    |   |__ asgi.py
      |    |   |__ wsgi.py
      |    |
      |    |__ manage.py
      |    |
      |    |__ client/
      |    |   |__ client.py
      |    |
      |    |__ certs/
      |    |   |__ server.crt
      |    |   |__ server.key
      |    |   
      |    |__ data/
      |    |   |__ sample_files    # 10k.txt, 50k.txt, 100k.txt, 200k.txt, 500k.txt, 500k.txt
      |    |
      |    |__ log/
      |    |   |__ server.log
      |    |
      |    |__ README.md
      |    |
      |    |__ .env
      |
      |__ venv/
      |__ README.md
      |__ requirements.txt


## Installation and setup

### How to runthe project

  1. Extract .zip file and navigate:
  ```
  cd String_search_server
  ```

  2. Setup virtual environment:
  Command:
  ```
    python -m venv .venv
    source venv/bin/activate 
  ```

  3. Install dependencies:
  ```
  pip install -r requirements.txt
  ```

  4. Configure MySQL Database `sudo mysql -u root -p`:
  ```
  CREATE DATABASE crm_db;
  CREATE USER 'crm_dbuser'@'localhost' IDENTIFIED BY 'Password@Here1234';
  GRANT ALL PRIVILEGES ON crm_db.* TO 'crm_dbuser'@'localhost';
  FLUSH PRIVILEGES;
  ```

  5. Run migrations:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

  6. Create SSL Certificates (Self-Signed for Local):
  ```
  mkdir certs && cd certs
  openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes
  cd ..
  ```

  Create `gunicorn.conf.py` file in project's root directory.
		- Module configures SSL directly without using shell substitution
  Update content as per your requirements; ssl cert and key, port, ip etc.


  ```
   from search_app.ssl_utils import get_ssl_config

   ssl = get_ssl_config()

   certfile = ssl["certfile"]
   keyfile = ssl["keyfile"]
   bind = "0.0.0.0:5000"
   workers = 3

  ```

  7. Running the server:
     Development server 
  ```
    python manage.py runserver 0.0.0.0:5000
  ```

     Production server (Gunicorn + SSL + Multithreading):
  ```
    gunicorn string_search_server.wsgi:application -c gunicorn.conf.py
  ```

    or
   ```
    gunicorn string_search_server.wsgi:application \
   --workers 4 \
   --threads 4 \
   --bind 0.0.0.0:5000 \
   --certfile=certs/server.crt \
   --keyfile=certs/server.key
   ```

   8. Run tests:
  ```
    pytest
  ```

   9. Run the client.py file on separate terminal, for testing queries between client and server


### Running the server as a Linux daemon/service
   1. Create the service file:
   ```
    sudo nano /etc/systemd/system/string_search.service
   ``` 

     Content:
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

	NB:
	* Update the Workingdirectory of the service file with your root project directory path i.e String_search_server
	* Update ExecStart with your virtual environment's gunicorn project directory path
	* Update Environment with your virtual environament path
   Activate and start:
	
   ```
   sudo systemctl daemon-reload
   sudo systemctl enable string_search.service
   sudo systemctl start string_search.service
   ```

## Testing
   Run all tests:
  ```
   pytest
  ```
  Tests include:
* Views and HTTP responses.
* SSL utility validation
* Search algorithms correctness
* Client-server TCP/SSL connection
* Error handling and edge cases

For testing while SSL is enabled, change 'SSL_ENABLED = True' in client.py.
and runserver as follows:
```
gunicorn string_search_server.wsgi:application \
   --workers 4 \
   --threads 4 \
   --bind 0.0.0.0:5000 \
   --certfile=certs/server.crt \
   --keyfile=certs/server.key
``` 

## Bugs
At this time, there's no known bugs.

## Author
* Felix Too 
