from service.Service import Service
from ui.UserInterface import UserInterface

def main():
    service = Service()
    user_interface = UserInterface(service)

    user_interface.Switch()


if __name__=="__main__":
    main()