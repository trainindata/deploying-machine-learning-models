# We are going to use this image of Python pulled from Docker Hub as our based image
# This is a Linux based image, so the subsequence commands will use Linux syntax
FROM python:3.6.4

# Create the user that will run the app: ml-api-user
RUN adduser --disabled-password --gecos '' ml-api-user

# We specify our working directory
# This is the location from which the subsequence commands will be run
WORKDIR /opt/ml_api

# This argurment is going to be passed into the BUILD commmanD
ARG PIP_EXTRA_INDEX_URL
# We specify the FLASK_APP environment variable
ENV FLASK_APP run.py

# Install requirements, including from Gemfury
# We copy all the packages of the requirement file to the container
ADD ./packages/ml_api /opt/ml_api/
RUN pip install --upgrade pip
RUN pip install -r /opt/ml_api/requirements.txt

# Give permissions to run
RUN chmod +x /opt/ml_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

# Expose the PORT 5000: incoming requests to our running Docker Container
EXPOSE 5000

# These are the commands to run when the container starts up
CMD ["bash", "./run.sh"]