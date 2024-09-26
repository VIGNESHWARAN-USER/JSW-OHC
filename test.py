import streamlit as st
import mysql.connector
import os
from mysql.connector import Error

DB_HOST = 'mysql-5893c62-jsw-test.a.aivencloud.com'
DB_USER = 'avnadmin'
DB_PASSWORD = 'AVNS_uVkEh0awpxi9I4bEOCq'
DB_NAME = 'defaultdb'
DB_PORT = 19129

# MySQL Database Connection Function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
            connection_timeout=10
        )
        return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Function to upload PDF to MySQL
def upload_pdf(file):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Read PDF file
            pdf_data = file.read()
            # Insert into the table
            cursor.execute("UPDATE pdf_files SET file_data = %s WHERE id = 1", (pdf_data,))
            cursor.execute("UPDATE pdf_files SET file_name = %s WHERE id = 1", (file.name,))
            connection.commit()
            st.success("PDF uploaded successfully!")
        except Error as e:
            st.error(f"Failed to upload PDF: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to download PDF from MySQL
def download_pdf():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Fetch all PDF files from the table
            cursor.execute("SELECT id, file_name FROM pdf_files")
            rows = cursor.fetchall()

            # Display available PDFs for download
            if rows:
                st.write("Available PDFs:")
                for row in rows:
                    file_id = row[0]
                    file_name = row[1]

                    if st.button(f"Download {file_name}", key=file_id):
                        cursor.execute("SELECT file_data FROM pdf_files WHERE id = %s", (file_id,))
                        file_data = cursor.fetchone()[0]
                        st.download_button(
                            label=f"Download {file_name}",
                            data=file_data,
                            file_name=file_name,
                            mime="application/pdf"
                        )
                        break  # Prevent creation of multiple buttons
            else:
                st.info("No PDFs available for download.")
        except Error as e:
            st.error(f"Failed to retrieve PDFs: {e}")
        finally:
            cursor.close()
            connection.close()

# Streamlit User Interface
st.title("PDF Upload and Download using MySQL")

# File upload section
uploaded_file = st.file_uploader("Choose a PDF file", type=["jpeg"])
if uploaded_file is not None:
    upload_pdf(uploaded_file)

# File download section
st.write("### Download PDF Files")
download_pdf()
