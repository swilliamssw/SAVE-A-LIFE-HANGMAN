# __SAVE-A-LIFE-HANGMAN__
 
SAVE A LIFE HANGMAN is a fun and entertaining python terminal game, which is utilised by the Code Institute mock terminal on Heroku. The game allows players to save a life, i.e the hangman by guessing letter untill they have completely guessed the word to win.
The game is aimed towards mainly develper IDE as a small break game. The game is also aimed to all ages, which have a interest in the programming space. 
The game allows new and seniors to the coding space to enjoy the fun side of code, having the chance to play around a python based game.
 
![Responsive Mockup](/assets/images/responsive-design.png)
 
## Logic Flow Chart
__LOGIC FLOW CHART__
-


![Flow Chart](/assets/images/)
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
 
__GAME DISPLAY__
 - Within the game the games display, the player is presented with the hangman graphics which changes in accordance of the player guessing incorrect answers. 
 - The state is also dependeant on the difficulty the player has chosen also. 
 - Below this the lives counter is presented which indicates to the player how many lives they have started with and how much they have left.
 - Below this the player is presented with the hidden word which is revealed letter by letter based on the what the player has answered correctly. 
 - Below the hidden word, the letters guessed section is displayed which indicates to the player what letters they have used to guess already. 
 - Lastly there is a section for the player to present their guessed letter.   

 ![Game Display](/assets/images/display.png)
 ![Game Display](/assets/images/correct-answer.png)
 
__CORRECT ANSWER__
 - On a successful correct guess given by the player the following message is presented, "Great guess! _ is the in the word.". 
 - This indicates to the player they have guessed correctly one of the letters correctly. 
 - In the example below you can see that the player has guessed "A", now if a word does contain one or more this is automatically populted for the player, allowing them to complete the word and gain more clues to what the word may be.

![Correct Answer](/assets/images/correct-answer.png)
 
__INCORRECT ANSWER__
- When a player make a incorrect guess, the following message is displayed to notify them of their incorrect guess, "_ is not correct.
- This then results in the player losing a life and the word being add to the guessed list.
 
![Incorrect Answer](/assets/images/game-easy-mode.png)
 
__GAME OVER__
- Once the player has ran out of lives the player will be presented with a Game OVER graphic which will have the following message above, "OH NO! It's a very unfortante day, you was unable to save the man this time. The correct word was ______. "Better luck next time.". 

![Game Over](/assets/images/game-over.png)

__YOU WIN__
- If the player were to successfully guess the word correctly before running out of lives, the player would be presented with a You Win! Graphic, which will indicate to the player that they have successfully aguessed the word and won the game. 
- The follwoing message would be displayed to the player, "CONGRATULATIONS YOU WIN! YOU SAVED A LIFE TODAY!".

![You Win](/assets/images/you-win.png)

__PLAY AGAIN__
- Once the player has either recieved either the game over or you win message the player will be presented with a play again option. 
- This play again  option would be presented below the graphics and will give the player to type "Y" for play again with the previous amount of lives or "N" to be navigated back to the main menu.

![Play Again](/assets/images/play-again.png)
![Play Again-No](/assets/images/play-again-no.png)

__INVALID INPUT__
- If the player were to input a value other that a-z the player would be presented with a message indicating them to guess useing any letter form a-z. 
- The message would be, "Sorry that is not a valid inout, please guess a letter from A-Z".
- This would also be the case, the player is instantly allowed to try again using the valid input suggested.

![Invalid Input](/assets/images/invalid-input.png)
![Invalid Input](/assets/images/invalid-input-number.png)
 
### Features Left to Implement
- Features that would be implemented at a later date, would be a player name tracking and score keeping system.
- This would allow the players to become more competitive and add more of a challenge for the game itself. 
- Other features include colours for the texts to give it more of a assteticly pleaseing look.

 
## Testing<hr>
  - I tested this page works on different browsers: Chrome, Firefox, Safari.
  -




## Unfixed Bugs
-





![Error](/assets/images/error-found.png)

### Validator Testing
- PEP8  
 - No errors were returned when passing through the official W3C validator.

[PEP8](http://pep8online.com/)
 
 ![PEP8 Validation](/assets/images/pep8-validation.png)

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
 