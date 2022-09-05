# Куда пойти

Проект сайта на фреймворке Django о самых интересных местах в Москве.

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки ([документация](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DEBUG)).
- `SECRET_KEY` — секретный ключ проекта ([документация](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY))
- `ALLOWED_HOSTS` - список хостов, с которых разрешено подключение [документация](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts).
- `STATIC_ROOT` - путь к директории, в которую будет собрана статика при деплое прокта [документация](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-STATIC_ROOT).

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
и выполнить комманду
```bash
python3 manage.py collectstatic
```

### Интерфейс администратора
Для того чтобы создать пользователя с правами администратора, нобходимо выполнить комманду
```bash
python3 manage.py createsuperuser
```
далее, необходимо ввести логин, пароль и e-mail (опционально).

Теперь вы можете зайти в интферфейс администратора по адресу http://127.0.0.1:8000/admin/.
В админке вы можете добавить новые места на карту или загрузить дополнительные изображения к существующим.
Для этого необходимо выбрать сущность (Places или Images) и далее нажать кнопку "Add place"/"Add image" 
![image](https://user-images.githubusercontent.com/79382246/188517208-09151d3c-0584-4150-b0e8-b80df34aa5e6.png)

### Тестовые данные
Сайт можно наполнить тестовыми данными из севиса [KudaGo](https://kudago.com/), для этого необходимо выполнить комманду
```bash
python3 manage.py load_place
```

### Демонстрационная копия сайта
https://sputnik555.pythonanywhere.com/
![image](https://user-images.githubusercontent.com/79382246/187556064-1f6cc865-4658-4e74-bf84-e6dbfa82f28e.png)
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
