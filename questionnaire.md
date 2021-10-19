1.	Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?


I believe most of the sub-optimal implementation has to do with how the information is actually gotten through the http requests (will elaborate more in question 3).  In addition, the exchanges used on the webpage are hard coded in a list, even though there are methods and resources that can be used to gather a sizeable amount of commonly-used exchanges automatically.


2.	Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)
In order 


In order to implement some sense of scalability for future improvements and additions, the webpage is capable of displaying information of more than two exchanges.  The code was written such that it could handle and give recommendations for any amount of exchanges that is 2 or greater.

3.	If you have to scale your solution to 100 users/second traffic what changes would you make, if any?

The main issue right now with my implementation of this webpage is that it only accounts for the usage traffic of a small amount of people.  The API used to gather information, cryptowat.ch, sets a rate limit for requests.  When I gather information to fill the table on the website and get information for recommendations, it calls the API once for every exchange that is being observed.  Right now, this means that there are 7 API calls per button press.  Should we find 100 users/second using this website, this rate limit would be reached extremely quickly.  To circumvent this, either an API key has to be paid for or a method to gather information directly from the exchanges by examining and parsing their HTML would have to be implemented.  The first method would be expensive monetarily, while the second method would be very costly in terms of time.

4.	What are some other enhancements you would have made, if you had more time to do this implementation

The main things I would improve in terms of the actual assignment are a better looking interface and a way to handle more exchanges without bieng quickly rate-limited by a third party API in order to showcase some form of easy scalability.  

Things that I want to improve outside the scope of the assignment would be historical graphs for ask/bid on each of the exchanges, support for more currency, and  more statistical information on different sections on the webpage.