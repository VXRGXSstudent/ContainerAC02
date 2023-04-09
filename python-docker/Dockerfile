# python versao 3.8, leve craido no Debian
FROM python:3.8-slim-buster

WORKDIR /app

# copiar a lista de bibliotecas
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]