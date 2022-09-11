import enum
from typing import Generic, Optional, TypeVar, Union

from pydantic.generics import GenericModel

T = TypeVar("T")


class Status(enum.IntEnum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


class Msg(enum.Enum):
    OK = "OK"
    FAIL = "FAIL"


class Response(GenericModel, Generic[T]):
    code: Status = Status.OK
    msg: Union[Msg, str] = Msg.OK
    data: Optional[T]
