# WEB SCRAPING FROM A FAKE JOB WEBSITE

# import libraries
import re
import requests
from bs4 import BeautifulSoup

# retrieve the website's DOM
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# create an object to make it look better readable
soup = BeautifulSoup(page.content, "html.parser")

# finding specific id's
results = soup.find(id="ResultsContainer")

# finding elements by class name (all jobs)
jobs = results.find_all("div", class_="card-content")


# function for all jobs
def allJobs():
    # going to all jobs
    print("Found: {} jobs\n".format(len(jobs)))
    for i in range(len(jobs)):
        title = jobs[i].find("h2", class_="title")
        company = jobs[i].find("h3", class_="company")
        location = jobs[i].find("p", class_="location")
        print("Number: {} / {}".format(i + 1, len(jobs)))
        print("Title: {}".format(title.text.strip()))
        print("Company: {}".format(company.text.strip()))
        print("Location: {}".format(location.text.strip()))

        # retrieving links
        link_url = jobs[i].find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")

        print()


# function filter for jobs
def titleJobs(name, par):
    # finding the filter parameter
    jobsFilter = results.find_all(
        par, string=re.compile(name, re.IGNORECASE)
    )

    # putting it in a list from child
    jobsDeep = [
        element.parent.parent.parent for element in jobsFilter
    ]
    print("Found: {} jobs\n".format(len(jobsDeep)))

    # iterate through parameter jobs
    for i in range(len(jobsDeep)):
        title = jobsDeep[i].find("h2", class_="title")
        company = jobsDeep[i].find("h3", class_="company")
        location = jobsDeep[i].find("p", class_="location")
        print("Number: {} / {}".format(i + 1, len(jobsDeep)))
        print("Title: {}".format(title.text.strip()))
        print("Company: {}".format(company.text.strip()))
        print("Location: {}".format(location.text.strip()))

        # retrieving links
        link_url = jobsDeep[i].find_all("a")[1]["href"]
        print(f"Apply here: {link_url}\n")

        print()


# user inputs and handling exceptions
print("Search for Fake Jobs on: https://realpython.github.io/fake-jobs/")
userInput = 0
try:
    userInput = int(input("Please enter the number of your sort filter:\n1 - All Jobs\n2 - Title\n3 - Company\n4 - "
                          "Location\nAnswer: "))
except ValueError:
    print("Something went wrong, please typing a number!")

# conditions for user inputs
if userInput == 1:
    print()
    allJobs()
elif userInput == 2:
    print()
    string = input("Enter the title: ")
    print()
    titleJobs(string.lower(), "h2")
elif userInput == 3:
    print()
    string = input("Enter the company: ")
    print()
    titleJobs(string.lower(), "h3")
elif userInput == 4:
    print()
    string = input("Enter the location: ")
    print()
    titleJobs(string.lower(), "p")
else:
    print()
    print("Please enter a number between 1 and 4!")