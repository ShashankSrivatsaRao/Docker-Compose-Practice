#  TASK  :TO CREATE 2 CONTAINERS AND ESTABLESH CONNECTION
## This includes all the steps I took to complete the tasks in order to demonstrate the simple working of the docker compose .

**Description** : I was given a task to spin up 2 containers ,flask and sql and connect to the database container using the flask container.

### Step 1: 
 First I created a folder to store my project and initialized it using git init.

 ```bash
 mkdir flask-app
 cd flask-app
 git init
 ```

### Step 2
 Now I started by creating the app.py file and added basic flask program into it to display hello world. Now I wrote a Dockerfile to create an image and run a container with all the dependencies and port mapping.
 ```bash
 touch app.py     --wrote the code for a hello world msg from flask docs
 touch Dockerfile    --wrote a docker file to run this app in a container
 touch requirements.txt   --put alll the requirements in this file (Flask)
  ---after writing all the files built an image and ran it as a container 
 docker build flaskapp:latest .
 docker run -p 3000:3000 flaskapp:latest
 --Checked the address 127.0.0.1:3000 to see hello world app.
 ```

 ### Step 3 
 I added code in the app.py file to make connections to a database.

 And created a docker-compose.yml file to spin up multiple containers

 ```bash
 touch docker-compose.yml 
     --added all the content of databse into the databse container using the postgres database.
     --built the previously written docker file into a container running the flask app
 ```

 *** Challenges: In the build section under flask-app container of the yml file I just added a . signifying that I had to build using the current docker file.

 Also the name of the database container is important to communicate with it. ***

 ### Step 4 

 Ran all the containers together using the docker compose 

 ```bash
 docker compose uild
 docker compose up
 ```

### Challenges: 1> Configuring the corrent name of the python file in the Dockerfile RUN command
 2>Build : .  this command used to build an image from a docker file in the current folder in the yml file . ###

 ## Conclusion:
 ** LEARNT HOW TO CONNCET THE CONTAINERS TO ONE ANOTHER USING THE DOCKER COMPOSE YML FILE AND ALSO LEARNT HOW IMPORTANT PORT MAPPING AND WRITING A DOCKERFILE IS.LEARNT THE CONCEPT OF DOCKER COMPOSE. **

 # THANK YOU SHASHANK S

