# Django REST API для Загрузки и Обработки Файлов

Это проект на Django, предоставляющий REST API для загрузки файлов на сервер и их асинхронной обработки с использованием Celery.

## Начало Работы

Следуйте этим инструкциям, чтобы настроить и запустить проект локально.

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Markporsh/upload_files.git
   cd upload_files
   ```

2. Создайте файл `.env` в корневой директории и определите следующие переменные окружения:

   ```bash
    SECRET_KEY="SOME_SECRET_KEY"
    DEBUG=False
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    REDIS_URL=redis://redis:6379/1
   ```

3. Соберите и запустите Docker контейнеры:

   ```bash
   make up
   ```

4. Создайте и примените миграции базы данных:

   ```bash
   maek makemigrations
   make migrate
   ```

5. Создайте суперпользователя для доступа к админ-панели Django:

   ```bash
   make createsuperuser
   ```

6. Для доступа к админ-панели перейдите по ссылке [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Залить файл в приложение
Можно с помощью консоли
   ### Так мы загрузим файл requirements на наш сервер
   ```bash
   curl -X POST -F "file=@requirements.txt" http://localhost:8000/upload/
   ```

   ### Можно с помощью Postman
   1. Введя URL localhost:8000/upload/
   2. Перейти во вкладку Body 
   3. Выбрать form-data, и указав тип поля как File.
   4. Затем выберите файл, который хотите загрузить, и отправьте запрос.


## API Эндпоинты

### Загрузка Файла

- URL: `/upload/`
- Метод: POST
- Описание: Загрузка файла для обработки.
- Тело Запроса: Форма с полем файла с именем `file`.
- Ответ: Сериализованные данные загруженного файла.

### Список Файлов

- URL: `/files/`
- Метод: GET
- Описание: Получение списка всех загруженных файлов.
- Ответ: Сериализованные данные всех загруженных файлов.

## Задача Celery

Задача Celery используется для асинхронной обработки загруженных файлов. В данном случае, в качестве примера обработки, вычисляется сумма квадратов чисел от 0 до 9999.

## Команды Makefile

- `make up`: Собрать и запустить Docker контейнеры.
- `make down`: Остановить и удалить Docker контейнеры.
- `make build`: Пересобрать Docker контейнеры.
- `make bash`: Войти в оболочку контейнера с приложением.
- `make makemigrations`: Создать миграции базы данных.
- `make migrate`: Применить миграции базы данных.
- `make createsuperuser`: Создать суперпользователя для админ-панели Django.
- `make celery logs`: Просмотреть логи Celery worker.
- `make logs`: Просмотреть логи приложения.
- `make test`: Запуск тестов.

## Масштабирование для Высокой Нагрузки

Для обработки высокой нагрузки вы можете рассмотреть следующие архитектурные изменения:

1. Использование балансировщика нагрузки для распределения входящих запросов на несколько экземпляров серверов приложений.
2. Масштабирование Celery: Вы можете настроить множество рабочих узлов Celery
для обработки большого количества асинхронных задач параллельно. Это позволит обработать больше файлов одновременно.
3. Использование RabbitMQ или другого брокера сообщений: Переход на более масштабируемый брокер сообщений,
такой как RabbitMQ, может улучшить производительность обработки задач.
4. Кэширование: Если ваша обработка файлов включает в себя длительные операции,
то можно рассмотреть использование кэширования результатов обработки, чтобы избежать повторных вычислений.
