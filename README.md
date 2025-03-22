# Technical Test - We+

In order to be able to run this project on your system, please make sure that you've the following dependencies installed:

- Docker
- Docker Compose
- Python 3.12 (with pip enabled) [optional, only needed if you want to run the application locally without containerization]

If you already make sure that all of the dependencies are installed, you can start by cloning / downloading this project on your local machine.

Then, you can copy the `env.example` file and rename it to `.env` file. Adjust the credentials on the `.env` file and `docker-compose.yml` file to your liking.

> P.S: If you want to run everything containerized, you won't need to adjust anything. But if you plan to run the application locally, you'll have to change the `DATABASE_HOST` and adjust it to use `localhost` instead of `database`

Now, you can get everything started with `docker compose up`, and if you want to throw all of the processes into the background, you can add `-d` argument to the command so that it would be `docker compose up -d` instead.

Then, don't forget to run the migration scripts with `docker compose run application python manage.py migrate`, and then add a superuser with `docker compose run application python manage.py createsuperuser --username admin --email admin@example.com` where you'll be prompted for the password.

## ERD
![ERD](https://github.com/muhammad-zakir/technical-test-kita-indonesia-plus/blob/master/ERD.png?raw=true)

## Postman's Collection
A Postman's Collection is also available for you to use within this repository.