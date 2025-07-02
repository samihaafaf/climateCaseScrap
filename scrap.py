
import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


keyword = 'climate wash'
url = f"https://climatecasechart.com/search/?fwp_search={keyword}&fwp_per_page=500"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
print(response.status_code)
if response.status_code != 200:
    print("Failed")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', class_='entry-title-link')

links = links[150:250]
print(len(links))
# for link in links:
#     print(link['href'])

data = []
def add_file_info(link):

    website = link
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(website) 
    contents = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/article/div/div[2]/ul") # assuming the first table is the one you want


    li_list = contents.find_elements(By.TAG_NAME, "li")
    

    for i, li in enumerate(li_list):
        
        case_name = li.find_element(By.TAG_NAME, "h5")
        entry_data = {"link": link, "entry_index": i,"case name":case_name.text ,"rows": []}
        try:
            table = li.find_element(By.TAG_NAME, "table")
            rows = table.find_elements(By.TAG_NAME, "tr")
            for each in rows:
                cells = each.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 5:
                    col1 = cells[0].text.strip()
                    col4 = cells[3].text.strip()
                    col5 = cells[4].text.strip()

                    if col5:  # only add if col5 is NOT empty
                            entry_data["rows"].append({
                                "Filing Data": col1,
                                "Action taken": col4,
                                "Summary": col5
                            })
            if entry_data["rows"]:
                data.append(entry_data)

        except:
            continue
        driver.quit()


# links = links[0:10] 
for each in range(len(links)):
    print(f"processing {each} of {len(links)} -> {links[each]['href']}")
    add_file_info(links[each]['href'])


with open(f"{keyword}_cases_150-250.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["link","entry_index", "case name", "Filing Data", "Action taken", "Summary"])
    writer.writeheader()

    for entry in data:
        for row in entry["rows"]:
            writer.writerow({
                "link": entry["link"],
                "entry_index": entry["entry_index"],
                "case name": entry["case name"],
                "Filing Data": row.get("Filing Data", ""),
                "Action taken": row.get("Action taken", ""),
                "Summary": row.get("Summary", "")
            })
