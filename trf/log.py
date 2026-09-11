import sys

ERROR = '❌'
INFO = 'ℹ️' # noqa
OK = '✅'
WARN = '⚠️️'

def fatal(msg: str) -> None:
    sys.exit(f'{ERROR} {msg}')

def ok(msg: str) -> None:
    print(f'{OK}  {msg}')

def info(msg: str) -> None:
    print(f'{INFO}  {msg}')

def warn(msg: str) -> None:
    print(f'{WARN}  {msg}')
