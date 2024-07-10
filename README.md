# Food Insecurity Notification System (FINS)

# Project Overview
FINS (Food Insecurity Notification System) is designed to help food-insecure students stay informed about available food resources, specials, and events at their school’s food pantry. This project enables food pantry managers to efficiently send notifications via email (and in future iterations, SMS) to subscribed students, ensuring they receive timely and relevant information.

# Features

# User Stories
Sprint 1
1. Notification System - Subscriber Account Creation and Login
- Users can create a new account or log into an existing account.
- User account information is protected.
- Passwords are stored as hashed values.
- Users receive feedback on account creation or login status.

2. Send Notification
- Food Pantry Managers can send email notifications to all subscribers.
- Each message contains a subject and body text.
- Notification details are logged for future review.

3. Review Notification Log
- Food Pantry Managers can review sent notifications.
- Log entries include the subject, message, sender, date and time, and the number of recipients.

# Sprint 2
1. Send Notification – SMS Messaging
- Notifications can be sent via SMS based on user preference.

2. Subscriber Settings – Profile Editing
- Users can update their personal information and notification preferences.

3. User Account Creation and Login – Account Deletion
- Users can delete their accounts.

# Directory Structure
FINS/
├── app.py
├── requirements.txt
├── README.md
├── UI/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── ...
│   ├── static/
│   │   ├── styles/
│   │   │   ├── login.css
│   │   │   ├── profile.css
│   │   │   └── ...
│   │   ├── images/
│   │   │   └── FINSfridge.png
│   │   └── ...
│   └── ...
├── Logic/
│   ├── User.py
│   ├── Notification.py
│   ├── ...
│   └── tests/
│       ├── UserTest.py
│       └── ...
└── ...

# Acknowledgements
Developed by Jess Repanshek and team.
Thanks to all contributors and supporters of this project.
