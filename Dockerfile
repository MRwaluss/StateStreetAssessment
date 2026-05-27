FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir streamlit

COPY App/ /app/ 

EXPOSE 80

CMD ["streamlit", "run", "assessment_ui.py", "--server.port=80", "--server.address=0.0.0.0"]