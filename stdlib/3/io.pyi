# Stubs for io

# Based on http://docs.python.org/3.2/library/io.html

from typing import List, BinaryIO, TextIO, IO, overload, Iterator, Iterable, Any
import builtins
import codecs
import _io

DEFAULT_BUFFER_SIZE = 0  # type: int
SEEK_SET = ...  # type: int
SEEK_CUR = ...  # type: int
SEEK_END = ...  # type: int

open = builtins.open

class BlockingIOError(OSError): ...
class UnsupportedOperation(ValueError, OSError): ...

class IncrementalNewlineDecoder(codecs.IncrementalDecoder):
    newlines = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def decode(self, input, final=...): ...
    def getstate(self): ...
    def reset(self): ...
    def setstate(self, state): ...

class IOBase(_io._IOBase): ...
class RawIOBase(_io._RawIOBase, IOBase): ...
class BufferedIOBase(_io._BufferedIOBase, IOBase): ...
class TextIOBase(_io._TextIOBase, IOBase): ...

class FileIO(_io._RawIOBase):
    closefd = ...  # type: Any
    mode = ...  # type: Any
    def __init__(self, name, mode=..., closefd=..., opener=...) -> None: ...
    def readinto(self, b): ...
    def write(self, b): ...

class BufferedReader(_io._BufferedIOBase):
    mode = ...  # type: Any
    name = ...  # type: Any
    raw = ...  # type: Any
    def __init__(self, raw, buffer_size=...) -> None: ...
    def peek(self, size: int = ...): ...

class BufferedWriter(_io._BufferedIOBase):
    mode = ...  # type: Any
    name = ...  # type: Any
    raw = ...  # type: Any
    def __init__(self, raw, buffer_size=...) -> None: ...

class BufferedRWPair(_io._BufferedIOBase):
    def __init__(self, reader, writer, buffer_size=...) -> None: ...
    def peek(self, size: int = ...): ...

class BufferedRandom(_io._BufferedIOBase):
    mode = ...  # type: Any
    name = ...  # type: Any
    raw = ...  # type: Any
    def __init__(self, raw, buffer_size=...) -> None: ...
    def peek(self, size: int = ...): ...

class BytesIO(BinaryIO):
    def __init__(self, initial_bytes: bytes = ...) -> None: ...
    # TODO getbuffer
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> bytes: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> bytes: ...
    def readlines(self, hint: int = ...) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    @overload
    def write(self, s: bytes) -> int: ...
    @overload
    def write(self, s: bytearray) -> int: ...
    def writelines(self, lines: Iterable[bytes]) -> None: ...
    def getvalue(self) -> bytes: ...
    def read1(self) -> str: ...

    def __iter__(self) -> Iterator[bytes]: ...
    def __enter__(self) -> 'BytesIO': ...
    def __exit__(self, t: type = None, value: BaseException = None, traceback: Any = None) -> bool: ...

class StringIO(TextIO):
    def __init__(self, initial_value: str = ...,
                 newline: str = ...) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> str: ...
    def readlines(self, hint: int = ...) -> List[str]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: str) -> int: ...
    def writelines(self, lines: Iterable[str]) -> None: ...
    def getvalue(self) -> str: ...

    def __iter__(self) -> Iterator[str]: ...
    def __enter__(self) -> 'StringIO': ...
    def __exit__(self, t: type = None, value: BaseException = None, traceback: Any = None) -> bool: ...

class TextIOWrapper(TextIO):
    # TODO: This is actually a base class of _io._TextIOBase.
    # write_through is undocumented but used by subprocess
    def __init__(self, buffer: IO[bytes], encoding: str = ...,
                 errors: str = ..., newline: str = ...,
                 line_buffering: bool = ...,
                 write_through: bool = ...) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> str: ...
    def readlines(self, hint: int = ...) -> List[str]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: str) -> int: ...
    def writelines(self, lines: Iterable[str]) -> None: ...

    def __iter__(self) -> Iterator[str]: ...
    def __enter__(self) -> StringIO: ...
    def __exit__(self, t: type = None, value: BaseException = None, traceback: Any = None) -> bool: ...
