from datetime import datetime
from typing import Callable


class Action:
    pass


class Tag:
    __count: int = 0

    def __init__(self, title: str, description: str, context: dict):
        self.__title = title
        self.__description = description
        self.__tag_id = context.get('tag_count', 0)
        context['tag_count'] = self.__tag_id + 1

    @property
    def tag_id(self) -> int:
        return self.__tag_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    def __str__(self) -> str:
        return self.__title


class TagSet:

    def __init__(self):
        self.__tags: dict[str, Tag] = dict()
        self.__listeners = list()

    def __contains__(self, other):
        if not isinstance(other, Tag):
            return False

        else:
            return str.lower(other.title) in self.__tags

    def add(self, tag: Tag):
        if not isinstance(tag, Tag):
            raise TypeError("Set of tags can only contain tags.")

        if tag in self:
            return False

        else:
            self.__tags[str.lower(tag.title)] = tag
            self.__notify_listeners(None, tag)

            return True

    def add_listener(self, listener: Callable):
        self.__listeners.append(listener)

    def remove_listener(self, listener):
        self.__listeners.remove(listener)

    def delete(self, tag: Tag):
        if tag not in self:
            return False

        del self[tag.title]
        self.__notify_listeners(tag, None)

    def __notify_listeners(self, old, new):
        for listener in self.__listeners:
            listener(old, new)

    def __delitem__(self, tag: str | Tag):
        if isinstance(tag, Tag):
            name = tag.title
        elif isinstance(tag, str):
            name = tag
        else:
            raise TypeError("Must be string or Tag instance.")

        del self.__tags[str.lower(name)]

    def __iter__(self):
        return iter(self.__tags.values())

    def clear(self):
        self.__tags.clear()


class Storage:

    def ___init__(self, name: str, description: str, resource: str):
        self._name = name
        self._description = description
        self._resource = resource

    @property
    def description(self) -> str:
        return self._description

    @property
    def name(self) -> str:
        return self._name

    def append(self, timestamp: datetime, action, tags: list[Tag] = []):
        """ Log action with timestamp in storage. """
        raise NotImplementedError()

    def get(self, timerange: tuple[datetime, datetime]) -> dict:
        pass

    def remove(self, timestamp: datetime):
        """ Delete log entry matching timestamp. """
        raise NotImplementedError()
