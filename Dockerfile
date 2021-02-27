# import python and the os as a docker image
FROM python:3.9.2-alpine3.13

# setup working directory
WORKDIR /myWorkDir

# copy files from the host to the current location
COPY requirements.txt .
COPY ./src/ /myWorkDir

# install dependencies
RUN pip install -r requirements.txt

# run the command in the container
CMD ["python", "./app.py"]