#  TASK  :TO CREATE 2 CONTAINERS AND ESTABLISH CONNECTION
## This outlines the steps I took to complete the tasks and demonstrate the basic functionality of Docker Compose. 

**Description** : I was tasked with spinning up two containers, Flask and SQL, and connecting the Flask container to the database container.

### Step 1: 
**I created a folder for my project and initialized it with git init.**


 ```bash
 mkdir flask-app
 cd flask-app
 git init
 ```

### Step 2

 **I created an app.py file with a basic Flask program to display "Hello, World," and then wrote a Dockerfile to build an image and run a container with all required dependencies and port mappings.**
   
 ```bash
touch app.py  # Created a hello world message using Flask
touch Dockerfile # Added a Dockerfile to containerize the app
touch requirements.txt # Listed all dependencies (Flask)

# Built and ran the Docker image
docker build -t flaskapp:latest .
docker run -p 3000:3000 flaskapp:latest

# Accessed the app at 127.0.0.1:3000 to verify the hello world message.
```

 ### Step 3 
 **1.I updated the app.py file to establish database connections.**
**2.Created a docker-compose.yml file to launch multiple containers.**

***NOTE: I connected to the database container by using the service name as the DB_HOST in the environment variables.***

 ```bash
touch docker-compose.yml
# Added all database content to the database container using PostgreSQL.
# Built the previously written Dockerfile into a container running the Flask app.
```

 ***Challenges: In the build section of the flask-app container in the YAML file, I added a dot to indicate that the build should use the current Dockerfile.***

***The database container's name is crucial for communication.***


 ### Step 4 

 **Executed all containers simultaneously with Docker Compose.**

 ```bash
 docker compose uild
 docker compose up
 ```

### Challenges: ### 
 **Configuring the correct Python file name in the Dockerfile RUN command.**
 **2>Build: This command is utilized to create an image from a Dockerfile located in the current directory as specified in the YAML file.**
 **3>Verified the connection by accessing the container and executing the command.**
 
   ```
   docker exec <id> -it bash
   psql -U testuser -d testdb 
   ```  
 **3> I was unable to access the database within the psql container. So took the following steps.**
 
 ```bash
 docker exec <container_id> -it bash
 #root@<container_id>psql -U rootuser -d testdb
 #testdb: /l  this will list the databses and the tables in the server
 ```
 

 ## Conclusion:
 **1. Acquired knowledge on how to connect containers to one another using the Docker Compose YAML file.  
2. Understood the significance of port mapping and the process of writing a Dockerfile.  
3. Learned the principles of Docker Compose.**

 # THANK YOU SHASHANK S

