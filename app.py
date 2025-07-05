import streamlit as st
from faker import Faker
import pandas as pd
import json
st.title("Streamlit App")

# Generate Fake Data
st.header("Generate Fake Data Using Faker")
num_records = st.number_input("Number of records to generate", min_value=1, step=1)
if st.button("Generate Data"):
    added_profiles = []
    fake = Faker()
    for _ in range(num_records):
        profile = fake.profile()
        profile['current_location'] = str(profile['current_location'] )
        profile['birthdate'] = str(profile['birthdate'])
        added_profiles.append(profile['name'])
    st.success(f"{num_records} records added successfully!")
    data = pd.DataFrame(added_profiles)
    st.dataframe(data)

# Generate Fake Data
st.header("Generate Fake Profile")
if st.button("Click To Generate Profile"):
    fake = Faker()
    profile = fake.profile()
    json_data = json.dumps(profile, indent=4, default=str)
    st.json(json_data)

# Display DataFrame
st.header("Display DataFrame")
df = pd.read_csv('goalscorers.csv')
if st.button("Show First 10 Rows"):
    st.dataframe(df.head(10))
if st.button("Show By Home Team"):
    home_team = st.selectbox("Select Home Team", df['home_team'].unique())
    st.dataframe(df[df['home_team'] == home_team])

# Selfie Input
st.header("Upload a Selfie")
selfie_file = st.file_uploader("Choose a selfie image", type=["jpg", "jpeg", "png"])
if selfie_file is not None:
    st.image(selfie_file, caption="Uploaded Selfie", use_column_width=True)

# Take Camera Picture
st.header("Take a Picture with Camera")
camera_image = st.camera_input("Take a picture")
if camera_image is not None:
    st.image(camera_image, caption="Camera Capture", use_column_width=True)
