<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Xtractor📊📊</h1>
    <div class="container">
        <h1>Xtractor</h1>
        <p>Tired of Boss asking you to fetch data from bulk, and presenting it to excel sheets? Is your higher ups to get data for many attributes and not getting details before deadline? No worries, this repo saves time, buddy😀😀</p>
        <p>This repository contains Python scripts to extract data from either a text file or directly from PDF files and store it in an Excel workbook. It's particularly useful for scenarios where data is distributed across multiple PDFs or a text file.</p>
        <p>Just provide a txt file full of links and let Python do your work. Get 1000's of data within 10 mins</p>
        <h2>Features:</h2>
        <p>Basically, there are 2 programs that can be run as python file in any IDE you desire. Just install a good and confortable IDE and follow the steps to get the desired output. You can directly use the code given if you don't want any hussle.</p>
        <h5>The programs can: </h5>
        <ul>
            <li>Extract from Text File: Extracts organization details from a text file and stores them in an Excel workbook.</li>
            <li>Extract from PDFs: Downloads PDF files from provided links, extracts specific information from them, and saves it in an Excel workbook.</li>
        </ul>
        <h2>Prerequisites:</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Required Python libraries: <code>openpyxl</code>, <code>pdfplumber</code>, <code>pandas</code>, <code>requests</code></li>
        </ul>
        <h2>Usage:</h2>
        <ol>
            <li>Clone the repository to your local machine.</li>
            <li>Install the required Python libraries if not already installed:
                <br><code>pip install openpyxl pdfplumber pandas requests</code>
            </li>
            <li>Prepare your input files:
                <ul>
                    <li>For the first script, provide a text file containing school details.</li>
                    <li>For the second script, provide a text file with links to PDF files.</li>
                </ul>
            </li>
            <li>Update the file paths and other configurations in the scripts if necessary.</li>
            <li>Run the scripts:
                <br><code>python extract_school_details.py</code>
                <br><code>python extract_pdf_data.py</code>
            </li>
        </ol>
        <h2>Example:</h2>
        <p>To extract school details:</p>
        <ul>
            <li>Provide the path to the text file containing school details.</li>
            <li>The script will generate an Excel file named <code>school_details.xlsx</code> with the extracted information.</li>
        </ul>
        <p>To extract data from PDFs:</p>
        <ul>
            <li>Provide a text file containing links to PDF files.</li>
            <li>The script will download the PDFs, extract specific information, and save it in an Excel file named <code>DATA.xlsx</code>.</li>
        </ul>
        <h2>Contributing:</h2>
        <p>Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.</p>
    </div>
</body>
</html>
