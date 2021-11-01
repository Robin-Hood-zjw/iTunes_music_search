#########################################
##### Name:JIAWEN ZHANG             #####
##### Uniqname: jiawenz             #####
#########################################


import json
from typing import ItemsView, final
import requests

#Part 2

class Media():
    print("xxxx")
    def __init__(self, title="No Title", author="No Author",
    release_year="No Release Year", url="“No URL", json=None):
        if json == None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            if "trackName" in json:
                self.title = json["trackName"]
            if "trackViewUrl" in json:
                self.url = json["trackViewUrl"]
            else:
                self.title = json["collectionName"]
                self.url = json["collectionViewUrl"]
            self.author = json["artistName"]
            self.release_year = json["releaseDate"][:4]


    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        return 0


class Song(Media):

    def __init__(self, 
    title="No Title",
    author="NoAuthor ",
    release_year = "No Release Year",
     url = "“No URL",
     json=None,
     album =  "No Album",
     genre = "No Genre",
     track_length = 0
     ):
        super().__init__(title, author, release_year, url, json)
        self.album= album
        self.genre = genre
        if json == None:
            self.track_length = track_length
        else:
            self.track_length = json["trackTimeMillis"]


    def info(self):
        return super().info() + f"{self.genre}"

    def length(self):
        return super().length()


class Movie(Media):

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="“No URL", json=None, rating="No Rating", movie_length=0):
        super().__init__(title, author, release_year, url, json)
        self.rating = rating
        self.movie_length = movie_length
        if json == None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            if ("collectionName" in json):
                self.title = json["collectionName"]
                self.author = json["artistName"]
                self.release_year = json["releaseDate"][:4]
            elif ("trackName" in json):
                self.title = json["trackName"]
                self.author = json["artistName"]
                self.release_year = json["releaseDate"][:4]

            elif ("trackViewUrl" in json):
                self.url = json["trackViewUrl"]
            else:
                self.url = json["collectionViewUrl"]

    def info(self):
        return super().info() + f"{self.rating}"

    def length(self):
        return super().length()

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    baseURL = "https://itunes.apple.com/search?term="

    firstNotice = 'Enter a search term, or "exit" to quit: '
    userInput = input(firstNotice)
    while (True):
        if (not userInput):
            userInput = input(firstNotice)
            continue
        if (userInput == "exit"):
            break
        else:
            stored_dict = {"term": userInput}
            systemResponse = requests.get(baseURL + userInput)
            outputObj = systemResponse.json()
            itunesList = outputObj["results"]
            if (not itunesList):
                print(" No result for your input. Try again! ")
                userInput = input(firstNotice)
                continue
            else:
                break



    songList = []
    moviesList = []
    mediaList = []
    finalList = []

    def fill_List(target_list):
        for genre in itunesList:
            if ("kind" in genre.keys()):
                if (genre["kind"] == "song"):
                    target_list.append(Song(json=genre))
                elif (genre["kind"] == "feature-movie"):
                    target_list.append(Movie(json=genre))
                else:
                    pass
            else:
                target_list.append(Media(json=genre))
    
    fill_List(songList)
    fill_List(moviesList)
    fill_List(mediaList)

    countNum = 1
    for song in songList:
        finalList.append(song)
        countNum += 1
    for movie in moviesList:
        finalList.append(movie)
        countNum += 1
    for media in mediaList:
        finalList.append(media)
        countNum += 1

    displayNum = 1

    print("SONGS")
    if (songList != None):
        for item in songList:
            print(f"{displayNum}", " ", item.info())
            displayNum += 1

    print("MOVIES")
    if (moviesList != None):
        for item in moviesList:
            print(f"{displayNum}", " ", item.info())
            displayNum += 1

    print("OTHER MEDIA")
    if (mediaList is not None):
        for item in mediaList:
            print(f"{displayNum}", " ", item.info())
            displayNum += 1

    secNotice = "Enter a number for more info, or another search term, or exit: "
    web_userInput = input(secNotice)

    while True:
        if (type(web_userInput) == str and web_userInput.lower().strip() == "exit"):
            print("Thank you for using iTunes! See you later!")
            break
        else:
            try:
                if (type(web_userInput) == str and web_userInput.isnumeric()):
                    web_userInput = int(web_userInput)
                    if web_userInput in range(len(finalList)+1):
                        indexNum = web_userInput - 1
                        urlPreview = finalList[indexNum].url
                        webResponse = requests.get(urlPreview)
                        print(f"Lauching \n{urlPreview} in web browser...")
                        break
                elif (type(web_userInput) == int):
                    if web_userInput in range(len(finalList)+1):
                        indexNum = web_userInput - 1
                        urlPreview = finalList[indexNum].url
                        webResponse = requests.get(urlPreview)
                        print(f"Lauching \n{urlPreview} in web browser...")
                        break
                    else:
                        thirdNotice = "Please choose an integer within the given range:"
                        web_userInput = input(thirdNotice)
            except:
                songList.clear()
                moviesList.clear()
                mediaList.clear()
                finalList.clear()
                continue