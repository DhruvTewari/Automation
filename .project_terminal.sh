#!/bin/zsh

function project() {
  # path to where the project.py file has been saved
  python project.py $1 $2
  cd /Users/dhruvtewari/Desktop/projects/$1
  # path to where the created file for the newly created project has to be saved
  git init
  git remote add origin https://github.com/{Enter you github username}/$1.git
  touch README.md
  git add .
  git commit -m 'initial commit'
  git push -u origin master
  code . # To open vs code 
  say 'project created ' $1
}