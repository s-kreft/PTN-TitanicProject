
class UserInterface:
    def __init__(self, service):
        self.service = service
    def InitMessage(self):
        print("Witaj w programie Titanic Data")

    def Switch(self):
        user_input = input("Wybierz akcję\n")
        if user_input == "1":
            self.service.TitanicData()
            return print("Wybrałeś 1")
        elif user_input == "2":
            return "Wybrałeś 2"
        elif user_input == "3":
            return "Wybrałeś 3"
        elif user_input == "4":
            return "Wybrałeś 4"
        elif user_input == "5":
            return "Wybrałeś 5"
        elif user_input == "q":
            return "Wyszedłeś z programu"
        else:
            "Akcja niedozwolona"