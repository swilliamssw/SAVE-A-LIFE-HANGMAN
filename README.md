# __SAVE-A-LIFE-HANGMAN__
 
SAVE A LIFE HANGMAN is a fun and entertaining python terminal game, which is utilised by the Code Institute mock terminal on Heroku. The game allows players to save a life, i.e the hangman by guessing letter untill they have completely guessed the word to win.
The game is aimed towards mainly develper IDE as a small break game. The game is also aimed to all ages, which have a interest in the programming space. 
The game allows new and seniors to the coding space to enjoy the fun side of code, having the chance to play around a python based game.
 
![Responsive Mockup](/assets/images/responsive-design.png)
 
## Logic Flow Chart
- Below shows the basic logic structure for SAVE A LIFE HANGMAN. 
- In order to batter visualise and plan the games cycle, this flow chart was disigned to give a logical point of view of the games functionality. 
- You are able to see from start of the game to each options available for the player to pick right through the game being played and ending on either or ither route whether the player wins the game or loses. 

![Flow Chart](/assets/images/logic-flow-chart.png)

## Features<hr>
 
### Existing Features
 
 __GAME MENU__
 - At the start if the game the player is greeted with the SAVE A LIFE HANGMAN logo,follow by a repersention of the hanged man. 
 - Below all of that the player is presented with three options to choose from, which is 1 Play game, 2 choose difficutly and 3 read game rules. 
 - The player is able to navigate freely through out the game menu to view all these options
 
![GAME HOME PAGE](/assets/images/game-home-screen.png)
 
 <hr>

 __PLAY GAME__
 - The play is able to play the game straight away by choosing option 1 which will provide the player with 7 lives, this is also known as the Normal mode. 
 - upon the player choosing option 1 the game is instantly loaded up with the 7 lives and a random word to start guessing. 
 
![Play Game](/assets/images/default-mode.png)
 
 <hr>

 __DIFFICULTY SELECTION__
 - The difficulty selction is displayed after choosing option 2, which will then display 4 options to choose from the for player. 
 - 1 for Easy mode, 2 for Normal mode, 3 for Hard Mode and 4 for Expert mode. This gives the player more of a challenge in the game, allowing them to think more carefully before making a decision. 
 - This Provide less lives the hard the game  is set with 10 for easy, 7 for normal, 5 for hard and lastly 3 for the experts. 
 
![Difficulty Selection](/assets/images/difficulty-selection.png)
  
 <hr>

 __GAME RULES__
 - Upon the player choosing option 3 the player is presented with the games rules, which explains to the player the basics of how the game works. 
 - The player after reading the rules is then able to press enter to exit this seciton of the game and is relocated back to game menu, allowing them to choose other options of the two above it to play on. 

 ![Game Rules](/assets/images/game-rules.png)
  
 <hr>

__GAME DISPLAY__
 - Within the game the games display, the player is presented with the hangman graphics which changes in accordance of the player guessing incorrect answers. 
 - The state is also dependeant on the difficulty the player has chosen also. 
 - Below this the lives counter is presented which indicates to the player how many lives they have started with and how much they have left.
 - Below this the player is presented with the hidden word which is revealed letter by letter based on the what the player has answered correctly. 
 - Below the hidden word, the letters guessed section is displayed which indicates to the player what letters they have used to guess already. 
 - Lastly there is a section for the player to present their guessed letter.   

 ![Game Display](/assets/images/display.png)
 ![Game Display](/assets/images/correct-answer.png)
  
 <hr>

__CORRECT ANSWER__
 - On a successful correct guess given by the player the following message is presented, "Great guess! _ is the in the word.". 
 - This indicates to the player they have guessed correctly one of the letters correctly. 
 - In the example below you can see that the player has guessed "A", now if a word does contain one or more this is automatically populted for the player, allowing them to complete the word and gain more clues to what the word may be.

![Correct Answer](/assets/images/correct-answer.png)
  
 <hr>

__INCORRECT ANSWER__
- When a player make a incorrect guess, the following message is displayed to notify them of their incorrect guess, "_ is not correct.
- This then results in the player losing a life and the word being add to the guessed list.
 
![Incorrect Answer](/assets/images/game-easy-mode.png)
  
 <hr>

__GAME OVER__
- Once the player has ran out of lives the player will be presented with a Game OVER graphic which will have the following message above, "OH NO! It's a very unfortante day, you was unable to save the man this time. The correct word was ______. "Better luck next time.". 

![Game Over](/assets/images/game-over.png)
 
 <hr>

