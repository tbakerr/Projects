from pytube import YouTube
link = input("https://www.youtube.com/watch?v=-bn7MLPFYrQ")
yt = YouTube(link)

#Title of video
print("Title:",yt.title)
#Number of views of video
print("Number of views:".yt.views)
#Length of the video
print("Length of video:",yt.length,"seconds")
#Description of video
print("Description:",yt.description)
#Rating
print("Ratings:",yt.rating)


#printing all the available streams
print(yt.streams)

