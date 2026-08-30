from __future__ import absolute_import
import typing
TData = typing.TypeVar(b'TData')
TDataFactory = typing.Callable[[], TData]
TPDCVersion = typing.Tuple[str, ...]
