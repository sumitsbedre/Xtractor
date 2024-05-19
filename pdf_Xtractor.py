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
    text_file = r"D:\work\quantum learning\software projects\pdf data extracter\inputs.txt"       
    download_folder = r"D:\work\quantum learning\software projects\pdf data extracter\pdf folder"       
    excel_file = "DATA.xlsx"          

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
