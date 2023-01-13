FROM python:3.9.16

WORKDIR /app
RUN python3 -m pip install uvicorn fastapi pandas scikit-learn
ADD ./functions /app/functions
COPY main.py .

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000