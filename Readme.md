# Куда пойти

Проект сайта на фреймворке Django о самых интересных местах в Москве.

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки ([документация](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DEBUG)).
- `SECRET_KEY` — секретный ключ проекта ([документация](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY)).
- `ALLOWED_HOSTS` - список хостов, с которых разрешено подключение ([документация](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts)).
- `STATIC_ROOT` - путь к директории, в которую будет собрана статика при деплое проекта ([документация](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-STATIC_ROOT)).

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```bash
pip install -r requirements.txt
```
Далее необходимо применить миграции командой
```bash
python manage.py migrate
```
Теперь можно запустить сервер
```bash
python3 manage.py runserver
```
При выполнении деплоя проекта на сервер, необходимо указать в параметре окружения `STATIC_ROOT` каталог для сбора статики
и выполнить команду
```bash
python3 manage.py collectstatic
```

### Интерфейс администратора
Для того чтобы создать пользователя с правами администратора, необходимо выполнить команду
```bash
python3 manage.py createsuperuser
```
Далее, необходимо ввести логин, пароль и e-mail (опционально).

Теперь вы можете зайти в интерфейс администратора по адресу http://127.0.0.1:8000/admin/
В админке вы можете добавить новые места на карту или загрузить дополнительные изображения к существующим.
Для этого необходимо выбрать сущность (Places или Images) и далее нажать кнопку "Add place"/"Add image" 
![image](https://user-images.githubusercontent.com/79382246/188517208-09151d3c-0584-4150-b0e8-b80df34aa5e6.png)

### Тестовые данные
Сайт можно наполнить тестовыми данными из сервиса [KudaGo](https://kudago.com/), для этого необходимо выполнить команду
```bash
python3 manage.py load_place
```
Для загрузки произвольного файла, можно указать URL в параметре команды
```bash
python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Японский%20сад.json
```
JSON файл должен иметь следующую структуру:
```json
{
  "title": "Японский сад",
  "imgs": [
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/52aea6b37037f7aab7cc82301f77e314.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3cce16840a41f2eafbe47ac72a61da12.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6b3a9e0c004531ca87414eefe1a93509.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/618dc376701574400887d909b5c80f1e.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/761adc74dd5f348d3e7c34d12bee8d24.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/21d6835554ca82259ff201af7da32fe3.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/2095714fb0148a8be9140aadaad302be.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/34b72d0d1819947fe385d0a1986dc962.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6c07645902cc90a2839b63896645021a.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/9b3bc5b446f1aaa8eeed2bb81a04d472.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/9c32261372fa061aad9b1f8827f87b7f.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0cd397dc43f864e55dc1ef458ead9d69.jpg"
  ],
  "description_short": "Удивительное и романтичное место, где вы сможете в полной мере ощутить единение человека и природы.",
  "description_long": "<p>Японский сад был торжественно открыт в 1987 году как дар Японии Советскому Союзу. Он стал живописной иллюстрацией японской культуры, в основе которой лежит идея единения человека и природы. Большое внимание в оформлении уделили символическим элементам, благодаря которым пейзаж превратится в величественное святилище, которое не терпит суеты и праздности. Здесь приятно прогуливаться по дорожкам, или, сидя напротив цветущей сакуры, размышлять о бытии, которое в этом чудесном уголке отделяется от лихорадочного московского шума и течёт в размеренном, непривычном ритме.</p><p>Японский сад открыт с конца апреля до середины октября, вход платный. Стоимость входных билетов для взрослых по вторникам, средам и пятницам — 250 рублей, для студентов и детей старше семи лет — 100 рублей, для пенсионеров — 50 рублей. По субботам и воскресеньям взрослые могут посетить сад за 300 рублей, дети — за 150 рублей, пенсионеры — за 50 рублей. С малышей до семи лет плата не взимается. По вторникам с 12:00 до 15:00 вход для пенсионеров, инвалидов и многодетных семей бесплатный. По понедельникам и четвергам сад закрыт для посетителей.</p><p>В Японском саду проводятся экскурсии для индивидуальных посетителей и групп продолжительностью 60 минут, стоимость — 500 рублей с человека. За 1500 рублей можно посетить полуторачасовую экскурсию-лекцию, посвящённую садовой культуре Японии.</p>",
  "coordinates": {
    "lng": "37.58996699999999",
    "lat": "55.84419699999997"
  }
}
```
### Демонстрационная копия сайта
https://sputnik555.pythonanywhere.com/
![image](https://user-images.githubusercontent.com/79382246/187556064-1f6cc865-4658-4e74-bf84-e6dbfa82f28e.png)
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
