import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# use requests package to get  response of url and search about the jobs using the title
job_search = "back%end"
page_num = 0

job_titles = []
job_links = []
job_companies = []
job_locations = []
job_skills = []

while True:
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&filters%5Bpost_date%5D%5B0%5D=within_1_month&filters%5Byears_of_experience_max%5D%5B0%5D=2&q={job_search}&start={page_num}")

    if result.status_code != 200:
        print("Can not get page")
        raise Exception("Can not get the page")

    # take the content of the response page
    # the response of the requests get return dictionary with many keys
    content = result.content

    soup = BeautifulSoup(content, "lxml")

    # get the data needed to save them with their tags
    job_titles_tags = soup.find_all("h2", {"class": "css-m604qf"})
    job_companies_tags = soup.find_all("a", {"class": "css-17s97q8"})
    job_locations_tags = soup.find_all("span", {"class": "css-5wys0k"})
    job_skills_tags = soup.find_all("div", {"class": "css-y4udm8"})

    # take only the actual needed data
    for i in range(len(job_titles_tags)):
        job_titles.append(job_titles_tags[i].text)
        job_companies.append(job_companies_tags[i].text)
        job_locations.append(job_locations_tags[i].text)
        job_skills.append(job_skills_tags[i].text)

        job_link = job_titles_tags[i].find("a", {"class": "css-o171kl"}).attrs["href"]
        job_links.append(job_link)

    page_limit = soup.find("strong").text
    if page_num >= (int(page_limit) // 15):
        print(f"Page limit {page_limit} reached at {page_num}")
        break

    page_num += 1

# save the data at Excel file
file_data_list = [job_titles, job_links, job_companies, job_locations, job_skills]
exported = zip_longest(*file_data_list)
with open("documents/job_links.csv", "w") as jobs_links_file:
    wr = csv.writer(jobs_links_file)
    wr.writerow(["Job Title", "Job Link", "Company", "Location", "Skills"])
    wr.writerows(exported)