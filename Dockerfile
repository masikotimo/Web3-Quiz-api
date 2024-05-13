FROM python:3.8.5

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /land_evaluation_app

# Set the working directory to /land_evaluation_app
WORKDIR /land_evaluation_app

# Copy the current directory contents into the container at /land_evaluation_app
ADD . /land_evaluation_app/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

CMD sh init.sh && pytest && python3 manage.py runserver 0.0.0.0:8000
