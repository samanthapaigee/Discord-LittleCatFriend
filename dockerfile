#dockerfile

FROM python:3.13.3

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /app/lcf
WORKDIR /app/lcf

COPY . . 

CMD ["python","bot.py"]
