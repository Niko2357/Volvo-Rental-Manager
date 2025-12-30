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

    def get_machine_usage(self):
        """
        Fetches data from view Machine_usage.
        :return: list
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select model, category, times_rented, total_revenue_generated from Machine_usage")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching machine usage: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def get_rented_machines(self):
        """
        Gets all rented machines.
        :return: list
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("select id, model from Machines where is_available = 0")
            return [type('Machine', (object,), {'id': row[0], 'model': row[1]}) for row in cursor.fetchall()]
        finally:
            cursor.close()
            connection.close()

    def return_machine(self, machine_id):
        """
        Updates machine's availability to available.
        :param machine_id: number id of machine
        :return:
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("update Machines set is_available = 1 where id = :1", [machine_id])
            connection.commit()
            return True
        except Exception as e:
            print(f"Update failed: {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()
