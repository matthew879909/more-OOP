from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)
@abstractmethod
def task(self):
    print("We are inside the Adsclass task")
class text_class(Absclass):
    def task(self):
        print("We are inside test_class task")
test_obj = text_class()
test_obj.task()
test_obj.print(100)
        