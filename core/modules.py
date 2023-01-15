from dataclasses import dataclass
import time
from typing import Protocol


class Info(Protocol):

    @staticmethod
    def _get_date(seconds: float) -> str:
        raise NotImplementedError

    @property
    def get_c_date(self) -> str:
        raise NotImplementedError

    @property
    def get_m_date(self) -> str:
        raise NotImplementedError

    @property
    def get_name(self) -> str:
        raise NotImplementedError


@dataclass
class DirInfo:
    created_at: float
    modified_at: float
    name: str

    @staticmethod
    def _get_date(seconds: float) -> str:
        date = time.gmtime(seconds + 21600)
        res = f'{date.tm_mon}/{date.tm_mday}/{date.tm_year}'
        res = f'{res}  {date.tm_hour}:{date.tm_min}:{date.tm_sec}'
        return res

    @property
    def get_c_date(self) -> str:
        return self._get_date(self.created_at)

    @property
    def get_m_date(self) -> str:
        return self._get_date(self.modified_at)

    @property
    def get_name(self) -> str:
        return self.name


@dataclass
class FileInfo(DirInfo):
    file_size: int

    @property
    def get_size(self) -> str:
        return str(self.file_size)
