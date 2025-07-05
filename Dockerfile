FROM python:3.12
LABEL author="Sreeharsha Veerapalli" email="itsreeharsha@gmail.com" batch="AWS B70"
WORKDIR /app
RUN apt update && apt install -y python3-pip jq net-tools tree unzip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD goalscorers.csv goalscorers.csv
COPY app.py app.py
EXPOSE 80
ENTRYPOINT ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
CMD ["--server.port", "80"]
