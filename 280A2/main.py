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
        cursor = connection.cursor()
        if args is None:
            print('!! name is required !!')
        elif args[1] is None:
            print('!! class is required !!')
        else:
            dname = args[0]
            dclass = args[1][7]
            if args[2] is not None:
                DroneStore.add(Drone(dname, class_type = int(dclass), rescue = true))
                query = 'select * from drone_info where drone_name = ' + dname + ' and class_type = ' + dclass + ' and rescue = "yes"'
                cursor.execute(query)
                records = cursor.fetchall()
                for row in records:
                    id = str(row[0])
                    print('Added rescue drone with ID 000'+id)
            else:
                DroneStore.add(Drone(dname, class_type = int(dclass), rescue = false))
                query = 'select * from drone_info where drone_name = ' + dname + ' and class_type = ' + dclass
                cursor.execute(query)
                records = cursor.fetchall()
                for row in records:
                    id = str(row[0])
                    print('Added drone with ID 000'+id)
                
        
        
        raise Exception("Add method has not been implemented yet")

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
        query = 'select * from drone_info'
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        n = 0

        
        if args is None:
            print('ID Name Class Rescue Operator')
            for row in records:
                print(*row)
                n += 1
            print(n, 'drones listed')
        else: 
            if args[0] == '-rescue':
                new_query = 'select * from drone_info where rescue = "yes"'
            else:
                dclass = int(args[0][7])
                if dclass != 1 or 2:
                    print('Unknown drone class n')
                    return
                new_query = 'select * from drone_info where class_type = ' + str(dclass)
            cursor.execute(new_query)
            info = cursor.fetchall()
            if info is not None:
                for row in info:
                    print(*row)
                    n += 1
                print(n, 'drones listed')
            else:
                print('!! There are no drones for this criteria !!')
            
        

    def remove(self, args):
        """ Removes a drone. """
        raise Exception("Remove method has not been implemented yet")

    def update(self, args):
        """ Updates the details for a drone. """
        raise Exception("Update method has not been implemented yet")


if __name__ == '__main__':
    conn = mysql.connector.connect(user='zden678',
                                   password='e43d7786',
                                   host='studdb-mysql.fos.auckland.ac.nz',
                                   database='stu_zden678_COMPSCI_280_C_S2_2019')
    app = Application(conn)
    app.main_loop()
    conn.close()
