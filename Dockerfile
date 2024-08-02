FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
EXPOSE 80
ENTRYPOINT ["python", "main.py"]
