# In this project we are exploring in depth the modules MySQLdb and SQLAlchemy.
0. Write a script that lists all states from the database.
1. Write a script that lists all states with a name starting with N (upper N) from the database.
2. Write a script that takes in an argument and displays all values in the states table of the database where name matches the argument.
3. Same as #2, but safe from SQL injections.
4. Mysqldb query for all cities in all states.
5. Mysqldb query for all cities in a given state.
6. Create a State class that will inherit from Base which is an instance of declarative_base().
7. Query with sqlalchemy to list all state objects from the database.
8. Query with sqlalchemy to list only the first state object in the database.
9. Query with sqlalchemy to list all state objects that contain the letter 'a'.
10. Query with sqlalchemy to list a state given the state name.
11. Write a script with sqlalchemy that adds a new state object to the database.
12. Write a script with sqlalchemy that updates an existing state object in the database.
13. Write a sqlalchemy script that deletes rows in the table for states containing the letter 'a'.
14. Create a new City class and write a sqlalchemy query that will print all cities matched with their states.