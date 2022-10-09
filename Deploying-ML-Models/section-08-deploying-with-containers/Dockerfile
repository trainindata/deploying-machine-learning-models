FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/house-prices-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./house-prices-api /opt/house-prices-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/house-prices-api/requirements.txt

RUN chmod +x /opt/house-prices-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
