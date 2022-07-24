FROM tensorflow/tensorflow:latest-gpu-jupyter 

WORKDIR /tf/ml_api


ENV FLASK_APP run.py

ADD ./packages /tf/packages 
RUN pip install --upgrade pip
RUN pip install -r /tf/packages/regression_model/requirements.txt
RUN pip install -r /tf/packages/ml_api/requirements.txt



EXPOSE 5000
EXPOSE 8888
# ENTRYPOINT [ "python" ]
CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]