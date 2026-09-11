import sys

ERROR = '❌'
OK = '✅'
TODO = '🛠️'
WARN = '⚠️️'

def fatal(msg: str) -> None:
    sys.exit(f'{ERROR} {msg}')

def ok(msg: str) -> None:
    print(f'{OK}  {msg}')

def todo(msg: str) -> None:
    print(f'{TODO}  {msg}')

def warn(msg: str) -> None:
    print(f'{WARN}  {msg}')
