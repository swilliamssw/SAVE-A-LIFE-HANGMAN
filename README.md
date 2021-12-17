# __SAVE-A-LIFE-HANGMAN__
 
SAVE A LIFE HANGMAN is a fun and entertaining python terminal game, which is utilised by the Code Institute mock terminal on Heroku. The game allows players to save a life, i.e the hangman by guessing letter untill they have completely guessed the word to win.
The game is aimed towards mainly develper IDE as a small break game. The game is also aimed to all ages, which have a interest in the programming space. 
The game allows new and seniors to the coding space to enjoy the fun side of code, having the chance to play around a python based game.
 
![Responsive Mockup](/assets/images/responsive-design.png)
 
## Features<hr>
 
### Existing Features
 
 __GAME MENU__
 - At the start if the game the player is greeted with the SAVE A LIFE HANGMAN logo,follow by a repersention of the hanged man. 
 - Below all of that the player is presented with three options to choose from, which is 1 Play game, 2 choose difficutly and 3 read game rules. 
 - The player is able to navigate freely through out the game menu to view all these options
 
![GAME HOME PAGE](/assets/images/game-home-screen.png)
 
 __PLAY GAME__
 - The play is able to play the game straight away by choosing option 1 which will provide the player with 7 lives, this is also known as the Normal mode. 
 - upon the player choosing option 1 the game is instantly loaded up with the 7 lives and a random word to start guessing. 
 
![Play Game](/assets/images/default-mode.png)

 __DIFFICULTY SELECTION__
 - The difficulty selction is displayed after choosing option 2, which will then display 4 options to choose from the for player. 
 - 1 for Easy mode, 2 for Normal mode, 3 for Hard Mode and 4 for Expert mode. This gives the player more of a challenge in the game, allowing them to think more carefully before making a decision. 
 - This Provide less lives the hard the game  is set with 10 for easy, 7 for normal, 5 for hard and lastly 3 for the experts. 
 
![Difficulty Selection](/assets/images/difficulty-selection.png)
 
 __GAME RULES__
 - Upon the player choosing option 3 the player is presented with the games rules, which explains to the player the basics of how the game works. 
 - The player after reading the rules is then able to press enter to exit this seciton of the game and is relocated back to game menu, allowing them to choose other options of the two above it to play on. 

 ![Game Rules](/assets/images/game-rules.png)
 
- __Answer Section__
 - The answer section displays four labeled tabs which have each possible answers to the questions presented above it.
 - The tabs display A-D labels on the left side to indicate the answer for the player.
 - Over in the middle of the tabs is the actual answers for the player to choose from.
 - The tabs have animation on them which allow them to glow and raise to indicate the answer that the player is planning on picking before they click on it, which provides more indication to the player of the answer they are picking.
 
 ![Answers Section](/assets/images/answers.png)
 
__Correct Answer__
 - The game gives indication by showing a pop up which says "Good Job" to indicate to the player that they have successfully answered the question correctly.
 - The pop up is timed and only lasts a few seconds before disappearing and revealing the next question.
 
![Footer](/assets/images/correct-answer.png)
 
__Incorrect Answer__
- The game gives indication by showing a pop up which says "SORRY NOT RIGHT! THE CORRECT ANSWER IS" to indicate to the player that they have successfully answered the question correctly.
- This also indicates to the player what the correct answers for that specific question that had answered.
- The pop up is also timed and disappears after a few seconds and then displays the following question.
 
![Footer](/assets/images/incorrect-answer.png)
 
__End Game Page__
- The game gives indication by showing a pop up which says "SORRY NOT RIGHT! THE CORRECT ANSWER IS" to indicate to the player that they have successfully answered the question correctly.
- This also indicates to the player what the correct answers for that specific question that had answered.
- The pop up is also timed and disappears after a few seconds and then displays the following question.
 
![Footer](/assets/images/endGame-page.png)
 
### Features Left to Implement
- Features i would like to implement later on would be to show all the  <br>
This  will require them to log their name once finished the game and this will store both their score and name in a separate page which allows them to look back at,, at a later date to bring more of a competitive feel to the game.
 
## Testing<hr>
  - I tested this page works on different browsers: Chrome, Firefox, Safari.
  - I confirmed that this project is responsive, looks good and functions on all standard screen sizing, using devtools device toolbar.
  - I confirmed that the navigation, header, Home, About Us, Explore, Sign up form & footer text are all readable and easy to understand.
  - I have confirmed that the form works: requires entries in every field, will only accept an email in the email field and the submit and cancel button works.
 
### Validator Testing
- PEP8  
 - No errors were returned when passing through the official W3C validator.
[PEP8](http://pep8online.com/)
 
 ![](/assets/images/pep8-validation.png)


## Unfixed Bugs
 
## Deployment
- The site was deployed to Heroku, utilising the Code institute mock terminal.
  The steps to deploy are as follows:
  - Any final commits for the game were push to the repository on Git Hub.
  - A new account with Heroku was made, after which settings was opened to reveal 
    app name and buildpacks.
  - App name was added inaccordance with project name. 
  - Python and nodejs packs were set in the buildpacks section.
  - Navigated to deploy tab clicking on GitHub for deployment method.
  - App was connected to GitHub by locating repository and connnecting.
  - Scrolling down to Manual deploy, the branch was set to main, and deploy branch button was clicked.
  - After waiting for app to be built a link will be provided by Heroku to access the app. 

The live link from Heroku can be found here - https://save-a-life-hangman.herokuapp.com/
 
## Credits / References<hr>
 
### Content
- To understand the basic structure and layout of the game, which help bring alot of clarity when understanding the logic. [YouTube](https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite)
 
- This was used to bring more understanding to some of the errors found when cleaning up the code. [Flake 8](https://www.flake8rules.com/rules)
 
- The graphics for the title, game over and you win was taken from here. [Patorjk](https://patorjk.com/software/taag/#p=display&v=1&f=Small&t=SAVE%20A%20LIFE%0A%20%20HANGMAN)

- This helped me understand and figure out synatax for python abit better for while loops. [W3SCHOOL](https://www.w3schools.com/python/python_while_loops.asp)

- For the mock terminal to be able to deploy to a live site. [CodeInstitute](https://codeinstitute.net/)

- Richard Wells for his good advice and guidence on breaking things down into manageable portions [RichardWells](https://github.com/D0nni387)
 