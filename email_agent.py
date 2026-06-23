import csv
from datetime import datetime

# Keywords
membership_keywords = [
    "membership",
    "join",
    "pricing",
    "fees",
    "plans"
]

trainer_keywords = [
    "trainer",
    "personal training",
    "coach",
    "coaching"
]


# Classify Email
def classify_email(email_text):

    email_text = email_text.lower()

    for keyword in membership_keywords:
        if keyword in email_text:
            return "membership"

    for keyword in trainer_keywords:
        if keyword in email_text:
            return "trainer"

    return "general"


# Generate Reply
def generate_reply(category):

    if category == "membership":

        return """
Hello,

Thank you for contacting Minimum Strength Gym.

For membership details, please contact us at:
+91 9876543210

Regards,
Minimum Strength Gym
"""

    elif category == "trainer":

        return """
Hello,

Thank you for your interest in Personal Training.

Please contact us at:
+91 9876543210

Regards,
Minimum Strength Gym
"""

    else:

        return """
Hello,

Thank you for contacting Minimum Strength Gym.

Please call us at:
+91 9876543210

Regards,
Minimum Strength Gym
"""


# Save Lead
def save_lead(name, email, category, message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("leads.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            name,
            email,
            category,
            message
        ])


# Main Program
print("===== GYM EMAIL AGENT =====")

name = input("Enter customer name: ")

email = input("Enter customer email: ")

email_text = input("What do you want to know about the gym? ")

category = classify_email(email_text)

reply = generate_reply(category)

save_lead(
    name,
    email,
    category,
    email_text
)

print("\n----- EMAIL ANALYSIS -----")
print("Category:", category)

print("\n----- AUTO REPLY -----")
print(reply)

print("\nLead saved successfully!")
