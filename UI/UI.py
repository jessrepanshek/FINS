from flask import render_template, request, redirect, url_for, g
from werkzeug.security import generate_password_hash, check_password_hash

from Logic.User import User
from Data.Data import DatabaseManager

def create_UI(app):
    # Store Database credentials
    def create_manager():
        return DatabaseManager('cisdbss.pcc.edu',
                               'Hardest_Part_Details',
                               'Hardest_Part_Details',
                               'MyCis234AStory*2')

    # Create global variable with attribute for manager
    # Then, create instance of the DatabaseManager for the UI to use
    @app.before_request
    def before_request():
        # Check if the manager object is not in the context globals (g)
        if not hasattr(g, 'manager'):
            # Create and store the manager object in the context globals
            g.manager = create_manager()

    # Display login form when accessing root
    @app.route('/')
    def index():
        return render_template('login.html')

    # Action when user clicks Create Account button
    @app.route('/createAccount', methods=['GET', 'POST'])
    def createAccount():
        if request.method == 'POST':
            # Collect data from the HTML form
            firstname = request.form.get('firstName')
            lastname = request.form.get('lastName')
            username = request.form.get('userName')
            email = request.form.get('email')
            confirm_email = request.form.get('confirmEmail')
            password = request.form.get('passwordHash')
            confirm_password = request.form.get('confirmPassword')

            # Check if email and confirm email fields match
            if email != confirm_email:
                error_message = 'Email and confirm email do not match.'
                return render_template('login.html',
                                       error_message=error_message)

            # Connect to the database
            g.manager.connect()

            # Query the database to get list of emails
            email_addresses = g.manager.get_all_emails()

            # Close the database connection
            g.manager.close_connection()

            # Show error if email is already registered
            if email in email_addresses:
                error_message = 'Email already registered.'
                return render_template('login.html',
                                       error_message=error_message)

            # Check if the password and confirm password fields match
            if password != confirm_password:
                error_message = 'Password and confirm password do not match.'
                return render_template('login.html',
                                       error_message=error_message)

            # Hash the password using Werkzeug's generate_password_hash
            hashed_password = generate_password_hash(password,
                                                     method='pbkdf2:sha256')

            # Create a new user object
            new_user = User(firstname,
                            lastname,
                            username,
                            email,
                            hashed_password)

            # Connect to the database
            g.manager.connect()

            # Insert the new user into the database
            g.manager.add_user(new_user)

            # Close the database connection
            g.manager.close_connection()

            # Redirect to dashboard
            return redirect(url_for('dashboard'))

        # If it's a GET request, display the login form
        return render_template('login.html', error_message=None)

    @app.route('/login', methods=['POST'])
    def login():
        # Collect data from the HTML form
        email = request.form.get('loginEmail')
        password = request.form.get('loginPassword')

        # Connect to database
        g.manager.connect()

        # Query database for email list
        email_addresses = g.manager.get_all_emails()

        # Close database connection
        g.manager.close_connection()

        # Check if the email already exists
        if email not in email_addresses:
            error_message = 'Incorrect credentials.'
            return render_template('login.html',
                                   error_message=error_message)

        # Connect to database
        g.manager.connect()

        # Query the database to retrieve the stored password hash
        stored_password_hash = g.manager.get_password_hash_for_email(email)

        # Close database connection
        g.manager.close_connection()

        # Compare the provided password with the stored password hash
        if check_password_hash(stored_password_hash, password):
            # Passwords match, redirect to the dashboard page
            return redirect(url_for('dashboard'))
        else:
            # Passwords do not match, throw an error or show a message
            error_message = 'Incorrect credentials. Please try again.'
            return render_template('login.html',
                                   error_message=error_message)

    @app.route('/dashboard')
    def dashboard():
        # Connect to the database
        g.manager.connect()

        # Retrieve all user data from the database
        user_data = g.manager.get_all_users()

        # Close database connection
        g.manager.close_connection()

        return render_template('dashboard.html', user_data=user_data)
