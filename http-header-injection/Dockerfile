FROM jfloff/alpine-python
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN sed -i '1171,1173s/.*//' /usr/lib/python3.6/site-packages/werkzeug/datastructures.py
COPY app/ /app
WORKDIR /app
CMD ["python", "run.py"]
