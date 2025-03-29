FROM python:3.10.14-slim-bookworm
ENV PYTHONFAULTHANDLER=1 PYTHONHASHSEED=random PYTHONUNBUFFERED=1

RUN mkdir job-hunt-ai
WORKDIR /job-hunt-ai
ENV PIP_DEFAULT_TIMEOUT=100 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1
RUN pip install "pip-tools"
COPY requirements.in ./
RUN pip-compile -r requirements.in -o requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python","run_server.py"]