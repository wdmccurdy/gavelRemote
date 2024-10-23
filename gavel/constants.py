ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = 'https://telemetry.anish.io/api/v1/submit'
TELEMETRY_DELTA = 20 * 60 # seconds
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
SETTING_TELEMETRY_LAST_SENT = 'telemetry_sent_time' # integer
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
## Welcome to Gavel!

We're excited to have you join us as a first-round judge for our 2024 "Reimagining User Experience" hackathon!

**Here's how Gavel works:**

*   **Pairwise Comparisons:** You'll be shown two submissions at a time and asked to choose which one is better.
*   **Can't Find a Submission?** If you encounter any issues locating a submission, use the 'Skip' button. But please try your best to find it first!
*   **Votes are Final:** Think carefully before you vote, as you won't be able to change your decision.

**Important Information:**

*   **Judging Deadline:**

    *   Pacific Time: 7:00 AM on October 24th
    *   Eastern Time: 10:00 AM on October 24th
    *   Dublin: 4:00 PM on October 24th

*   **Time Commitment:** Aim to spend 60-90 minutes watching the videos, but don't feel pressured to watch them all. Every vote counts!

*   **Gavel Keeps Going:** Gavel will continue to offer you videos to judge. Feel free to watch as many as your time allows.

**Need Help?**

*   **Video Tutorial:** [Link to Gavel video tutorial](https://drive.google.com/file/d/1b9ka6aVZt87Qhos3FseaIWXsIL2LUfEQ/view)
*   **FAQs:** [Link to FAQs](https://sites.google.com/d/1PJ9sf4zKl0lhc2CAkZxHBrriWvp9zftO/p/1h05KZPhuikIPuBO9_OTqaQuLU1E903UV/edit?authuser=1)
*   **Slack Channel:** #stu-2024-hackathon-judges

Thank you for your time and support! We appreciate you helping us make this hackathon a success!
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Welcome to Gavel!'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Welcome to Gavel, the online expo judging system. This email contains your
magic link to the judging system.

DO NOT SHARE this email with others, as it contains your personal magic link.

To access the system, visit {link}.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
Wait for a little bit and reload the page to try again.

If you've looked at all the projects already, then you're done.
'''.strip()
