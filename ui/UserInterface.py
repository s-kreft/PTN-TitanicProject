
class UserInterface:
    def __init__(self, service):
        self.service = service
    def init_message(self):
        self.service.titanic_data()
        print("Witaj w programie Titanic Data")
        print("Inicjalizacja danych - wybierz 1\n"
              "Wyświetlenie danych - wybierz 2\n"
              "Przeszukaj dane - wybierz 3\n"
              "Filtruj po wieku - wybierz 4\n"
              "Wyświetl wykres - wybierz 5\n"
              "Wyjdź z programu - wybierz q")
    def switch(self):
        running = True
        while running == True:
            user_input = input("Wybierz akcję\n")
            if user_input == "1":
                self.service.titanic_data()
                print("Wybrałeś 1")
            elif user_input == "2":
                self.service.show_titanic_data()
                print("Wybrałeś 2")
            elif user_input == "3":
                search_input = input("Podaj wartość\n")
                self.service.search_titanic_data(search_input)
                print("Wybrałeś 3")
            elif user_input == "4":
                search_input = input("Podaj wartość\n")
                self.service.search_titanic_age(search_input)
                print("Wybrałeś 4")
            elif user_input == "5":
                self.service.titanic_age_plot()
                print("Wybrałeś 5")
            elif user_input == "q":
                running = False
                print("Wyszedłeś z programu")
            else:
                print("Akcja niedozwolona")