from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEmployeeRequest(_message.Message):
    __slots__ = ("short_name",)
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    short_name: str
    def __init__(self, short_name: _Optional[str] = ...) -> None: ...

class GetEmployeeResponse(_message.Message):
    __slots__ = ("employee",)
    EMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    employee: Employee
    def __init__(self, employee: _Optional[_Union[Employee, _Mapping]] = ...) -> None: ...

class ListEmployeesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEmployeesResponse(_message.Message):
    __slots__ = ("short_names",)
    SHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
    short_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, short_names: _Optional[_Iterable[str]] = ...) -> None: ...

class Employee(_message.Message):
    __slots__ = ("id", "full_name", "birthday")
    ID_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    full_name: str
    birthday: str
    def __init__(self, id: _Optional[int] = ..., full_name: _Optional[str] = ..., birthday: _Optional[str] = ...) -> None: ...
