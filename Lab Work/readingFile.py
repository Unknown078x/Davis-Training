# Question:  I want to read a text file present in github repository into python in GoogleColab.



# Documentation:

#Step:1-- first we will install the requests module
#Step:2-- then we will import that module
#Step:3-- then we will get the raw file link from github
#Step:4-- then we request the url and store it to response
#Step:5-- now we will extract the text from the response
#Step:6-- print the data


import requests

url = "https://raw.githubusercontent.com/Unknown078x/Davis-Training/refs/heads/main/Classwork/file%20handling/article.txt"

response = requests.get(url)

text = response.text

print(text)