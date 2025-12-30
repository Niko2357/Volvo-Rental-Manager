from Database.DBConnect import get_connection
from Model.Customer import Customer


class CustomerDAO:
    def get_all_customers(self):
        """
        Selects all records of customers in database.
        :return: list of objects Customer or None
        """
        connection = get_connection()
        if not connection:
            return []
        cursor = connection.cursor()
        customers = []
        try:
            query = """select id, company_name, name, surname, email, registration_date from Customers 
            order by registration_date desc"""
            cursor.execute(query)
            for row in cursor:
                c = Customer(row[0], row[1], row[2], row[3], row[4], row[5])
                customers.append(c)
            return customers
        except Exception as e:
            print(f"Something wrong with creating Customer objects. - {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def create_customer(self, company_name, name, surname, email):
        """
        Creates new record in table Customers.
        :param company_name: string name of the company
        :param name: string name of person renting
        :param surname: string surname of responsible person renting a machine
        :param email: string email of contacting person
        :return: bool
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = "insert into Customers(company_name, name, surname, email) values(:1, :2, :3, :4)"
            cursor.execute(query, [company_name, name, surname, email])
            connection.commit()
            return True
        except Exception as e:
            print(f"Couldn't add the customer. - {e}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            connection.close()
