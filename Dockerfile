ARG PYTHON_VERSION=3.12.3

FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /quizapp

RUN apt-get update && \
    apt-get install -y gcc build-essential

COPY requirements.txt .

RUN  python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "quizapp/manage.py", "runserver", "0.0.0.0:8000"]
