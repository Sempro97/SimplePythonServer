FROM python:3.8-slim-buster
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 80
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

