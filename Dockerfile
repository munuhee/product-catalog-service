FROM python:3.10-alpine
WORKDIR /product-catalog-service
COPY . /product-catalog-service
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "run.py"]