from typing import Any, Callable, Iterable, NewType, Optional, Protocol, Text, Union

# Anything that can be called with arbitrary arguments
# TODO: Is it possible to genericise the callable such that functions like wsgi.responder can assert they return a
#       function with the same signature as their argument?
AnyCallable = Callable[..., Any]

# Anything that can be called with zero arguments only
# TODO: Is this worth genericising?
NoArgCallable = Callable[[], Any]

# Anything that can be usefully passed as the argument to the builtin `iter(...)`.
# TODO: Is it possible to genericise this on _T to constrain those types that builds on it?
Iter = NewType('Iter', Union[Iterable[Any], NoArgCallable])

class Readable(Protocol):
    """
    Readable is the Typeshed-specific Protocol that describes the file-like operations Werkzeug expects to be able to
    use in a few different areas.

    They have slightly different signatures from Python's usual `read` and `readline`; namely that they take an
    `Optional[int]` size limit, where the standard lib will want a bare `int` as the kwarg. This also makes them
    incompatible with the input streams of PEP 3333, and Typeshed's own helper type `wsgiref.types._Readable`.
    """
    def read(self, size: Optional[int]) -> Optional[Text]: ...
    # TODO: Where was this one used again?
    def readline(self, size: Optional[int]) -> Optional[Text]: ...

class EnvironProp(Protocol):
    """
    EnvironProp is the Typeshed-specific Protocol that describes anything that has an `environ` attribute. Werkzeug
    expects to be able to find `environ` on a lot of object-alikes.
    """
    # TODO: What's the type `environ`?
    environ: ...

class HeadersProp(Protocol):
    """
    HeadersProp is the Typeshed-specific Protocol that describes anything that has a `headers` attribute. Werkzeug
    expects to be able to find `headers` on a lot of object-alikes.
    """
    # TODO: What's the type of `headers`?
    headers: ...

class HTMLProp(Protocol):
    """
    HTMLProp is the Typeshed-specific Protocol that describes anything that carries the no-arg function `__html__()`.
    Werkzeug sometimes uses this in lieu of a a text type when it can carry some more semantic information.
    """
    def __html__(self) -> Text: ...