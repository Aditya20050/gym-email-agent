
import streamlit as st
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
Thank you for contacting Minimum Strength Gym.

For membership details, please contact:
+91 9876543210
"""

    elif category == "trainer":
        return """
Thank you for your interest in Personal Training.

Please contact:
+91 9876543210
"""

    else:
        return """
Thank you for contacting Minimum Strength Gym.

Please call:
+91 9876543210
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

    st.success("Lead Saved Successfully!")

    st.subheader("Category")
    st.write(category)

    st.subheader("Auto Reply")
    st.write(reply)
