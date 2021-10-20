How to build and run:

In terminal (assuming git has already been downloaded):
git clone https://github.com/freedomzx/cryptoinfo.git

A downloaded Python version is required (tested using 3.8.8 and 3.10, so most modern/near modern Python 3 versions should work.)

After python is downloaded, there are 2 packages that must be installed using pip (automatically included in Python 3)

In terminal:
pip install flask
pip install requests

Once the project is cloned, python 3 is downloaded, and flask + requests have been downloaded using pip, cd into the project folder (cryptoinfo)
and in the terminal type:
flask run

Flask will then automatically utilize port 5000 to host the webpage locally and launch the application. 
This webpage on port 5000 can be accessed using either:

http://localhost:5000/

or 

http://127.0.0.1:5000/


Using either of these addresses, the webpage can now be accessed after executing "flask run".