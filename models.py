from settings import STORAGE_CLASS
from utils import import_string
import abc
import attr


storage = import_string(STORAGE_CLASS)


class Model(abc.ABC):
    """
    Abstract class for all Models
    """

    @abc.abstractmethod
    def as_dict(self) -> dict:
        pass


@attr.s(frozen=True)
class GeneratedUUID(Model):
    timestamp = attr.ib(kw_only=True)
    uuid = attr.ib(kw_only=True)

    def as_dict(self) -> dict:
        return {self.timestamp: self.uuid}

    def create(self):
        return storage.create(self)

    @staticmethod
    def fetch_all() -> dict:
        return storage.fetch()
