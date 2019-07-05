"""
Default configuration options for CTI Cloud Manager (CCM)
"""
PORTAL_NAME = "CTI Cloud Manager"
EMAIL_LOGO = "static/CTI-logo2.png"
THEME = "computrade"
EMAIL_FROM = "CTI Cloud Manager <cti@computradetech.com>"
EMAIL_ALERTS = "alert@computradetech.com"
EMAIL_INFO = "info@computradetech.com"
EMAIL_SALES = "sales@computradetech.com"
EMAIL_SUPPORT = "support@computradetech.com"
EMAIL_NOTIFICATIONS = "notifications@computradetech.com"
CURRENCY = {
    "sign": "Rp",
    "rate": 14430.0
}
ENABLE_MONITORING = True
DOCS_URI = SUPPORT_URI = ''

PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'cloudify_insights',
]

EC2_SECURITYGROUP = {
    'name': 'cti-cloud-manager',
    'description': 'Security group created by CTI Cloud Manager (CCM)'
}


CONFIRMATION_EMAIL_SUBJECT = "[CTI Cloud Manager (CCM)] Confirm your registration"

CONFIRMATION_EMAIL_BODY = \
"""Hi %s,

we received a registration request to CTI Cloud Manager from this email address.

To activate your account, please click on the following link:

%s/confirm?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message.

Best regards,
The CTI Cloud Manager team

--
%s
"""


RESET_PASSWORD_EMAIL_SUBJECT = "[CTI Cloud Manager (CCM)] Password reset request"

RESET_PASSWORD_EMAIL_BODY = \
"""Hi %s,

We have received a request to change your password.
Please click on the following link:

%s/reset-password?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. Your password has not been changed.


Best regards,
The CTI Cloud Manager team

--
%s
"""


WHITELIST_IP_EMAIL_SUBJECT = "[CTI Cloud Manager (CCM)] Account IP whitelist request"

WHITELIST_IP_EMAIL_BODY = \
"""Hi %s,

We have received a request to whitelist the IP you just tried to login with.
Please click on the following link to finish this action:

%s/confirm-whitelist?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. The above IP will not be whitelisted.


Best regards,
The CTI Cloud Manager team

--
%s
Govern the clouds
"""


FAILED_LOGIN_ATTEMPTS_EMAIL_SUBJECT = "[CTI Cloud Manager (CCM)] Failed login attempts warning"


ORG_NOTIFICATION_EMAIL_SUBJECT = "[CTI Cloud Manager (CCM)] Subscribed to team"

USER_NOTIFY_ORG_TEAM_ADDITION = \
"""Hi

You have been added to the team "%s" of organization %s.

Best regards,
The CTI Cloud Manager team

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
you will be able to login to your CTI Cloud Manager user account
as a member of the team%s.

Best regards,
The CTI Cloud Manager team

--
%s
"""

ORG_INVITATION_EMAIL_SUBJECT = "[CTI Cloud Manager (CCM)] Confirm your invitation"

REGISTRATION_AND_ORG_INVITATION_EMAIL_BODY = \
"""Hi

You have been invited by %s to join the %s organization
as a member of the %s.

Before joining the team you must also activate your account in  CTI Cloud Manager and set
a password. To activate your account and join the team, please click on the
following link:

%s/confirm?key=%s&invitoken=%s

Once you are done with the registration process,
you will be able to login to your CTI Cloud Manager user account
as a member of the team%s.

Best regards,
The CTI Cloud Manager team

--
%s
"""

NOTIFY_REMOVED_FROM_TEAM = \
"""Hi

You have been removed from team %s of organization %s by the
administrator %s.

Best regards,
The CTI Cloud Manager team

--
%s
"""

NOTIFY_REMOVED_FROM_ORG = \
"""Hi

You are no longer a member of the organization %s.

Best regards,
The CTI Cloud Manager team

--
%s
"""

NOTIFY_INVITATION_REVOKED_SUBJECT = "Invitation for organization revoked"

NOTIFY_INVITATION_REVOKED = \
"""Hi

Your invitation to the organization %s has been revoked.

Best regards,
The CTI Cloud Manager team

--
%s
"""

