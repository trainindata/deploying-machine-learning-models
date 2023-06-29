#
FROM python:3.9

#
WORKDIR /house-prices-api

#
COPY ./requirements.txt /house-prices-api/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /house-prices-api/requirements.txt

#
COPY ./app /house-prices-api/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
