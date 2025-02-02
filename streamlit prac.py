import streamlit as st
from st_files_connection import FilesConnection

# Ensure credentials are loaded from secrets
conn = st.connection("gcs", type=FilesConnection)

# Define the file path in the GCS bucket
bucket_file_path = "streamlit-test1/myfile.csv"  # Make sure this file exists in GCS

# Read CSV File from GCS
df = conn.read(bucket_file_path, input_format="csv", ttl=600)

# Display Data
st.write("## CSV File Content:")
st.dataframe(df)

# Loop through rows and display formatted content
st.write("## Formatted Output:")
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
