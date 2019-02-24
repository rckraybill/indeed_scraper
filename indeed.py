


pages_and_job_count_text = soup.find(name='div', attrs={'id':"searchCount"}).get_text()




def grab_job_links():
	'''get all the job posting links for a given search result page'''

	urls = []

	for link in soup.find_all('h2', {'class':'jobtitle'}):

		partial_url = link.a.get('href')
		url 		= 'https://www.indeed.com' + partial_url
		urls.append(url)

	return urls

def get_urls(query, location):
	'''loop through all the search result pages and get all the job posting links'''
	for i in range(2, num_of_pages + 1): 
		num = (i-1) * 10
		base_url = 'https://www.indeed.com/jobs?q={}&l={}&start={}'.format(query, location, num)
		try:
			soup = get_soup(base_url)
			urls += grab_job_links(soup)
		except:
			continue

def get_soup():
	'''obtain beautiful soup object for given url'''

	driver 	= webdriver.Firefox()
	driver.get(url)

	html 	= driver.page_source
	soup 	= BeautifulSoup(html, 'html.parser')
	driver.close()

	return soup

def get_posting(url):
	'''open a job page posting and parse out the text portion'''
	soup = get_soup(url)
	title = soup.find(name='h3').getText().lower()
	posting = soup.find(name='div', attrs={'class':'jobsearch-JobComponent'}).get_text()

	return title, posting.lower()


def get_data():
	'''loop through the url list'''
