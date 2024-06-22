from service.Service import Service
from ui.UserInterface import UserInterface

def main():
    service = Service()
    user_interface = UserInterface(service)

    user_interface.init_message()
    user_interface.switch()


if __name__=="__main__":
    main()