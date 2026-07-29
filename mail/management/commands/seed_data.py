from datetime import datetime, timezone as dt_timezone

from django.core.management.base import BaseCommand

from mail.models import Email, User

# Usernames for all demo accounts
DEMO_USERS = ["steph@mail.com", "hi@mail.com", "seykafu@mail.com"]

# Shared login password for all the demo accounts above
DEMO_PASSWORD = "password123"

# Each entry mirrors what the compose view does, creating one Email row per user
# involved and sharing the sender, recipients, subject, and body across rows,
# with a per-user read and archived state
DEMO_EMAILS = [
    {
        "sender": "hi@mail.com",
        "recipients": ["steph@mail.com", "seykafu@mail.com"],
        "subject": "Book meeting as soon as possible",
        "body": "Hi, please let me know what times you are available so we can book a meeting as soon as possible!",
        "sent_at": datetime(2024, 5, 14, 3, 49, 17, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": True, "archived": True}},
    },
    {
        "sender": "steph@mail.com",
        "recipients": ["hi@mail.com", "seykafu@mail.com"],
        "subject": "Question about tomorrow's presentation",
        "body": "Hey guys, I was just wondering what time tomorrow's presentation was?",
        "sent_at": datetime(2024, 5, 14, 3, 52, 17, tzinfo=dt_timezone.utc),
        "states": {},
    },
    {
        "sender": "steph@mail.com",
        "recipients": ["hi@mail.com", "seykafu@mail.com"],
        "subject": "Follow up about yesterday's event",
        "body": "Hey guys!\n\nHope this email finds you well. I just wanted to follow up about yesterday's event and see if there is anything I missed.",
        "sent_at": datetime(2024, 5, 14, 3, 55, 35, tzinfo=dt_timezone.utc),
        "states": {},
    },
    {
        "sender": "seykafu@mail.com",
        "recipients": ["hi@mail.com", "steph@mail.com"],
        "subject": "Product management newsletter",
        "body": "Hi guys,\n\nPlease subscribe to my new newsletter and come listen to my upcoming podcasts!",
        "sent_at": datetime(2024, 5, 14, 3, 58, 1, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": False}},
    },
    {
        "sender": "hi@mail.com",
        "recipients": ["steph@mail.com", "seykafu@mail.com"],
        "subject": "Open house scheduled for tomorrow",
        "body": "Hey guys,\n\nI just booked an open house scheduled for tomorrow at 1pm! Please let me know if you can't make it!",
        "sent_at": datetime(2024, 5, 14, 3, 59, 10, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": True}},
    },
    {
        "sender": "steph@mail.com",
        "recipients": ["hi@mail.com", "seykafu@mail.com"],
        "subject": "Exclusive presale and access and discount",
        "body": "Hi!\n\nPlease see the link attached for the exclusive presale and access as well as discount to my new subscription service!\nhttps://www.subscriptionservicesteph.com",
        "sent_at": datetime(2024, 5, 14, 4, 0, 39, tzinfo=dt_timezone.utc),
        "states": {},
    },
    {
        "sender": "seykafu@mail.com",
        "recipients": ["hi@mail.com", "steph@mail.com"],
        "subject": "Understanding how early career professionals can chase passions wisely",
        "body": "Hi guys,\n\nI released a new article on my steps on how to chase a passion wisely!",
        "sent_at": datetime(2024, 5, 14, 4, 2, 13, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": True}},
    },
    {
        "sender": "seykafu@mail.com",
        "recipients": ["hi@mail.com", "steph@mail.com"],
        "subject": "Invitation: work dinner on Sunday",
        "body": "Hi guys,\n\nWanted to check in to see if you guys would be down to have a work dinner on Sunday at 6pm?",
        "sent_at": datetime(2024, 5, 14, 4, 3, 17, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": True, "archived": True}},
    },
    {
        "sender": "hi@mail.com",
        "recipients": ["steph@mail.com", "seykafu@mail.com"],
        "subject": "Updated plans for upcoming work trip",
        "body": "Hi guys,\n\nPlease check our website for the updated plans for the upcoming work trip in June!",
        "sent_at": datetime(2024, 5, 14, 4, 4, 54, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": True}},
    },
    {
        "sender": "steph@mail.com",
        "recipients": ["hi@mail.com", "seykafu@mail.com"],
        "subject": "Book meeting asap",
        "body": "Hey guys,\n\nWe need to book a meeting asap to go over today's to dos. Thanks!",
        "sent_at": datetime(2024, 5, 14, 4, 6, 7, tzinfo=dt_timezone.utc),
        "states": {},
    },
    {
        "sender": "seykafu@mail.com",
        "recipients": ["hi@mail.com", "steph@mail.com"],
        "subject": "Document shared with you: meeting notes",
        "body": "Please see the document I will share regarding today's meeting notes.",
        "sent_at": datetime(2024, 5, 14, 4, 7, 28, tzinfo=dt_timezone.utc),
        "states": {"steph@mail.com": {"read": False}},
    },
]


class Command(BaseCommand):
    help = "Seeds the database with demo users and emails for local development/testing."

    # Adds the --flush flag for clearing existing demo emails before reseeding
    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing demo emails (from the demo users) before reseeding.",
        )

    # Creates the demo users, then seeds their emails unless they already exist
    def handle(self, *args, **options):
        users = {}
        for email in DEMO_USERS:
            user, created = User.objects.get_or_create(
                username=email, defaults={"email": email}
            )
            if created:
                user.set_password(DEMO_PASSWORD)
                user.save()
                self.stdout.write(f"Created user {email}")
            users[email] = user

        if options["flush"]:
            deleted, _ = Email.objects.filter(sender__in=users.values()).delete()
            self.stdout.write(f"Deleted {deleted} existing demo email row(s)")

        if Email.objects.filter(sender__in=users.values()).exists():
            self.stdout.write(
                self.style.WARNING(
                    "Demo emails already exist, skipping. Re-run with --flush to reseed."
                )
            )
        else:
            for entry in DEMO_EMAILS:
                sender = users[entry["sender"]]
                recipients = [users[email] for email in entry["recipients"]]
                timestamp = entry["sent_at"]

                involved = {sender}.union(recipients)
                for user in involved:
                    state = entry["states"].get(user.username, {})
                    email = Email(
                        user=user,
                        sender=sender,
                        subject=entry["subject"],
                        body=entry["body"],
                        read=state.get("read", user == sender),
                        archived=state.get("archived", False),
                    )
                    email.save()
                    for recipient in recipients:
                        email.recipients.add(recipient)
                    email.timestamp = timestamp
                    email.save()

            self.stdout.write(f"Created {len(DEMO_EMAILS)} demo email thread(s)")

        self.stdout.write(self.style.SUCCESS("Done."))
        self.stdout.write(f"Demo accounts (password: {DEMO_PASSWORD}):")
        for email in DEMO_USERS:
            self.stdout.write(f"  {email}")
