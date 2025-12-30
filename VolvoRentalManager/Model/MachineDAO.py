from Database.DBConnect import get_connection
from Model.Machine import Machine


class MachineDAO:
    def get_all_machines(self):
        """
        Selects all records of machines in database.
        :return: list of objects Machine
        """
        connection = get_connection()
        cursor = connection.cursor()
        machines = []
        try:
            query = """select m.id, m.model, m.weight, m.is_available, c.name from Machines m 
            join Categories c on m.id_category = c.id 
            order by m.id_category
            """
            cursor.execute(query)

            for row in cursor:
                machine = Machine(row[0], row[1], row[2], row[3], row[4])
                machines.append(machine)
            return machines
        except Exception as e:
            print(f"Something went wrong with creating Machine objects. - {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def get_machine(self, m_id):
        """
        Selects a machine according to set id.
        :param m_id: int number
        :return: Machine object
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = "select id, model, weight, is_available, id_category from Machine where id = :1"
            cursor.execute(query, [m_id])
            row = cursor.fetchone()
            if row:
                return Machine(row[0], row[1], row[2], row[3])
            return None
        finally:
            cursor.close()
            connection.close()

    def get_categories(self):
        """
        Selects all rows of Categories table.
        :return: list of rows (tuple)
        """
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select id, name from Categories")
        return cursor.fetchall()

    def create_machine(self, model, weight, id_category):
        """
        Connects to database and inserts machine information to table Machine.
        :param model: string name of machine
        :param weight: float number in tons
        :param id_category: id of table Categories
        :return:
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = "insert into Machines(model, weight, is_available, id_category) values(:1, :2, :3, :4)"
            cursor.execute(query, (model, float(weight), 1, int(id_category)))
            connection.commit()
            print("Machine was successfully created.")
            return True
        except ValueError:
            print("Error: Weight must be a number.")
            return False
        except Exception as e:
            print(f"Something went wrong, machine couldn't be created. - {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()

    def get_available_machines(self):
        """
        Selects all records of machines that are available.
        :return: list of objects Machine
        """
        connection = get_connection()
        cursor = connection.cursor()
        machines = []
        try:
            query = """select m.id, m.model, m.weight, m.is_available, c.name from Machines m 
            join Categories c on m.id_category = c.id 
            order by m.model
            """
            cursor.execute(query)

            for row in cursor:
                machine = Machine(row[0], row[1], row[2], row[3], row[4])
                if int(row[3]) == 1:
                    machines.append(machine)
            return machines
        except Exception as e:
            print(f"Something went wrong with creating Machine objects. - {e}")
            return []
        finally:
            cursor.close()
            connection.close()

