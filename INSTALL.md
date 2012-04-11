# Installation


This installation guide is for Ubuntu Linux in 7 simple steps. It's remainder for me in case I would forget how to run the blog on my computer.


1. Clone the code. `git clone git@github.com:honzajavorek/blog.git`
2. `cd blog`
3. Create a new Python virtual environment. `virtualenv env --distribute`
4. Activate the environment. `. env/bin/activate`
5. In virtual environment, install all Pythonic requirements. `pip install -r requirements.txt`
6. Install SASS. `apt-get install ruby rubygems && gem install sass`
7. Run it. `start.sh`
