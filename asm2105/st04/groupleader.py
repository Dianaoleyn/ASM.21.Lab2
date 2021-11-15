from abc import ABC
from dataclasses import dataclass

from asm2105.st04.member import Member


@dataclass()
class GroupLeader(Member, ABC):
    type: str = 'Староста'
    stipend: int = 4000

    def getData(self, id):
        super(GroupLeader, self).getData(id)