# Json_API_aiohttp
Json api сервис на aiohttp

##### _разработка Spiridonov R.A aka Speccy_


## Описание проекта:
### Json api сервис на aiohttp с валидацией данных

Используемые библиотеки:

* aiohttp — фреймворк для создания web-приложений
* pydantic — классы, которые позволяют декларативно описывать данные и валидировать их
* valdec — декоратор для валидации аргументов и возвращаемых значений у функций

#### Build image:

```bash
docker build -t api_service . 
```

- The simple service:

```bash
docker run -e RS="run_simple.py" --rm -it -p 5000:5000 --name api_service api_service
```

- The service whose handlers can have different arguments:

```bash
docker run -e RS="run_kwargs.py" --rm -it -p 5000:5000 --name api_service api_service
```

- The service where requests and responses have a wrap and the data is validated:

```bash
docker run -e RS="run_wraps.py" --rm -it -p 5000:5000 --name api_service api_service
