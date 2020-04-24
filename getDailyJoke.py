import requests
from bs4 import BeautifulSoup
import numpy as np 
from joke.models import Joke

# $some commetns
def get_page_content():
	#gets page content with 99 beautiful jokes hidden in the html soup
	#Gives 0 for error
	page = requests.get("https://www.boredpanda.com/funny-dad-jokes-puns/?utm_source=google&utm_medium=organic&utm_campaign=organic")
	
	if page.status_code == 200:
		soup = BeautifulSoup(page.content, 'html.parser')
		foundJokes = soup.find_all('p', 'post-content-description text-open-list')
	else:
		foundJokes = [0]

	return list(foundJokes)

def parse_jokes(foundJokes):
	#parses jokes from the nasty html line where it was found
	n=0
	for joke in foundJokes:
		joke = str(joke)
		parsedJoke = joke.split(">")[2].split("<")[0]
		foundJokes[n] = parsedJoke
		n+=1
		
	return foundJokes


foundJokes = get_page_content()
parsedJokes = parse_jokes(foundJokes)


print("Adding ", np.size(parsedJokes), " jokes")
count =0
for joke in parsedJokes:
	# Joke.objects.create(joke = joke)
	jokeObject = Joke(joke = joke)
	jokeObject.save()
	count +=1
print("Saved ", count, " jokes!")