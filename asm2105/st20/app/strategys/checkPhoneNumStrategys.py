from abc import ABC, abstractmethod

class BaseCheckPhoneNumStrategy(ABC):
    @abstractmethod
    def check(self, phone):
        pass


class CheckMobilePhoneNumWithPlusStrategy(BaseCheckPhoneNumStrategy):
    def check(self, phone:str):
        if len(phone)==12 and phone[1:].isdigit():
            return True
        else: return False