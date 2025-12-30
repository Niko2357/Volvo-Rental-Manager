# Volvo-Rental-Manager
This software simulates management of renting construction machines using database and GUI. It records individual customers and machines. Meets the requirement of D1, DAO design pattern usage.
## Requirements and libraries
Build in PyCharm.
* System
  * Python interpreter: 3.11 or higher
  * Database: access to Oracle database 19c or 21c XE
* Libraries
  * oracledb - newer version of cx_Oracle
 
    ```python
      pip install oracledb 
    ```
  * tkinter - GUI components
  * shutil - manipulation with files
  * pyinstaller - executable application builder
 
    ```python
      pip install pyinstaller
    ```
## Running the application
### Database setup
Open Oracle SQL Developer and make a new connection. Rewrite connection information to configuration file that is located in /dist directory or the one in the project. Depends on which of three ways to run the application you choose. If it's first then edit the config.json in /dist directory. If it's second or third way edit config.json in the project VolvoRentalManager (same level as main.py).

> [!Important]
> **All needed SQL operations are in code. But path to data being imported needs to stay how you found them (/Data).**

### Application
There are three ways to run this application.

> [!Caution]
> **Change configuration file. Without right username and password nothing will work.**

1. Run the build
   Build is in /dist directory. Find Volvo Manager.exe and start it. Don't forget to change configuration file with your information.
2. Build the app
   Open project VolvoRentalManager and find BuildExe.py. This python file builds and runs the application.
3. Console version
   Just open project VolvoRentalManager and run main.py. GUI will load and some messages might appear in the console.
   
Edit configuration file and try to run application RentalManager
  ```json
    {
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "dsn": "localhost:1521/XE"
    }
  ```

> [!Important]
> **Make sure you have all Privileges needed (creating tables and views, etc.).**

## Application architecture
This application follows DAO (Data access object) design pattern. Presenting layer is build with tkinter library and is build in MainMenu class. Logic layer defines objects such as Machine, Customer, RentalItem and Rental. Data Access layer are classes MachineDAO, CustomerDAO and RentalDAO. They communicate with database.
### Database Model

<img width="639" height="552" alt="Relational_1" src="https://github.com/user-attachments/assets/00b90b1d-bb0f-4293-9457-03e0af85f0a7" />

## Testing Validation
There are three test cases.
* Scenario 1: Creating a rental correctly updates the Machine table.
* Scenario 2: Submitting empty forms triggers a warning dialog.
* Scenario 3: Launches without connection to database results in handled error message instead of crash.

## Checklist
- [x] 1. Relation Database
- [x] 2. 5 tables, M:N relation and 2 views
- [x] 3. Attributes like float, bool, enum, string, varchar, date
- [x] 4. Operations with multiple tables (select, update)
- [x] 5. Transaction upon multiple tables
- [x] 6. Report with information deducated from data
- [x] 7. Import from csv, xml or json into two or more tables
- [x] 8. Configuration file
- [x] 9. Input validation and error handling

## More Info
This software is for educational purposes. The Volvo machine model names are the property of the Volvo Group.

* Author: Nikola Poláchová
* Contact: polachova@spsejecna.cz
