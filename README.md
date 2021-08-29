#Musical Time Machine Project
###Creating a Spotify Playlist using the Musical Time Machine
##The Goal
####How music can take you back to particular time in your life as if it's just transported you.
####By listening to the same songs that were hits during that period of time.
####It was like as if I was being transported back and could relive a moment in my childhood.
####And you might have the same experience.
##How It's done
####I used Beautiful Soup to scrape top 100 songs from a particular date of my choice.
####And then I'm extracting all the song titles from the list, and then i'm using the 
####Spotify API to create a new playlist for that particular date.
####And then i'm searching through Spotify for each of the songs and add those songs to the new
####playlist. 
####At the end a new playlist is created that has the top 100 songs for particular date in the past.

###step 1
####Create an input() prompt that asks what year you would like to travel to in YYYY-MM-DD format.
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
####Using Beautiful Soup scrape the top 100 song titles on that date into a Python List.
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.find_all("span", class_="chart-element__information__song")
    song_names = [song.getText() for song in song_names_spans]
#####Take a look at the URL of the chart on a historical date:
####https://www.billboard.com/charts/hot-100/2000-08-12





