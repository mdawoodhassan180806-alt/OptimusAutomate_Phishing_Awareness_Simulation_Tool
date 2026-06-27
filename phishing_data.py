# phishing_data.py

EMAIL_EXAMPLES = [
    {
        "title": "Fake Bank Alert",
        "email": """
From: security@bank-verification.com
Subject: URGENT: Your Account Will Be Suspended

Dear Customer,

We detected suspicious activity in your account.
Please verify your account immediately by clicking below:

http://secure-bank-login.verify-user.com

Failure to act within 24 hours will result in account suspension.

Regards,
Security Team
        """,
        "tactics": [
            "Creates urgency",
            "Uses suspicious domain",
            "Threatens account suspension",
            "Requests immediate action"
        ]
    },

    {
        "title": "Fake Prize Winner",
        "email": """
From: winner@lottery-global.net
Subject: Congratulations! You Won $10,000

You have been selected as our lucky winner.

To claim your reward send:
- Full Name
- Address
- Bank Information

within 48 hours.

Congratulations!
        """,
        "tactics": [
            "Unexpected reward",
            "Requests sensitive information",
            "Creates excitement and urgency"
        ]
    },

    {
        "title": "Fake IT Support",
        "email": """
From: it-support@company-security.com
Subject: Password Expiring Today

Your password expires today.

Click here immediately:
http://company-password-reset.security-login.net

Failure to reset may lock your account.

IT Department
        """,
        "tactics": [
            "Impersonation",
            "Urgency",
            "Suspicious URL",
            "Fear-based pressure"
        ]
    }
]

QUIZ_QUESTIONS = [
    {
        "question": "An email asks you to verify your bank account immediately or it will be suspended.",
        "answer": "phishing"
    },
    {
        "question": "An email from your manager uses the normal company domain and references a meeting you attended.",
        "answer": "legitimate"
    },
    {
        "question": "You won a prize but never entered a contest.",
        "answer": "phishing"
    },
    {
        "question": "A website URL looks slightly different from the official company website.",
        "answer": "phishing"
    },
    {
        "question": "An email asks for your password.",
        "answer": "phishing"
    }
]

