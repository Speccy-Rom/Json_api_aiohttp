""" Классы данных для Персоны."""
from uuid import UUID
from pydantic import Field, StrictStr
from base import BaseApi


class PersonCreate(BaseApi):
    """ Параметры для создания персоны."""
    name: StrictStr = Field(description="Имя.", example="Oleg")


class PersonInfo(BaseApi):
    """ Информация о персоне.
    """
    id: UUID = Field(description="Идентификатор.")
    name: StrictStr = Field(description="Имя.")