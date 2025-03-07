FROM python:slim
WORKDIR /app
COPY . /app
RUN pip install flask yfinance
EXPOSE 5000
CMD ["python", "app.py"]