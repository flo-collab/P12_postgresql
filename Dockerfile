FROM python:3.8

WORKDIR /script

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .


CMD ["python", "print_lala.py"]