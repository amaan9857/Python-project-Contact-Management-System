import streamlit as st
import json
import os

FILE = "contacts.json"

# Load contacts
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        contacts = json.load(f)
else:
    contacts = {}

# Save contacts
def save():
    with open(FILE, "w") as f:
        json.dump(contacts, f)

st.title("Contact Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add", "View", "Search", "Update", "Delete"]
)

# Add Contact
if menu == "Add":
    st.subheader("Add Contact")

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("email")

    if st.button("Add"):
        if name and phone and email:
            contacts[name] = {"Phone": phone, "Email": email}
            save()
            st.success("Contact Added!")
        else:
            st.error("Enter all details")

# View Contacts
elif menu == "View":
    st.subheader("All Contacts")

    if contacts:
        for name, details in contacts.items():

            st.write("Name:", name)
            st.write("Phone:", details.get("phone", details.get("Phone", "Not Available")))
            st.write("email:", details.get("email", details.get("Email", "Not Available")))

            st.divider()

    else:
        st.info("No Contacts Available")

# Search Contact
elif menu == "Search":
    st.subheader("Search Contact")

    name = st.text_input("Enter Name")

    if st.button("Search"):
        if name in contacts:
            st.write(contacts[name])
        else:
            st.error("Contact Not Found")

# Update Contact
elif menu == "Update":
    st.subheader("Update Contact")

    name = st.text_input("Enter Name")
    phone = st.text_input("New Phone")
    email = st.text_input("New Email")

    if st.button("Update"):
        if name in contacts and phone and email:
            contacts[name] = {"Phone": phone, "Email": email}
            save()
            st.success("Contact Updated!")
        else:
            st.error("Contact Not Found or Missing Details")

# Delete Contact
elif menu == "Delete":
    st.subheader("Delete Contact")

    name = st.text_input("Enter Name")

    if st.button("Delete"):
        if name in contacts:
            del contacts[name]
            save()
            st.success("Contact Deleted!")
        else:
            st.error("Contact Not Found")

