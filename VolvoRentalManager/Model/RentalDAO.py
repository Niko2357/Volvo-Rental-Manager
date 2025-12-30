from Database.DBConnect import get_connection


class RentalDAO:
    def create_rental(self, customer_id, machine_id, days, price, note=""):
        """
        Creates new rental and updates machines, so that availability is update.
        :param customer_id: number id of customer
        :param machine_id: number id of machine
        :param days: number of days machine is rented
        :param price: price for rent per day
        :param note: string note
        :return: bool
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            rental_id_var = cursor.var(int)
            query_rental = "insert into Rentals(customer_id, note) values(:1, :2) returning id into :3"
            cursor.execute(query_rental, [customer_id, note, rental_id_var])
            new_rental_id = rental_id_var.getvalue()[0]

            query_item = """insert into Rental_Items(rental_id, machine_id, price_per_day, days_count) 
            values(:1, :2, :3, :4)"""
            cursor.execute(query_item, [new_rental_id, machine_id, price, days])

            query_update_machine = "update Machines set is_available = 0 where id = :1"
            cursor.execute(query_update_machine, [machine_id])
            connection.commit()
            print(f"Rental created successfully with ID: {new_rental_id}")
            return True
        except Exception as e:
            connection.rollback()
            print(f"Something went wrong with creating Rental. - {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def get_all_rentals(self):
        """
        Selects all rentals for purpose of display.
        :return: list of rentals
        """
        connection = get_connection()
        cursor = connection.cursor()
        try:
            query = """select r.id, c.company_name, m.model, ri.days_count, ri.price_per_day
            from Rentals r join Customers c on r.customer_id = c.id
            join Rental_Items ri on r.id = ri.rental_id
            join Machines m on ri.machine_id = m.id order by r.id desc"""
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error loading rentals. - {e}")
            return []
        finally:
            cursor.close()
            connection.close()
