FROM debian:stable-slim
RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]
