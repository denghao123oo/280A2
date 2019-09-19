import mysql.connector
from drones import Drone, DroneStore

class Application(object):
    """ Main application wrapper for processing input. """

    def __init__(self, conn):
        self._drones = DroneStore(conn)
        self._commands = {
            'list': self.list,
            'add': self.add,
            'update': self.update,
            'remove': self.remove,
            'allocate': self.allocate,
            'help': self.help,
        }

    def main_loop(self):
        print('Welcome to DALSys')
        cont = True
        while cont:
            val = input('> ').strip().lower()
            cmd = None
            args = {}
            if len(val) == 0:
                continue

            try:
                parts = val.split(' ')
                if parts[0] == 'quit':
                    cont = False
                    print('Exiting DALSys')
                else:
                    cmd = self._commands[parts[0]]
            except KeyError:
                print('!! Unknown command "%s" !!' % (val))

            if cmd is not None:
                args = parts[1:]
                try:
                    cmd(args)
                except Exception as ex:
                    print('!! %s !!' % (str(ex)))

    def add(self, args):
        self._drones.add(args)

    def allocate(self, args):
        """ Allocates a drone to an operator. """
        raise Exception("Allocate method has not been implemented yet")

    def help(self, args):
        """ Displays help information. """
        print("Valid commands are:")
        print("* list [- class =(1|2)] [- rescue ]")
        print("* add 'name ' -class =(1|2) [- rescue ]")
        print("* update id [- name ='name '] [- class =(1|2)] [- rescue ]")
        print("* remove id")
        print("* allocate id 'operator'")

    def list(self, args):
        self._drones.list_all(args)
        

    def remove(self, args):
        """ Removes a drone. """
        raise Exception("Remove method has not been implemented yet")

    def update(self, args):
        if args is None:
            print('ID is required')
        else:
            if args[0
        
        


if __name__ == '__main__':
    conn = mysql.connector.connect(user='zden678',
                                   password='e43d7786',
                                   host='studdb-mysql.fos.auckland.ac.nz',
                                   database='stu_zden678_COMPSCI_280_C_S2_2019')
    app = Application(conn)
    app.main_loop()
    conn.close()
