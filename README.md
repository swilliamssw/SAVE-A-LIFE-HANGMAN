# __SAVE-A-LIFE-HANGMAN__
 
SAVE A LIFE HANGMAN is a fun and entertaining python terminal game, which is utilised by the Code Institute mock terminal on Heroku. The game allows players to save a life, i.e the hangman by guessing letter untill they have completely guessed the word to win.
The game is aimed towards mainly develper IDE as a small break game. The game is also aimed to all ages, which have a interest in the programming space. 
The game allows new and seniors to the coding space to enjoy the fun side of code, having the chance to play around a python based game.
 
![Responsive Mockup](/assets/images/website-responsive.png)
 
## Features<hr>
 
### Existing Features
 
- __Play Buttons__
 - Featured at the start of the game, the player is welcomed with the home screen, where the Trihub white logo is presented against the teal background.
 - Below the Trihub logo the user is presented with a play button in the center of the screen __GO!__ which links to the main game page where the  player can begin playing the quiz.
 - The other navigation links are the social pages, which are, Instagram, Discord, and Twitter which links to the different social platforms page opening up a new window when doing so.
 - The logo, play button and social links are all in a font that is congruent with the rest of the pages and a color that contrasts well with the background.
 
![GAME HOME PAGE](/assets/images/home-page.png)
 
- __Game Page__
 - The game page is displayed right after the home page and is identical in style and appearance as the home page.
 
![Game Page](/assets/images/game.png)
 
- __Hud Section__
 - The hud section gives the user  information  which question they are on as well as how many questions they have left.
 - The questions tracker, all has a bar which fills as the player answers the questions, to be able to give the player a more visual representation of their progression through the game.
 - On the right hand side is the title score and score tracker, this section keeps a track of the amount of the answered questions that are correct.
 
![Services](/assets/images/hud.png)
 
- __Questions Section__
 - The question section is displayed right above the four possible answers below.
 - This area changes when the player answers each time, and is congruent with both font and colour.
 
 ![Question Section](/assets/images/questions.png)
 
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
- A High Scores page which enables players to keep track of their high scores when playing the game. <br>
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
 