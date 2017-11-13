# program to get top 10 quotes of Mark Twain from Goodreads
#
# Author : Shravani Ramisetty
# Dated : 11/12/2017
#

import datetime
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import requests


# function to validate the credentials provided by user
def validateUserCredentials(website,userEmail,userPassword):
    browser= RoboBrowser()
    browser.open(website)
    signInForm = browser.get_form()
    signInForm['user[email]'].value = userEmail
    signInForm['user[password]'].value = userPassword
    browser.submit_form(signInForm)
    string1 = str(browser.parsed)

    if "recognize that email/password combination. Please try again." in string1:
        check= 'notValid'
    else:
        check= 'valid'
    return check

#function to retrieve the quotes of Author
def getQuotesList(authorName):
    if(authorName== ''):
        return 'No author name provided'
    else:
        pageNumber = 1
        numberOfQuotes = 10
        # authorName = 'Mark Twain'
        url = "https://www.goodreads.com/quotes/search?commit=Search&page=" + str(
            pageNumber) + "&q=" + authorName + "&utf8=%E2%9C%93"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html")
        finalResponse = {}
        finalResponse['Author'] = authorName
        currentTimeStamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        finalResponse['File Generated on'] = currentTimeStamp
        finalResponse['DataRetrived'] = 'Top ' + str(numberOfQuotes) + ' quotes of' + authorName
        finalQuoteList = []
        counter = 0
        for i in soup.findAll('div', {'class': 'quote mediumText '}):
            try:
                soupVar = BeautifulSoup(str(i), "html.parser")
                quoteDetails = soupVar.find('div', {'class': 'quoteDetails '})
                soupQuoteDetails = BeautifulSoup(str(quoteDetails), "html.parser")
                quoteText = soupQuoteDetails.find('div', {'class': 'quoteText'})
                # extracting the quote of author
                quote = quoteText.contents[0].strip()
                soupQuoteText = BeautifulSoup(str(quoteText), "html.parser")
                quoteTitle = soupQuoteText.find('a', {'class': 'authorOrTitle'})
                # extracting the author
                author = quoteTitle.string.strip()
                # print (quote)
                if author.upper() != authorName.upper():
                    continue
                quoteFooter = soupQuoteDetails.find('div', {'class': 'quoteFooter'})
                soupFooterRight = BeautifulSoup(str(quoteFooter), 'html.parser')
                quoteLikes = soupFooterRight.find('a', {'class': 'smallText'})
                url = "https://www.goodreads.com" + quoteLikes.get('href')
                likesString = quoteLikes.string.strip()
                likes = (int)(likesString.split(" ")[0])
                quotesList = {}
                quotesList['quote'] = quote
                quotesList['likes'] = likes
                finalQuoteList.append(quotesList)
                counter += 1
                if (counter > numberOfQuotes):
                    break

            except Exception, e:
                continue
        finalResponse['Quotes'] = finalQuoteList
        return finalResponse



def main():

    website = 'http://www.goodreads.com'
    # take credentials input from user
    userEmail=raw_input("Enter email-address")
    userPassword= raw_input("Enter password")
    isValid=validateUserCredentials(website,userEmail,userPassword)
    if isValid=='valid':
        authorName=raw_input("Enter the Author Name")
        Response=getQuotesList(authorName)
        print (Response)
    else:
        print("Invalid Credentials..")


if __name__== "__main__":
  main()
