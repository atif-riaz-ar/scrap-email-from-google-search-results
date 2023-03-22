## LinkedIn Scraper 2023

**Hello. I am Atif Riaz. I am still working on it. Will keep on updating this repository. I start this to reduce the bounce rate of my emails I use for lead generation so emails can better warm up.**

This is the new update concerning the data scraping from [LinkedIn](https://linkedin.com).

![linked data mining](https://woz-u.com/wp-content/uploads/2021/04/woz-what-is-data-mining-1280x720.jpg)

## Tools used for this project
- [Python](https://www.python.org/)
- [Selenium](https://www.seleniumhq.org/)
- [parsel](https://parsel.readthedocs.io/)
- [iPython](https://ipython.org/)

To contribute, you know the story,
- Clone
    - ```
        git clone https://github.com/atif-riaz-ar/scrap-email-from-google-search-results.git
        ```
- Make commits and PRs
    - ```
        git add .
        git commit -m "message"
        git push
        ```

### System Setup

- Download dependencies
    ```bash
        pip install -r requrements.txt

    ```
- Create a `.env` file with the following variables:
    ```bash
        LINKEDIN_USERNAME=**************
        LINKEDIN_PASSWORD=**************
    ```
- Run the scraper
    ```bash
        python main.py
    ```

The scraper will automatically login and scrape the data.