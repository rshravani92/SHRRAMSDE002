# SHRRAMSDE002
To get top 10 quotes of Author from Goodreads

Details
The program is developed as a Python 2.7 script in GetAuthorTop10Quotes.py
The testcases are in GetAuthorTop10QuotesTest.py
The program will authorize the user to Goodreads website and search for top 10 quotes of Author (currently Mark Twain) and produce the output on console with list of quotes and likes of each quote
The details of author, quote list and time stamp of file generation and what data is retrieved are provided in the response
Instructions to run the program
The program can be imported as new project in IDE like PyCharm to be executed
To get the list of required quotes, the user have to provide valid login credentials. If not existing user, can sign up in following link
https://www.goodreads.com/
Design Assumptions
The basic assumptions are: 
1.	The user is already a member of Goodreads with valid user credentials
2.	Currently implemented without performing any sorting logic after extraction, as website is returning the top 10 based on number of likes (can be extended to implement sorting using heaps)
3.	As the top 10 quotes are available on the first page in most of the scenarios, functionality to implement search in multiple pages is not yet implement. But the program is flexible to implement the solution as any values are not hardcoded.
4.	The number of quotes can be increased or decreased in future as per the need.
5.	The test cases written are basic unit test cases performing check on the different kinds of input to each function.
6.	Integration test cases can be written to check the overall functionality of the code.


