#
FROM python:3.9

#
WORKDIR /section-06-model-serving-api

#
COPY ./house-prices-api/requirements.txt /section-06-model-serving-api/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /section-06-model-serving-api/requirements.txt

#
COPY ./house-prices-api/app /section-06-model-serving-api/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
