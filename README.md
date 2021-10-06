# EMLO Session 3

The objective of this session was to amend an existing repo with the given requirements) and upload to Heroku.

Requirements:
- [x] Show your name 
- [x] Add dropdown menu to chose between personal information and homepage
- [x] Give credit to original author
- [x] Three file upload on homepage using single button
- [x] Last five results
- [x] Present with sample image on home page

No changes were made to the model/inference.

All the above requirements are satisfied and can be seen after clicking on the 'About Project' link. 

# Steps 

After entering the virtual environment created for the assignment and installing the required dependencies, the following commands were executed in the shell.

```
heroku login -i
heroku create ___
heroku local
pip freeze > requirements.txt
- add +cpu next to torch and torchvision
git init
heroku git:remote -a ___ (same as in line 2)
git add .
git config user.name "____"
git config user.email "______"
git commit -m "Final App"
git push heroku master
git remote set-url origin git@github.com:mmgxa/EMLO_S3.git
git push origin master

```