# Email Project
The email project allows the user to view their mailbox and send emails in a email-based web application.
<br></br>

## Mail App
**Login** 
- Users must login to their account using their credentials to access the email application
&nbsp;

![Login](/mail/static/mail/images/login.png?raw=true "Login")
<br></br>

**Register for a New Account**
- The user can also register for a new account (must provide an email and password)
&nbsp;

![Register](/mail/static/mail/images/register.png?raw=true "Register")
<br></br>

**Inbox**
- The user can view all emails in their inbox on the homepage (displayed in reverse chronological order by date and time)
- Each email will display the sender, subject, as well as the date and time
- Emails that are unread are white, and emails that are read are grey
&nbsp;

![Inbox](/mail/static/mail/images/inbox.png?raw=true "Inbox")
<br></br>

**Navigation Bar**
- Users can access the navigation bar at the top to go to a specific mailbox or to compose a new email
- The navigation bar has the following options:
    - Inbox
      - User can view their own inbox
    - Compose
      - User can compose a new email to send
    - Sent
      - User can view all emails already sent
    - Archive
      - User can view all archived emails
    - Logout
      - User can logout of their account
<br></br>

**Email Details**
- Clicking on a selected email allows the user to view the email details including the following:
    - Sender
    - Recipients
    - Subject
    - Body
    - Timestamp
- The user can toggle the email from read to unread and vice versa 
- The user can also archive and unarchive the email
- There is also an option to reply to the email
    - Replying to the email will bring the user to the compose email form with prefilled information about the recipient, Re: the previous subject, and information about the previous email (sender, contents, timeframe) will be prepopulated in the body
&nbsp;

![Reply](/mail/static/mail/images/reply.png?raw=true "Reply")
<br></br>

**Compose**
- Users can compose and send a new email by filling out the recipients (comma and space separated), subject, and body
&nbsp;

![Compose](/mail/static/mail/images/compose.png?raw=true "Compose")
<br></br>

**Sent**
- The user can view all of their sent emails
&nbsp;

![Sent](/mail/static/mail/images/sent.png?raw=true "Sent")
<br></br>

**Archive**
- The user can view all of their archived emails
- Emails can be unarchived by viewing the email details and clicking the unarchive button
&nbsp;

![Archive](/mail/static/mail/images/archive.png?raw=true "Archive")
<br></br>


## Languages & Frameworks
- The email project was created using Django, a Python-based web framework
- JavaScript was utilized to create a single-page web application with dynamic user interfaces

## How to Run Locally
- Install the latest version of python
    - Check the version using ```python --version```
- Clone the repository from github by typing in the command line
    - ```git clone <repo-url>```
- Install any dependencies by typing in the command line
    -```pip install -r requirements.txt```
- Apply database migrations by typing in the command line
    - ```python manage.py migrate```
- The web application can be run on your local server by typing in the command line
    - ```python3 manage.py runserver```

