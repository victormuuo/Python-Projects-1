#import urllib
#use urllib.request to get the data from url
#write a function that takes the url
#returns a response

import urllib.request as urllib

def main(url):
    print("Checking Connectivity")

    response=urllib.urlopen(url)
    print("Connected to", url,  "successfully")
    print("The response code was:", response.getcode())

print("This is  site connectivity checker program") 
input_url=input("Input the url of the site you want to check: ") 
main(input_url)  