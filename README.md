# Crispy Succotash
## Installation

1. Install [Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/)

2. cd into the project directory
  
  ```shell
  cd crispy-succotash
  ```
  
2.1 **SKIP THIS STEP IF YOU'RE USING LINUX**
    
    If you're running Docker in a VM  (docker-machine) you'll find permission issues due to the way Postgres' handles its data directory permissions and the fact that you're running it inside a VM with a shared AUFS folder from your host (bug description can be found [on this link](https://github.com/docker-library/postgres/issues/60)). There are ways to fix this, but they take time and are quite annoying. 
    
    I've created a separated docker-compose file for Macs, which needs to be specified when running all docker-compose commands. 
    You can run the project directly with no preparation commands.
 
3. Run it

  Linux

  ```shell
  docker-compose up
  ```
  
  Docker-Machine

  ```shell
  docker-compose -f docker-compose.mac.yml up
  ```
  
That's it! :) The project will be available on port 8000 of your Docker host. 

## Running the tests

  ```shell
  docker-compose run app bash
  ./manage.py test
  ```
