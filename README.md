Необходимые компоненты: python 2.7, Ubuntu 12.04 и выше.

Установка необходимых зависимостей.
sudo apt-get install git
sudo apt-get install mongodb
sudo pip install Django 
sudo pip install django-mongodb-engine 
sudo pip install djangotoolbox
sudo pip install git+https://github.com/django-nonrel/django@nonrel-1.5

Развертывание системы.

git clone https://github.com/vicky92/lab5_afisha.git
cd lab5_afisha
python manage.py runserver

Доступ к сайту: http://localhost:8000

