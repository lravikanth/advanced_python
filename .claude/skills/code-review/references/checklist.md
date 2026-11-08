# Review checklist

## Correctness
- Logic errors, off-by-one, wrong return values, unhandled `None`.
- Mutable default arguments (`def f(x=[])`) and shared class-level mutable state.
- Exceptions swallowed by bare `except:` or `except Exception: pass`.
- Resource handling: files, sockets, and HTTP sessions are closed (prefer `with`).

## Naming (project rule)
- Functions, methods, variables, modules, and new file names use **snake_case**.
- Classes use PascalCase; constants use UPPER_SNAKE_CASE.
- Flag new camelCase identifiers. Mention existing ones only if they're in the reviewed change.

## Typing (Python 3.14)
- Public functions have parameter and return annotations.
- Prefer built-in generics (`list[int]`, `dict[str, int]`) and `X | None` over `typing.List` / `Optional`.
- Prefer PEP 695 syntax (`def f[T](x: T) -> T`, `class Box[T]:`, `type Alias = ...`) over `TypeVar` in new code, unless the file is specifically demonstrating `TypeVar`.

## Advanced-feature specifics
- **Decorators:** use `functools.wraps`; pass through `*args, **kwargs` and the return value.
- **Context managers:** `__exit__` returns a falsy value unless it really means to suppress exceptions; `@contextmanager` generators wrap the `yield` in `try/finally`.
- **Descriptors:** `__set_name__` is used for the storage name; per-instance state lives on the instance, not the descriptor.
- **Iterators/generators:** `__iter__` returns `self` on iterators; `StopIteration` isn't raised inside a generator; async generators are closed or fully consumed.
- **Async:** no blocking calls (`time.sleep`, `requests`) inside `async def`; tasks are awaited or gathered.
- **Protocols/ABCs:** `Protocol` classes aren't instantiated; `@runtime_checkable` is present if `isinstance` is used; ABCs mark required methods `@abstractmethod`.
- **Metaclasses / `__slots__`:** `super().__new__` / `__init__` are called; `__slots__` classes don't rely on `__dict__`; weakref use with slots includes `__weakref__`.
- **Caching:** `lru_cache` / `cache` aren't used on methods with unhashable args or where instances would be kept alive unintentionally.

## Workspace / imports
- `expense_tracker` imports `tax_calulation` (spelled that way). Don't "fix" the spelling in imports.
- Packages under `src/` use absolute package imports and must run from `src/`.
- New dependencies go in the right `pyproject.toml` (root vs. workspace member).
