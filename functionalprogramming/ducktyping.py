class Pycharm:
    def open(self):
        print("open methode in pycharm")
    def run(self):
        print("run funtlty in pycharm")
    def debug(self):
        print("debug funcnlty in pycharm")

class Jupiter:
    def open(self):
        print("open methode in Jupiter")

    def run(self):
        print("run funtlty in Jupiter")

    def debug(self):
        print("debug funcnlty in Jupiter")
class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharm()
pg=Programmer()
pg.coding(py)
print("*****************************************************")
ju=Jupiter()
pg.coding(ju)