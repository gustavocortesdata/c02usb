FROM python:3.8

WORKDIR /home
COPY . .
RUN pip install -r requirements.txt
CMD ["python","./app.py"]
EXPOSE 8025