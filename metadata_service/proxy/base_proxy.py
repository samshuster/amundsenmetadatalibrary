from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Union

from amundsen_common.models.table import Table
from amundsen_common.models.user import User as UserEntity

from metadata_service.entity.popular_table import PopularTable
from metadata_service.util import UserResourceRel


class BaseProxy(metaclass=ABCMeta):
    """
    Base Proxy, which behaves like an interface for all
    the proxy clients available in the amundsen metadata service
    """
    @abstractmethod
    def get_user(self, *, id: str) -> Union[UserEntity, None]:
        pass

    @abstractmethod
    def get_users(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def get_table(self, *, table_uri: str) -> Table:
        pass

    @abstractmethod
    def delete_owner(self, *, table_uri: str, owner: str) -> None:
        pass

    @abstractmethod
    def add_owner(self, *, table_uri: str, owner: str) -> None:
        pass

    @abstractmethod
    def get_table_description(self, *,
                              table_uri: str) -> Union[str, None]:
        pass

    @abstractmethod
    def put_table_description(self, *,
                              table_uri: str,
                              description: str) -> None:
        pass

    @abstractmethod
    def add_tag(self, *, table_uri: str, tag: str, tag_type: str) -> None:
        pass

    @abstractmethod
    def delete_tag(self, *, table_uri: str, tag: str, tag_type: str) -> None:
        pass

    @abstractmethod
    def put_column_description(self, *,
                               table_uri: str,
                               column_name: str,
                               description: str) -> None:
        pass

    @abstractmethod
    def get_column_description(self, *,
                               table_uri: str,
                               column_name: str) -> Union[str, None]:
        pass

    @abstractmethod
    def get_popular_tables(self, *, num_entries: int) -> List[PopularTable]:
        pass

    @abstractmethod
    def get_latest_updated_ts(self) -> int:
        pass

    @abstractmethod
    def get_tags(self) -> List:
        pass

    @abstractmethod
    def get_table_by_user_relation(self, *, user_email: str,
                                   relation_type: UserResourceRel) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_frequently_used_tables(self, *, user_email: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def add_table_relation_by_user(self, *,
                                   table_uri: str,
                                   user_email: str,
                                   relation_type: UserResourceRel) -> None:
        pass

    @abstractmethod
    def delete_table_relation_by_user(self, *,
                                      table_uri: str,
                                      user_email: str,
                                      relation_type: UserResourceRel) -> None:
        pass
