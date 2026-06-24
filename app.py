
import streamlit as st
import csv
import smtplib
from email.message import EmailMessage
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
    "coaching",
    "train",
    "training"
]


def classify_email(email_text):

    email_text = email_text.lower()

    for keyword in membership_keywords:
        if keyword in email_text:
            return "membership"

    for keyword in trainer_keywords:
        if keyword in email_text:
            return "trainer"

    return "general"


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


def send_email(receiver_email, reply_message):

    sender_email = st.secrets["EMAIL_ADDRESS"]
    app_password = st.secrets["EMAIL_PASSWORD"]

    msg = EmailMessage()

    msg["Subject"] = "Thank You For Contacting Minimum Strength Gym"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(reply_message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


st.title("🏋️ Gym Email Agent")

name = st.text_input("Customer Name")

email = st.text_input("Customer Email")

message = st.text_area("Customer Inquiry")

if st.button("Submit Inquiry"):

    category = classify_email(message)

    reply = generate_reply(category)

    save_lead(
        name,
        email,
        category,
        message
    )

    try:
        send_email(email, reply)
        st.success("Lead Saved & Email Sent Successfully!")

    except Exception as e:
        st.error(f"Email Error: {e}")

    st.subheader("Category")
    st.write(category)

    st.subheader("Auto Reply")
    st.write(reply)
