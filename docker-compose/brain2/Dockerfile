FROM python:3.9-slim

RUN apt-get update && apt-get install -y ethtool

COPY wol_script.py /app/wol_script.py

CMD ["python", "/app/wol_script.py"]
