
# Using python:3.10.12-slim-bullseye as base image on debian bullseye in its slim variant
FROM python:3.10.12-slim-bullseye

# set environment variables to unbuffer python output, aiding in logging and debugging
ENV PYTHONUNBUFFERED=1

# define an env variable for the web service's port, defaulting to 8080
ENV PORT=8000

# set tbe working directory within the container to /app for any subsequent commands
WORKDIR /app

# copy entire current directory file from the host to the container's /app directory
COPY . /app/

# install the required packages from the requirements.txt file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# set the command to run our web services using gunicorn, binding it to 0.0.0.0 and the PORT env variable
CMD gunicorn membership_project.wsgi:application --bind 0.0.0.0:${PORT}


# inform docker that the container listens on the specified network port at runtime
EXPOSE ${PORT}