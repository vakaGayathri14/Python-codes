# static methods
# class methods

# class Calender:
#     def __init__(self) -> None:
#         self.events = []

#     def add_event(self,event_name):
#         self.events.append(event_name)

#     def display_events(self):
#         print(f"Events = {self.events}")

# obj1 = Calender()
# obj1.add_event("Honey")
# obj1.add_event("is")
# obj1.add_event("Studying")
# obj1.display_events()


# static method : need a decorator which is @static method
from datetime import datetime


class Calender:
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event_name):
        self.events.append(event_name)

    def display_events(self):
        print(f"Events = {self.events}")

    # static method is which doesn't not depend on the object it is called static method
    @staticmethod  # we have written this static method inside the class but this static method cannot able to access class variables and also you don't need to write self in parameters
    def is_weekend(date: datetime):
        if date.weekday()> 4: # weekend is a built in method which we get from datetime 
            print("It is a weekend")
        else:
            print("It is a weekday")


obj1 = Calender()
obj1.add_event("Honey")
obj1.add_event("is")
obj1.add_event("Studying")
obj1.display_events()

current_date = datetime.now()
Calender.is_weekend(current_date)