__YOU WIN__
- If the player were to successfully guess the word correctly before running out of lives, the player would be presented with a You Win! Graphic, which will indicate to the player that they have successfully aguessed the word and won the game. 
- The follwoing message would be displayed to the player, "CONGRATULATIONS YOU WIN! YOU SAVED A LIFE TODAY!".

![You Win](/assets/images/you-win.png)
 
 <hr>

__PLAY AGAIN__
- Once the player has either recieved either the game over or you win message the player will be presented with a play again option. 
- This play again  option would be presented below the graphics and will give the player to type "Y" for play again with the previous amount of lives or "N" to be navigated back to the main menu.

![Play Again](/assets/images/play-again.png)
![Play Again-No](/assets/images/play-again-no.png)
 
 <hr>

__INVALID INPUT__
- If the player were to input a value other that a-z the player would be presented with a message indicating them to guess useing any letter form a-z. 
- The message would be, "Sorry that is not a valid inout, please guess a letter from A-Z".
- This would also be the case, the player is instantly allowed to try again using the valid input suggested.

![Invalid Input](/assets/images/invalid-input.png)
![Invalid Input](/assets/images/invalid-input-number.png)
  
 <hr>

### Features Left to Implement
- Features that would be implemented at a later date, would be a player name tracking and score keeping system.
- This would allow the players to become more competitive and add more of a challenge for the game itself. 
- Other features include colours for the texts to give it more of a assteticly pleaseing look.

 
## Testing<hr>
No automated testing has been used for this project, all testing has been conducted manully, with numerous users to validate any findings further. 

  TEST 1🧪 : Loading up game with option 1.
  This was done by simply choosing option 1 and going through the default playing settings, to see if anything may arrise.

  -RESULTS🏆 : The player is able to play using the default settings, all choices from picking a guess to putting in a invalid input to getting a correct and incorrect answer right through to the player winning or losing were bringing back the correct responses. 

  -VERDICT ✅ : The initial gameplay for the option 1 default setting is a pass and completed with no occuring bugs. 

  <hr>

  TEST 2🧪 : Difficulty selection with option 2.
  This was conducted by choosing each difficulty and going through the game, from easy, normal, hard and expert. 

  -RESULTS🏆 : The player is able to choose from the four options of difficulties and play with the game with the given lives. Easy mode had given the correct number of lives 10, Normal mode had given the correct number of lives 7, Hard mode had given the correct number of lives 5 and lastly Expert mode had given the correct number of lives 3.

  With saying this, hangman graphics were also monitored and this also where changing in accordance to the lives amount. 

  -VERDICT✅ : This test has passed successfully with no bugs being presented. 
 
  <hr>

  TEST 3🧪 : Game Rules option 3.
  This was conducted by choosing by choosing the option 3 to display the games rules, and trying to exit the rules page with the advised instructions, which is the press enter.

  -RESULTS🏆 : The player is able to choose option 3 and display the games rules, which displayed correctly, but upon trying to exit this area, pressing enter had displayed the message shown below. This was then looked into further.


  -VERDICT✅ : This test has failed due to the bug that was found when trying to exit the results page. This however was recterfied and solved by placing the correct variable name in, which was tries. After changing this, the game was then tested again and was taking the player back to the game menu as intended.

![Error](/assets/images/error-found.png)


## Unfixed Bugs
- There are currently no unfixed bugs, on this game.
 
 <hr>

### Validator Testing
- PEP8  
 - No errors were returned when passing through the official W3C validator.

[PEP8](http://pep8online.com/)
 
 ![PEP8 Validation](/assets/images/pep8-validation.png)
 
 <hr>

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

 <hr>

## Credits / References<hr>
 
### Content
- To understand the basic structure and layout of the game, which help bring alot of clarity when understanding the logic. [YouTube](https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite)
 
- This was used to bring more understanding to some of the errors found when cleaning up the code. [Flake 8](https://www.flake8rules.com/rules)
 
- The graphics for the title, game over and you win was taken from here. [Patorjk](https://patorjk.com/software/taag/#p=display&v=1&f=Small&t=SAVE%20A%20LIFE%0A%20%20HANGMAN)

- This helped me understand and figure out synatax for python abit better for while loops. [W3SCHOOL](https://www.w3schools.com/python/python_while_loops.asp)

- For the mock terminal to be able to deploy to a live site. [CodeInstitute](https://codeinstitute.net/)

- Richard Wells for his good advice and guidence on breaking things down into manageable portions [RichardWells](https://github.com/D0nni387)
 