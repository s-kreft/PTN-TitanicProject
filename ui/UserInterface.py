
class UserInterface:
    def __init__(self, service):
        self.service = service
    def init_message(self):
        #self.service.titanic_data()
        print("|----------------------------------------------------------|\n"
              "|            Witaj w programie Titanic Data                |\n"
              "|**********************************************************|\n"             
              "|Wyświetlenie danych - wybierz 1                           |\n"
              "|Filtrowanie danych wg płci - wybierz 2                    |\n"
              "|DO POPRAWY Przeszukaj dane - wybierz 3                    |\n"
              "|Filtrowanie danych wg wieku - wybierz 4                    |\n"
              "|Wyświetlenie wykresu słupkowego dla wieku - wybierz 5     |\n"
              "|Zresetowanie wyszukiwania - wybierz 6                     |\n"
              "|Wyjdź z programu - wybierz q                              |\n"
              "|----------------------------------------------------------|")
    def switch(self):
        running = True
        while running == True:
            self.init_message()
            user_input = input("Wybierz akcję\n")
            if user_input == "1":
                self.service.show_titanic_data()
                print("Wybrałeś 1")
            elif user_input == "2":
                gender_input = input("Wybierz k żeby wyszukać kobiety lub m żeby wyszukać męższczyzn")
                self.service.search_gender_titanic_data(gender_input)
                print("Wybrałeś 2")
            elif user_input == "3":
                self.service.search_titanic_data()
                print("Wybrałeś 3")
            elif user_input == "4":
                search_input = input("Podaj wartość\n")
                self.service.search_titanic_age(search_input)
                print("Wybrałeś 4")
            elif user_input == "5":
                self.service.titanic_age_plot()
                print("Wybrałeś 5")
            elif user_input == "6":
                self.service.data_frame_reset()
                print("Wybrałeś 6")
            elif user_input == "q":
                running = False
                print("Wyszedłeś z programu")
            else:
                print("Akcja niedozwolona")