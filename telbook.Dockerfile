FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip

COPY telbook .
RUN pip install -r requirements.txt

COPY entrypoint.sh .

EXPOSE 5000

ENTRYPOINT ["sh","entrypoint.sh"]
