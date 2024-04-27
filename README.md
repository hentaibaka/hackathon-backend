# hackathon-backend
***
### Требования к ПО:
1. Python: 3.10
***
### Как запустить:
1. Сборка Django:
> Powershell:
> ```powershell
> ./setup/build.ps1
> ```

> Bash:
> ```bash
> source setup/build.sh
> ```
2. Запуск Django:
    * Через ```runserver```:
    >Powershell:
    >```powershell
    >py manage.py runserver --nostatic
    >```
    
    >Bash:
    >```bash
    >-
    >```
    * Через ```uvicorn```:
    >Powershell:
    >```powershell
    >uvicorn nul_sii_site.asgi:application --host 127.0.0.1 --port 8800 --reload --log-level info
    >```
    
    >Bash:
    >```bash
    >-
    >```
    * Через ```VS Code debug```:\
    ![image](https://github.com/hentaibaka/handwriting-recognition-service-backend/assets/61946499/a8d5754a-68c6-4f5b-a1f0-e5912240634a)\
    ![image](https://github.com/hentaibaka/handwriting-recognition-service-backend/assets/61946499/e39a1df1-6fa0-4678-850f-422394fcabf3)
      * Django Runserver:
      > То же самое, что и ```runserver```, но в отладочном режиме.
      * Django ASGI:
      > То же самое, что и ```uvicorn```, но в отладочном режиме.

    Конфигурации отладочного режима доступны в [launch.json](.vscode/launch.json)
***
### Сброс Базы Данных:
Восстановить Базу Данных до начального состояния можно с помощью:
> Powershell:
> ```powershell
> ./setup/config_db.ps1
> ```

> Bash:
> ```bash
> -
> ```

Все базовые записи и настройки находятся в [adminuser.py](setup/adminuser.py)
***
### Тестовые пользователи:
| Права доступа | Логин | Пароль |
| :-| :- | :- |
| Суперпользователь | superuser | superuser |
***
### Пути:
1. /api/questions/ - [GET] возращает активные вопросы
2. /api/questions/\<int:id\>/ - [GET] возращает вопрос по id
3. /api/courses/ - [GET] возващает список курсов
4. /api/courses/\<int:id\>/ - [GET] возващает курс по id
5. /api/answers/ - [GET] возвращает список ответов | [POST] создаёт ответ
6. /api/answers/\<int:id\>/ - [GET] возвращает ответ по id
7. /api/data/ - [GET] возвращает список "опросников" | [POST] создаёт "Опросник"
8. /api/data/\<int:id\>/ - [GET] возвращает "опросник" по id
***
### Воркфлоу бота:
1. запрос на /api/courses/ [GET] - пользователь выбирает по какому курсу даёт отзыв
2. /api/questions/ [GET] - бот задаёт вопросы
3. /api/answers/ [POST] - бот записывает ответы в бд
4. /api/data/ [POST] - бот создаёт опросник
