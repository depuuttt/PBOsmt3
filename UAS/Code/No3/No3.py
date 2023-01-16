class Hewan:
    def suara(self):
        pass


class Kucing(Hewan):
    def suara(self):
        print("Meow")


class Anjing(Hewan):
    def suara(self):
        print("Woof")


def main():
    hewan1 = Kucing()
    hewan2 = Anjing()
    hewan3 = Kucing()

    hewan1.suara()  # akan mencetak "Meow"
    hewan2.suara()  # akan mencetak "Woof"
    hewan3.suara()  # akan mencetak "Meow"


if __name__ == "__main__":
    main()
