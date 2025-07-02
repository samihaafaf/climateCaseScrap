# Climate Case Scraper

This repository contains a Python-based web scraper that extracts legal case information from [climatecasechart.com](https://climatecasechart.com/) based on keyword searches related to climate change litigation.

---

## Overview

- **`scrap.py`**:  
  The main script that automates the following tasks:
  - Performs a keyword search on [climatecasechart.com](https://climatecasechart.com/)
  - Extracts result page links
  - Visits each case link to collect structured data including:
    - **Filing Date**
    - **Action Taken**
    - **Summary**

  The scraper is built using **Python** and **Selenium**.

- **`scrap.ipynb`**:  
  A rough Jupyter Notebook used for initial prototyping and testing of the scraping logic implemented in `scrap.py`.

---

## Requirements

- Python 3.7+
- [Google Chrome](https://www.google.com/chrome/) browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (compatible with your Chrome version)
- Required Python packages:
  ```bash
  pip install selenium pandas openpyxl

## Use guide
To use this scraper, follow the steps below:

1. Clone the repository to your local machine by running `git clone https://github.com/yourusername/climate-case-scraper.git`, then navigate into the project folder using `cd climateCaseScrape`.

2. Install the required Python packages by running `pip install selenium pandas openpyxl`.

3. Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) that matches your installed version of Google Chrome. Make sure ChromeDriver is accessible via your system's PATH (cache folder on MAC - cmd+shift+G), or place it in the project directory.

4. Open the `scrap.py` file in any code editor and update the `keyword` variable to your desired search term (e.g., `"greenwashing"`).

5. Run the script using the command `python scrap.py`.

6. After execution, the scraper will save the extracted data into a CSV or Excel file (e.g., `greenwashing_cases.xlsx`) in the same directory. The file will include information such as Filing Date, Action Taken, Summary, Case Name, and Link.
