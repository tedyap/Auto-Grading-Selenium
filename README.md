# Grade Assignments and Upload Feedbacks with Selenium

This code automatically input grades and upload feedback files on Moodle using Selenium, an open-source web-based automation tool.

## Usage
First install all the dependencies by running:
```
pip install -r requirements.txt
```

Once all dependencies are installed, run:
```
python3 homework.py <assignment_name> <id_number>
```
Assignment specifies the folder name to retrieve grades and feedback files from. Id number refers to the id query string in the url on Moodle.com.
