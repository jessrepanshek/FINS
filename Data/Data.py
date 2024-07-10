import pymssql

class DatabaseManager:
    def __init__(self, server, database, user, password):
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pymssql.connect(server=self.server,
                                              user=self.user,
                                              password=self.password,
                                              database=self.database)
            print("Connected to the database successfully")
        except pymssql.Error as e:
            print("Error connecting to the database:", e)

    def create_user_table(self):
        # SQL command to create a user table
        create_table_query = """
        CREATE TABLE Users (
            ID INT IDENTITY(1,1) PRIMARY KEY,
            userName VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            firstName VARCHAR(255) NOT NULL,
            lastName VARCHAR(255) NOT NULL,
            hash VARCHAR(255) NOT NULL,
            role VARCHAR(255) NOT NULL
        )
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
            print("Users table created successfully")
        except pymssql.Error as e:
            print("Error creating Users table:", e)

    def add_user(self, user):
        # SQL command to insert a new user
        insert_user_query = """
        INSERT INTO Users (
            userName, 
            email, 
            firstName, 
            lastName, 
            hash, 
            role)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (user._userName,
                  user._email,
                  user._firstName,
                  user._lastName,
                  user._passwordHash,
                  user._role)

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_user_query, values)
            self.connection.commit()
            print("User added successfully")
        except pymssql.Error as e:
            print("Error adding user:", e)

    def get_all_users(self):
        # SQL command to retrieve all user data
        select_users_query = "SELECT * FROM Users"

        try:
            cursor = self.connection.cursor()
            cursor.execute(select_users_query)
            user_data = cursor.fetchall()
            return user_data
        except pymssql.Error as e:
            print("Error retrieving user data:", e)
            return []

    def get_all_emails(self):
        # SQL command to retrieve all email addresses
        select_emails_query = "SELECT email FROM Users"

        # Extract list of email addresses from the query
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_emails_query)
            email_data = cursor.fetchall()
            return [email[0] for email in email_data]
        except pymssql.Error as e:
            print("Error retrieving email addresses:", e)
            return []

    def get_password_hash_for_email(self, email):
        # SQL command to retrieve the password hash for the given email
        select_password_hash_query = "SELECT hash FROM Users WHERE email = %s"

        # Extract the password hash from the result
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_password_hash_query, (email,))
            password_hash = cursor.fetchone()
            if password_hash:
                return password_hash[0]
            else:
                return None  # Email not found in the database
        except pymssql.Error as e:
            print("Error retrieving password hash:", e)
            return None

    def insert_placeholder_values(self):
        # SQL command to insert placeholder values
        create_table_query = """
        INSERT INTO Users (
            userName, email, 
            firstName, lastName, hash, role)
        VALUES
            ('User1', 'user1@example.com', 
            'user', 'one', 'password1', 'Subscriber'),
            ('User2', 'user2@example.com', 
            'User', 'Two', 'password2', 'Subscriber'),
            ('User3', 'user3@example.com', 
            'user', 'three', 'password3', 'Subscriber'),
            ('User4', 'user4@example.com', 
            'User', 'Four', 'password4', 'Subscriber'),
            ('User5', 'user5@example.com', 
            'user', 'five', 'password5', 'Subscriber')
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
            print("User data created successfully")
        except pymssql.Error as e:
            print("Error creating user data:", e)

    def clear_table(self):
        # Clear entries in the test table
        clear_table_query = """
                DELETE FROM Users;
                """
        try:
            cursor = self.connection.cursor()
            cursor.execute(clear_table_query)
            self.connection.commit()
            print("Users table cleared successfully")
        except pymssql.Error as e:
            print("Error clearing Users table:", e)

    def drop_table(self):
        # Clear entries in the test table
        clear_table_query = """
                DROP TABLE Users;
                """
        try:
            cursor = self.connection.cursor()
            cursor.execute(clear_table_query)
            self.connection.commit()
            print("Users table dropped successfully")
        except pymssql.Error as e:
            print("Error dropping Users table:", e)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

if __name__ == '__main__':
    server = 'cisdbss.pcc.edu'
    database = 'Hardest_Part_Details'
    user = 'Hardest_Part_Details'
    password = 'MyCis234AStory*2'

    # Functions to do table maintenance
    #manager = DatabaseManager(server, database, user, password)
    #manager.connect()
    #manager.create_user_table()
    #manager.insert_placeholder_values()
    #manager.clear_table()
    #manager.drop_table()
    #manager.close_connection()
