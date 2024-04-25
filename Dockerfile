FROM python:3.12.1

COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
