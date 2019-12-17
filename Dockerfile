FROM python:3.6.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/ml_api

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP run.py

# Install requirements, including from Gemfury
ADD ./packages/ml_api /opt/ml_api/
RUN pip install --upgrade pip
RUN pip install -r /opt/ml_api/requirements.txt

RUN chmod +x /opt/ml_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]