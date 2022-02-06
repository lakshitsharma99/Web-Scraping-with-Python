from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.roberthalf.com/blog/salaries-and-skills/the-13-highest-paying-it-jobs-in-2019").text
soup = BeautifulSoup(site, 'html.parser')

top_heading  = soup.find('h1', class_="page-title node--type-rh-blog rh-blog__node-title rh-taxonomy__node-title").text
print(top_heading)

titles  = soup.find_all('h2', class_="rh-display-2--rich-text")

for title in titles:
    print(title.text)

f = open("Top 15 Tech Job.txt", "w")
f.writelines(f"{top_heading} \n\n")

for title in titles:
    data = title.get_text()
    f.writelines(f"{data} \n")
print("File Saved Successfully")