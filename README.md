# Email

A full stack web application that replicates the core functionality of a modern inbox. Users can create an account, sign in, read and send messages, reply to existing threads, and organize their mail across sent and archived folders. The application is built as a single page interface, meaning every action updates instantly in the browser without requiring a full page reload.

<br>

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Future Improvements](#future-improvements)

<br>

## Overview

This project demonstrates the design and implementation of a functional email client from the ground up, covering both a responsive client side interface and the server side logic behind it. The frontend is built with JavaScript, HTML5, CSS3, and Bootstrap, and renders each view (Inbox, Sent, Archive, Compose, and Email Detail) dynamically. Rather than reloading the page for each interaction, the interface communicates with the backend asynchronously in the background, which keeps the application quick and responsive to use. The backend is built with Django and Python, handling account authentication, a JSON API that sends, retrieves, and updates messages, and persistent storage of all user and email data in a SQLite database.

<br>

## Features

### Authentication
Access to the application is secured through a login system. Existing users can sign in with their registered credentials, while new users can create an account by providing an email address and password. User sessions and credentials are managed through Django's built in authentication framework.

<p align="center"><b>Login</b></p>
<p align="center"><img src="/mail/static/mail/images/login.png?raw=true" alt="Login" width="700"></p>

<p align="center"><b>Register</b></p>
<p align="center"><img src="/mail/static/mail/images/register.png?raw=true" alt="Register" width="700"></p>

<br>

### Inbox
The inbox serves as the landing page after a user signs in. Received emails are displayed in reverse chronological order, with each entry showing the sender, subject, and timestamp. Unread messages are displayed with a white background to draw attention, while messages that have already been opened appear in grey, giving users a clear visual distinction at a glance.

<p align="center"><img src="/mail/static/mail/images/inbox.png?raw=true" alt="Inbox" width="700"></p>

<br>

### Navigation
A persistent navigation bar at the top of the application provides quick access to the Inbox, Sent, and Archive mailboxes, as well as options to compose a new email or log out. This allows users to move between different sections of the application efficiently without losing their place.

<br>

### Email Detail
Selecting an email opens a detailed view of the full message, including the sender, recipients, subject, body, and timestamp. From this view, users can mark the message as read or unread, move it into or out of the archive, or reply directly. Selecting reply opens the compose form with the recipient, subject line, and original message content automatically populated, allowing the user to continue the conversation without having to retype existing information.

<p align="center"><img src="/mail/static/mail/images/reply.png?raw=true" alt="Reply" width="700"></p>

<br>

### Compose
Users can create and send a new email through the compose form by specifying one or more recipients (comma and space separated), a subject line, and a message body. Once sent, the message is saved on the backend and delivered to the inbox of each recipient.

<p align="center"><img src="/mail/static/mail/images/compose.png?raw=true" alt="Compose" width="700"></p>

<br>

### Sent and Archive
The Sent mailbox provides a record of all messages a user has sent, while the Archive stores emails the user has chosen to set aside from the main inbox. Archived emails remain fully accessible and can be restored to the inbox at any time from the email detail view, giving users flexible control over how their mail is organized.

<p align="center"><b>Sent</b></p>
<p align="center"><img src="/mail/static/mail/images/sent.png?raw=true" alt="Sent" width="700"></p>

<p align="center"><b>Archive</b></p>
<p align="center"><img src="/mail/static/mail/images/archive.png?raw=true" alt="Archive" width="700"></p>

<br>

## Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | JavaScript, HTML5, CSS3, Bootstrap |
| Backend | Django, Python |
| Database | SQLite |

<br>

## How It Works

The application follows a clear separation between the client and the server. On the client side, JavaScript intercepts user interactions such as navigation and form submissions, then issues asynchronous requests to a JSON API rather than triggering a full page reload. The data returned from each request is used to construct and update the relevant view directly in the browser. On the server side, Django serves the initial page and exposes that JSON API, managing each mailbox and individual email. User actions, including archiving, marking messages as read or unread, replying, and sending, are sent back to the Django backend, which updates the database and returns the current state of the affected data. This architecture keeps the interface responsive while ensuring all changes are reliably persisted on the server.

<br>

## Getting Started

Follow the steps below to set up and run the application on your own machine.

**Prerequisites**

Make sure Python 3 is installed before you begin. You can check by running the command below, which should print a version number.
```bash
python --version
```

**1. Clone the repository**

This downloads a copy of the project to your computer and moves you into the project folder.
```bash
git clone https://github.com/steph-xue/email.git
cd email
```

**2. Create and activate a virtual environment (recommended)**

This keeps the project's dependencies separate from other Python projects on your machine.
```bash
python3 -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
```

**3. Install the dependencies**

This installs Django and everything else the project needs to run.
```bash
pip install -r requirements.txt
```

**4. Set up the database**

This creates the local database and the tables the application relies on.
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

**5. Start the development server**

This runs the application locally.
```bash
python3 manage.py runserver
```

Once the server is running, open `http://127.0.0.1:8000/` in your browser to start using the application.

<br>

## Future Improvements
Several enhancements are planned to extend the functionality and reach of the application:
- Search and filtering across mailboxes
- Pagination for large inboxes
- Support for file and image attachments
- A live hosted demo to allow users to try the application without a local setup
