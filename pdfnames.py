#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.title("PDF File Names to Excel")

# Text input for Excel file name
excel_file_name = st.text_input("Enter Excel file name (without extension)", "pdf_file_names")

# Allow multiple file uploads
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files and excel_file_name.strip():
    # Get just the file names
    pdf_names = [file.name for file in uploaded_files]

    # Create a DataFrame
    df = pd.DataFrame(pdf_names, columns=["PDF File Names"])

    # Convert the DataFrame to an Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="PDFs")

    output.seek(0)

    # Download button
    st.download_button(
        label="Download Excel file",
        data=output,
        file_name=f"{excel_file_name.strip()}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
elif not uploaded_files:
    st.info("Upload one or more PDF files to get started.")
elif not excel_file_name.strip():
    st.warning("Please enter a valid Excel file name.")


# In[ ]:




