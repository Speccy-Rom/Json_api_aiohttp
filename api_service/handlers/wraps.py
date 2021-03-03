from typing import Any, List, Union
from uuid import UUID, uuid4

from aiohttp import web
from valdec.decorators import async_validate as validate

from api_service.data_classes.person import PersonCreate, PersonInfo


@validate("data", "return")
async def create(
    data: Union[PersonCreate, List[PersonCreate]], storage: dict,
) -> Union[PersonInfo, List[PersonInfo]]:
    """ Создает запись или несколько записей о персоне и сохраняет в хранилище.
        Возвращает созданную запись или их список.
    """
    data_is_list = isinstance(data, list)

    persons = data if data_is_list else [data, ]

    result = []
    for person in persons:
        person_info = PersonInfo(id=uuid4(), name=person.name)

        # Добавим в хранилище новую запись
        storage[person_info.id] = person_info.dict()

        result.append(person_info)

    return result if data_is_list else result[0]


class PersonNotFound(Exception):
    pass


@validate("data", "return")
async def read(storage: dict, req: web.Request, data: UUID) -> PersonInfo:
    """ Читает запись с id=data из хранилища, и возвращает её.
    """
    # Параметр req не используется в коде этой функции, дан здесь просто
    # для примера.

    person = storage.get(data)

    if person is None:
        raise PersonNotFound(f"Person whith id={data} not found!")

    return PersonInfo(id=person["id"], name=person["name"])


@validate("info_id")
async def info(info_id: int, request: web.Request) -> Any:
    """ Информация.
    """
    return f"info_id={info_id} and request={request}"