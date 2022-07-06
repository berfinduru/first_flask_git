FROM python:3-alpine3.16
RUN pip3 install flask
WORKDIR /app
COPY mynew.py .
EXPOSE 5001
CMD ["python3", "mynew.py"]