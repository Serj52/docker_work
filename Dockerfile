#sudo docker build -t app . создать образ
#df -h  посмотреть своюодное место
#sudo docker images
#sudo docker rmi $(sudo docker images -q) -f Очистить все images
#sudo docker run --rm --name web app Запуск контейнера с удалением
#sudo docker ps -all Посмотреть список контейнеров
#sudo docker rm 2b2f4c5f7715 удалить контейнер
#sudo docker rmi 2b2f4c5f7715 удалить образ
#sudo docker cp 23bbaa12ce9b:"app/screen.png" "/home/serj52/PycharmProjects/docker_work/" Скопировать из контейнера файл в директорию
#sudo docker run -v /home/serj52/PycharmProjects/attach/readme.txt:/app/readme.txt --name fish app Расшарить файл
#docker run --rm -v /home/serj52/PycharmProjects/docker_work/source:/app/source --name my_web app Расшарить папку
#sudo docker volume rm app
#sudo docker volume create my-vol
#sudo docker volume inspect my-vol
#df -h


FROM python:3.8

#Добавляем ключи для репозитория
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#Добавляем Google Chrome в репозиторий
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip
#Качаем Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
#Распаковываем файл с драйвером
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
#Устанавливаем переменную окружения
ENV DISPLAY=:99

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
# RUN pip install selenium
RUN pip install exchangelib
# VOLUME /my-vol
CMD ["python", "app.py"]



