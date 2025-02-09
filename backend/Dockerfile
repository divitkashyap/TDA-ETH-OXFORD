FROM python:3.12.2

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python3 fetch_tweets.py && python3 extract_tweets.py && python3 analyze_debates.py"]
