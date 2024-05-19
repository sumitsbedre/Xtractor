# Xtractors
This are Python based project that can be used to extract information from given links, Fetch information from them (of that link) and present it as an Excel file. 

# Description
PDF Data Extractor is a Python script designed to automate the process of downloading PDFs from a list of URLs, extracting specific information from each PDF, saving the extracted information into an Excel file, and then cleaning up by deleting the downloaded PDF files. This tool is particularly useful for batch processing large numbers of PDF files to extract standardized data fields (for e.g: the name of an organization, the head of the organization, mobile numbers, and email addresses.)

# Features
Extract PDF Links: Reads a text file containing URLs of PDFs to be processed.
Download PDFs: Downloads PDF files from the given URLs and saves them to a specified folder.
Extract Information: Extracts specific information from each PDF, such as:
Name of the Organization
Name of the Head of the Organization
Mobile Number
Registered Email / Alternate Email
Save to Excel: Writes the extracted information to an Excel file.
Clean Up: Deletes the downloaded PDF files after processing.

# Requirements
-> Python 3.x (The latest version You can have)
-> pandas
-> requests
-> pdfplumber

code: pip install pandas requests pdfplumber
