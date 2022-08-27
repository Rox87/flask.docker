FROM python:3.8.0

WORKDIR /user/src/app

COPY './requirements.txt' .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python","app.py" ]