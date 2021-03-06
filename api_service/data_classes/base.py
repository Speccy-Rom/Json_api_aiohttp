""" Базовый класс данных для api."""

from pydantic import BaseModel, Extra


class BaseApi(BaseModel):
    """ Базовый класс данных для api."""

    class Config:
        extra = Extra.forbid
