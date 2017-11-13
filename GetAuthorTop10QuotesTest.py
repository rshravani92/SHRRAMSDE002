#
# Author : Shravani Ramisetty
# Dated : 11/12/2017
#

import unittest
import GetAuthorTop10Quotes

class MyTestCase(unittest.TestCase):
    # checking for null user name and null password
    def test_authentication_valid_credentials(self):
        from GetAuthorTop10Quotes import validateUserCredentials
        testOutput = validateUserCredentials('http://www.goodreads.com', "shravsramisetty@gmail.com", "chinnari92")
        self.assertEqual(testOutput,'valid')

    # checking for null user name
    def test_authentication_empty_username(self):
        from GetAuthorTop10Quotes import validateUserCredentials
        testOutput = validateUserCredentials('http://www.goodreads.com', "", "msekad")
        self.assertEqual(testOutput,'notValid')

    # checking for null password
    def test_authentication_empty_password(self):
        from GetAuthorTop10Quotes import validateUserCredentials
        testOutput = validateUserCredentials('http://www.goodreads.com', "sdjf@mail.com", "")
        self.assertEqual(testOutput,'notValid')

    # checking if author name is not provided
    def test_user_input_author_name(self):
        from GetAuthorTop10Quotes import getQuotesList
        testOutput= getQuotesList("")
        self.assertEqual(testOutput,'No author name provided')


if __name__ == '__main__':
    unittest.main()
