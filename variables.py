from dotenv import load_dotenv
import os

load_dotenv()

my_username = os.environ['LINKEDIN_USERNAME']
my_password = os.environ['LINKEDIN_PASSWORD']

file_name = 'results.csv' # file where the results will be saved

page_number = 1
q = 'site:linkedin.com/in/ AND "@gmail.com" AND "DENTIST" AND "California"'
query = q + "&start=" + str((page_number-1) * 100) + "&num=" + str(page_number)