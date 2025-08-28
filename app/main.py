import os
from typing import Self


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(
            self,
            exc_type: None,
            exc_value: None,
            traceback: None
    ) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            raise FileNotFoundError
