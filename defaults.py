"""
Default configuration options for Avvan
"""
PORTAL_NAME = "Avvan"
EMAIL_LOGO = "static/CTI-logo2.png"
THEME = "computrade"
EMAIL_FROM = "Avvan <cmp@avvan.id>"
EMAIL_ALERTS = "alert@avvan.id"
EMAIL_INFO = "info@avvan.id"
EMAIL_SALES = "sales@avvan.id"
EMAIL_SUPPORT = "support@avvan.id"
EMAIL_NOTIFICATIONS = "notifications@avvan.id"
#CURRENCY = {
#    "sign": "Rp",
#    "rate": 13720.5
#}
ENABLE_MONITORING = True
DOCS_URI = SUPPORT_URI = ''

PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]

EC2_SECURITYGROUP = {
    'name': 'avvan',
    'description': 'Security group created by Avvan'
}


CONFIRMATION_EMAIL_SUBJECT = "[Avvan] Confirm your registration"

CONFIRMATION_EMAIL_BODY = \
"""Hi %s,

we received a registration request to Avvan from this email address.

To activate your account, please click on the following link:

%s/confirm?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message.

Best regards,
The Avvan team

--
%s
"""


RESET_PASSWORD_EMAIL_SUBJECT = "[Avvan] Password reset request"

RESET_PASSWORD_EMAIL_BODY = \
"""Hi %s,

We have received a request to change your password.
Please click on the following link:

%s/reset-password?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. Your password has not been changed.


Best regards,
The Avvan team

--
%s
"""


WHITELIST_IP_EMAIL_SUBJECT = "[Avvan] Account IP whitelist request"

WHITELIST_IP_EMAIL_BODY = \
"""Hi %s,

We have received a request to whitelist the IP you just tried to login with.
Please click on the following link to finish this action:

%s/confirm-whitelist?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. The above IP will not be whitelisted.


Best regards,
The Avvan team

--
%s
Govern the clouds
"""


FAILED_LOGIN_ATTEMPTS_EMAIL_SUBJECT = "[Avvan] Failed login attempts warning"


ORG_NOTIFICATION_EMAIL_SUBJECT = "[Avvan] Subscribed to team"

USER_NOTIFY_ORG_TEAM_ADDITION = \
"""Hi

You have been added to the team "%s" of organization %s.

Best regards,
The Avvan team

--
%s
"""

USER_CONFIRM_ORG_INVITATION_EMAIL_BODY = \
"""Hi

You have been invited by %s to join the %s organization
as a member of the %s.

To confirm your invitation, please click on the following link:

%s/confirm-invitation?invitoken=%s

Once you are done with the confirmation process,
you will be able to login to your Avvan user account
as a member of the team%s.

Best regards,
The Avvan team

--
%s
"""

ORG_INVITATION_EMAIL_SUBJECT = "[Avvan] Confirm your invitation"

REGISTRATION_AND_ORG_INVITATION_EMAIL_BODY = \
"""Hi

You have been invited by %s to join the %s organization
as a member of the %s.

Before joining the team you must also activate your account in  Avvan and set
a password. To activate your account and join the team, please click on the
following link:

%s/confirm?key=%s&invitoken=%s

Once you are done with the registration process,
you will be able to login to your Avvan user account
as a member of the team%s.

Best regards,
The Avvan team

--
%s
"""

NOTIFY_REMOVED_FROM_TEAM = \
"""Hi

You have been removed from team %s of organization %s by the
administrator %s.

Best regards,
The Avvan team

--
%s
"""

NOTIFY_REMOVED_FROM_ORG = \
"""Hi

You are no longer a member of the organization %s.

Best regards,
The Avvan team

--
%s
"""

NOTIFY_INVITATION_REVOKED_SUBJECT = "Invitation for organization revoked"

NOTIFY_INVITATION_REVOKED = \
"""Hi

Your invitation to the organization %s has been revoked.

Best regards,
The Avvan team

--
%s
"""

