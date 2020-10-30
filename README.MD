# PWS-11_F2_HR_project

### Для запуска проекта:

1. Скопировать даный репозиторий.
2. Установить зависимости из requirements.txt: pip install -r requirements.txt.
3. Создать миграции: python manage.py makemigrations.
4. Провести миграции БД: python manage.py migrate
5. Создать суперпользователя: python manage.py createsuperuser
6. Загрузить фикстуры: python manage.py loaddata data.xml
7. Запустить сервер: python manage.py runserver

Сайт будет доступен по адресу:  http://127.0.0.1:8000

В БД были созданы несколько пользователей:
admin - admin (администратор); test - test123456 (персонал); testi - test123456 (пользователь)

Также можно создать своих пользователей с помощью панели администрирования

Опросы с вопросами создаются админом/персоналом через панель администрирования.

Ссылка на сайт : http://84.201.141.199/
