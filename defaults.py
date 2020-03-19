"""
Default configuration options for Kapsch CMP
"""
PORTAL_NAME = "Kapsch CMP"
EMAIL_LOGO = "static/ui/kapsch_logo-2.png"
THEME = "kapsch"
EMAIL_FROM = "Kapsch CMP <cmp@kapsch.net>"
EMAIL_ALERTS = "cmp@kapsch.net"
EMAIL_INFO = "info@kapsch.net"
EMAIL_SALES = "sales@kapsch.net"
EMAIL_SUPPORT = "support@kapsch.net"
EMAIL_NOTIFICATIONS = "cmp@kapsch.net"

ENABLE_MONITORING = True
DOCS_URI = SUPPORT_URI = ''

PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
]

EC2_SECURITYGROUP = {
    'name': 'kapsch-cmp',
    'description': 'Security group created by Kapsch CMP'
}


CONFIRMATION_EMAIL_SUBJECT = "[Kapsch CMP] Confirm your registration"

CONFIRMATION_EMAIL_BODY = \
"""Hi %s,

we received a registration request to Kapsch CMP from this email address.

To activate your account, please click on the following link:

%s/confirm?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message.

Best regards,
The Kapsch CMP team

--
%s
"""


RESET_PASSWORD_EMAIL_SUBJECT = "[Kapsch CMP] Password reset request"

RESET_PASSWORD_EMAIL_BODY = \
"""Hi %s,

We have received a request to change your password.
Please click on the following link:

%s/reset-password?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. Your password has not been changed.


Best regards,
The Kapsch CMP team

--
%s
"""


WHITELIST_IP_EMAIL_SUBJECT = "[Kapsch CMP] Account IP whitelist request"

WHITELIST_IP_EMAIL_BODY = \
"""Hi %s,

We have received a request to whitelist the IP you just tried to login with.
Please click on the following link to finish this action:

%s/confirm-whitelist?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. The above IP will not be whitelisted.


Best regards,
The Kapsch CMP team

--
%s
Govern the clouds
"""


FAILED_LOGIN_ATTEMPTS_EMAIL_SUBJECT = "[Kapsch CMP] Failed login attempts warning"


ORG_NOTIFICATION_EMAIL_SUBJECT = "[Kapsch CMP] Subscribed to team"

USER_NOTIFY_ORG_TEAM_ADDITION = \
"""Hi

You have been added to the team "%s" of organization %s.

Best regards,
The Kapsch CMP team

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
you will be able to login to your Kapsch CMP user account
as a member of the team%s.

Best regards,
The Kapsch CMP team

--
%s
"""

ORG_INVITATION_EMAIL_SUBJECT = "[Kapsch CMP] Confirm your invitation"

REGISTRATION_AND_ORG_INVITATION_EMAIL_BODY = \
"""Hi

You have been invited by %s to join the %s organization
as a member of the %s.

Before joining the team you must also activate your account in  Kapsch CMP and set
a password. To activate your account and join the team, please click on the
following link:

%s/confirm?key=%s&invitoken=%s

Once you are done with the registration process,
you will be able to login to your Kapsch CMP user account
as a member of the team%s.

Best regards,
The Kapsch CMP team

--
%s
"""

NOTIFY_REMOVED_FROM_TEAM = \
"""Hi

You have been removed from team %s of organization %s by the
administrator %s.

Best regards,
The Kapsch CMP team

--
%s
"""

NOTIFY_REMOVED_FROM_ORG = \
"""Hi

You are no longer a member of the organization %s.

Best regards,
The Kapsch CMP team

--
%s
"""

NOTIFY_INVITATION_REVOKED_SUBJECT = "Invitation for organization revoked"

NOTIFY_INVITATION_REVOKED = \
"""Hi

Your invitation to the organization %s has been revoked.

Best regards,
The Kapsch CMP team

--
%s
"""

