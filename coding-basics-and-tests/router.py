hostname = "GLO"


class Router():
    hostname = None
    model = None
    version = None
    ip = None
    __serial = None

    def __init__(self, serial):
        self.__serial = serial

    def alterar_hostname(self, new_hostname):
        self.hostname = new_hostname
        self.__metodo_privado()

    def __metodo_privado(self):
        print("OI")

    def print(self):
        print(self.hostname)
        print(self.ip)
        print(self.model)
        print(self.__serial)


r1 = Router(serial="675765765786")
r1.__serial = "99999"
r1.alterar_hostname("R3")
r1.print()
