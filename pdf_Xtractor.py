'''code is written by: Sumit Arjun.
This code asks for storng Internet connection to download PDF's, so Please fullfill the requirements.
The code is sample code for data extraction of institution data. 
Do make changes according to the information ot data that is asked!!
I am not responsible if your boss kicks you out, if inappropriate data is served to him..☠☠☠
Edit count: 15'''

import pandas as pd
import requests
import os
import pdfplumber

def extract_pdf_links(text_file):
    with open(text_file, 'r') as file:
        pdf_links = [line.strip() for line in file]
    return pdf_links

def download_pdf(pdf_links, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for i, link in enumerate(pdf_links):
        filename = os.path.join(download_folder, f"pdf_{i}.pdf")
        try:
            response = requests.get(link)
            with open(filename, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"Error downloading {link}: {e}")

def extract_information_from_pdf(pdf_folder):
    extracted_info = []
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            try:
                name_of_institution = '-'
                name_of_head = '-'
                mobile_no = '-'
                registered_email = '-'
                alternate_email = '-'

                with pdfplumber.open(os.path.join(pdf_folder, file)) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()

                        # Search for information in the text
                        #pls remember to change the folowing prompt according to the data you need.
                        if "Name of the Institution" in text:
                            name_of_institution = text.split("Name of the Institution")[1].split("\n")[0].strip()
                        if "Name of the head of the Institution" in text:
                            name_of_head = text.split("Name of the head of the Institution")[1].split("\n")[0].strip()
                        if "Mobile no." in text:
                            mobile_no = text.split("Mobile no.")[1].split("\n")[0].strip()
                        if "Registered Email" in text:
                            registered_email = text.split("Registered Email")[1].split("\n")[0].strip()
                        if "Alternate Email" in text:
                            alternate_email = text.split("Alternate Email")[1].split("\n")[0].strip()

                extracted_info.append([name_of_institution, name_of_head, mobile_no, registered_email, alternate_email])
            except Exception as e:
                print(f"Error processing {file}: {e}")
    return extracted_info

def write_to_excel(extracted_info, excel_file):
    df = pd.DataFrame(extracted_info, columns=["Name of the Institution", "Name of the head of the Institution", "Mobile no.", "Registered Email", "Alternate Email"])
    df.to_excel(excel_file, index=False)

def delete_pdf_files(pdf_folder):
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            os.remove(os.path.join(pdf_folder, file))
    print("PDF files deleted successfully.")

def main():
    text_file = r"inputs.txt"       #enter the path for your txt file where all links are stored
    download_folder = r"pdf folder"       #enter the path of your pdf folder, where you want to store your downloaded pdf's
    '''(Don't worry buddy, this data will be deleted, once all data is extracted..If you want to keep the pdfs, then 
    simply stop the code from running when it gives you an alert message of pdf's got downloaded.)'''
    excel_file = "DATA.xlsx"          #enter appropriate name of excel file or its path for data to be stored with .xlsx extension

    # Extract PDF links from text file
    pdf_links = extract_pdf_links(text_file)
    
    # Download PDF files
    download_pdf(pdf_links, download_folder)
    print("PDF files downloaded successfully.")

    # Extract information from PDF files
    extracted_info = extract_information_from_pdf(download_folder)

    # Write extracted information to Excel file
    write_to_excel(extracted_info, excel_file)
    print(f"Extracted information written to {excel_file}.")

    # Delete downloaded PDF files
    delete_pdf_files(download_folder)

if __name__ == "__main__":
    main()
