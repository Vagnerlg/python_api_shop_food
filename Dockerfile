FROM python:3.10
WORKDIR /var/www
COPY shop_food shop_food
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
EXPOSE 80/tcp
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:80", "shop_food.app:app"]