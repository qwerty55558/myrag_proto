import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRequest(_message.Message):
    __slots__ = ("query", "current_timestamp", "k", "session_id", "user_id", "access_token")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    query: str
    current_timestamp: _timestamp_pb2.Timestamp
    k: int
    session_id: str
    user_id: str
    access_token: str
    def __init__(self, query: _Optional[str] = ..., current_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., k: _Optional[int] = ..., session_id: _Optional[str] = ..., user_id: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ("token", "is_final", "sources")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    token: str
    is_final: bool
    sources: _containers.RepeatedCompositeFieldContainer[SourceDocument]
    def __init__(self, token: _Optional[str] = ..., is_final: bool = ..., sources: _Optional[_Iterable[_Union[SourceDocument, _Mapping]]] = ...) -> None: ...

class SourceDocument(_message.Message):
    __slots__ = ("title", "uri", "score")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    title: str
    uri: str
    score: float
    def __init__(self, title: _Optional[str] = ..., uri: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...

class IndexDocumentsRequest(_message.Message):
    __slots__ = ("drive_folder_id", "access_token", "user_id")
    DRIVE_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    drive_folder_id: str
    access_token: str
    user_id: str
    def __init__(self, drive_folder_id: _Optional[str] = ..., access_token: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class IndexDocumentsResponse(_message.Message):
    __slots__ = ("chunk_count", "files", "message")
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    chunk_count: int
    files: _containers.RepeatedScalarFieldContainer[str]
    message: str
    def __init__(self, chunk_count: _Optional[int] = ..., files: _Optional[_Iterable[str]] = ..., message: _Optional[str] = ...) -> None: ...

class ListDocumentsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ListDocumentsResponse(_message.Message):
    __slots__ = ("documents",)
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[IndexedDocument]
    def __init__(self, documents: _Optional[_Iterable[_Union[IndexedDocument, _Mapping]]] = ...) -> None: ...

class IndexedDocument(_message.Message):
    __slots__ = ("document_id", "file_name", "source_uri", "chunk_count", "indexed_at")
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    INDEXED_AT_FIELD_NUMBER: _ClassVar[int]
    document_id: str
    file_name: str
    source_uri: str
    chunk_count: int
    indexed_at: _timestamp_pb2.Timestamp
    def __init__(self, document_id: _Optional[str] = ..., file_name: _Optional[str] = ..., source_uri: _Optional[str] = ..., chunk_count: _Optional[int] = ..., indexed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetSupportedFormatsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSupportedFormatsResponse(_message.Message):
    __slots__ = ("formats",)
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    formats: _containers.RepeatedCompositeFieldContainer[SupportedFormat]
    def __init__(self, formats: _Optional[_Iterable[_Union[SupportedFormat, _Mapping]]] = ...) -> None: ...

class SupportedFormat(_message.Message):
    __slots__ = ("extension", "description")
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    extension: str
    description: str
    def __init__(self, extension: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class DeleteDocumentsRequest(_message.Message):
    __slots__ = ("document_ids", "user_id")
    DOCUMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    document_ids: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, document_ids: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeleteDocumentsResponse(_message.Message):
    __slots__ = ("deleted_count", "message")
    DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    deleted_count: int
    message: str
    def __init__(self, deleted_count: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
