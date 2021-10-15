# Funny Bones

![Funny Bones Mockup Images](readme-files/responsive-site.PNG)

[View the live project here](https://github.com/Irishbecky91/Funny_Bones)

## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
    1. [Main Languages Used](#Main-Languages-Used)
    3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
    1. [Testing User Stories](#Testing-User-Stories)
    2. [Manual Testing](#Manual-Testing)
    3. [Automated Testing](#Automated-Testing) 
        - [Code Validation](#Code-Validation)
        - [Browser Validation](#Browser-Validation)
    4. [User Testing](#User-Testing)
7. [Deployment](#Deployment)
    1. [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
8. [Credits](#Credits)
    1. [Content](#Content)
    2. [Media](#Media)
    3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***


## Introduction

For the Portfolio Project 3 - Python Essentials, the developer decided to build a hangman type game. Instead of a hanged man being drawn, a Halloween themed skeleton, "Funny Bones", is created when incorrect words or letters are input.

The main requirements of this project are to build a command-line application that allows the user to manage a common dataset about a particular domain.

[Back to top ⇧](#)



## UX
### Ideal User Demographic
The ideal user for this website is:
* New user
* Current user

#### New User Goals
1. As a new user, I want to see clear instructions for gameplay. 
2. As a new user, I want to see a visual representation of my remaining lives.
3. As a new user, I want the ability to replay the game.

#### Current User
1. As a current user, I want the ability to replay the game.
2. As a current user, I want the guess word to follow a certain theme.
3. As a current user, I want the choice to use different themes. 


### Development-Planes
To create a command-line application that allows the user to play a word guess game, "Funny Bones".


#### Strategy
Strategy incorporates user needs as well as product objectives. This website will focus on the following target audience, divided into three main categories:
- **Roles:**
    - New users
    - Current users

- **Demographic:**
    - All ages
    - All puzzle playing levels

- **Psychographic:**
    - Lifestyles:
        - Interest in games
        - Interest in Halloween
        - Interest in puzzles
    - Personality/Attitudes:
        - Focused
        - Forward-Thinking
        - Creative
    
The application needs to enable the **user** to:
- play the game "Funny Bones" using only alpha characters.
- generate a new word on each play-through by sourcing a random word from an external list of words.
    
With the above information in mind, a strategy table was created to show the trade-offs between what is important and what is viable with the following results.

<details>
<summary>Strategy Plane - Viability/Feasibility Table</summary>

![Strategy Table](readme_files/flowcharts_and_tables/strategy_table.PNG)

</details>


#### Scope
The scope plane is about defining requirements based on the goals established on the strategy plane. Using the information in the strategy plane, the identified required features have been broken into the following two categories.
- Content Requirements:
    - The user will be looking for:
        - Clear and concise instructions.
        - A consistent theme, such as Halloween 
- Functionality Requirements:
    - The user will be able to:
        - Enter either a letter or a whole word if they think they know it.
        - Replay the game.
        - End the program at the end of the game.


#### Structure
The project will be deployed to a Heroku terminal. There will be no styling aside from the image of Funny Bones built using special characters within the terminal. 


#### Skeleton
A flowchart was created to show the logic the functions would follow. This flowchart was created using the flowcharts template on [Lucid](https://lucid.app/).


<details>
<summary>Lucid Flowchart</summary>
    
![Lucid Flowchart](readme_files/flowcharts_and_tables/flowchart.png)

</details>


### Design
#### Imagery
The imagery used in the game is a skeleton named Funny Bones. The image is made using only special and alpha characters. This image was chosen to match the Halloween theme chosen for the game. The initial image was of a skeleton stood upright which turned out to be too long for the terminal window. This was substituted for a crouching skeleton, making the appearance more intimidating also.

[Back to top ⇧](#)


## Features
### Existing Features
- **Input Bar** - In order to progress the game, the user will use the input bar to input their next guess, either a letter or word.
- **Replay Choice** - At the end of each game, win or lose, the user will be offered the choice to play again by entering either Y (yes) or any other character to end the game.
- **Visual Representation of Lives Remaining** - Each time the user enters an incorrect guess, a section of Funny Bones the skeleton will appear. When Funny Bones is completed, the game is lost.
- **Instructions and Introduction** - At the beginning of each game, a brief introduction to Funny Bones and the instructions is shown, telling the user how to play the game.

### Features to Implement in the future
- **Additional Themes**
     - **Feature** - A set of additional themes will be available to the user to play.
     - **Reason for not featuring in this release** - A lack of experience and time prevented the developer from making this feature upon release. This feature will be developed and implemented in the future to improve repeat play by users.

[Back to top ⇧](#)


<!--
## Issues and Bugs 
The developer ran into several issues during the development of the website, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.

**Grid Difficulty Bug** - A bug was detected early in development as the numbers on the grid did not change when other difficulties were selected. It was found the developer had used .click instead of .checked when coding the event handler. Once changed, the problem was resolved.

**Square Selection Bug** - A bug was detected where an empty square, when clicked on, did not register the click. The cause of this was found to be a mislabelling of an element. Instead of a "p" element, the selected class in CSS should have been a "div element. Once this and the square's element was changed to a div, the problem was resolved.

**Number Transfer Bug** - A bug was detected which affected the squares, causing the number chosen in the number selector to not transfer to the selected square. The problem was the variable selected on line 232 was incorrect, selectedNumber was used instead of selectedSquare. Once this was replaced for the correct variable, the issue was resolved.

**Game Won Early Bug** - A bug was detected when playing the game as the game would complete a win sequence early if the first available square was filled in before any others. The problem was the function checkGridComplete was only checking to see if the first square in the grid was filled correctly. This required a complete reworking of the function, creating an empty array to check for and store empty squares. Once the array is emptied, the game is won. This was the final bug which has now been rectified.

[Back to top ⇧](#)



## Technologies Used
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")

### Frameworks, Libraries & Programs Used
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts was used to import the fonts "Special Elite", "Open Sans", "Oswald" and "Nosifer" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on almost all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
     - GitPod was used for writing code, committing, and then pushing to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Balsamiq](https://balsamiq.com/ "Link to Balsamiq homepage")
     - Balsamiq was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.

[Back to top ⇧](#)



## Testing
### Testing User Stories

#### Current User Goals:

#### New User Goals:
1. As a new user, I want to easily navigate the site intuitively. 
  - The navigation bar brings users to each of the three site pages. It is clearly laid out with easy to read buttons.
  
2. As a new user, I want the instructions to be easily found, clear and concise.
  - The rules of Sudoku are clearly laid out on the instructions/rules page. 
  - The key points of the rules are displayed using bullet points.

3. As a new user, I want attractive and relevant visuals and colour schemes that work with the content.
  - There is a relaxed neutral colour scheme across the site.
  - The user has a choice of theme when starting a new game. 
  - The theme choices change the colours of the header, footer and body of the page, depending on the selected theme.

#### Current User
1. As a current user, I want to have a variety of difficulty options, to challenge myself.
  - There are four available difficulties for the user to choose from, easy, medium, hard and hardcore.
  - There are four premade puzzle layouts that change according to the users chosen difficulties.

2. As a current user, I want to have an option of a timed game.
  - There are three available timer options for the user to choose from, 3 minutes, 5 minutes and 10 minutes
  - The chosen timer begins as soon as the user hits the Start New Game button and counts back from the chosen time frame.

3. As a current user, I want to see randomly generated puzzle boards for each difficulty level.
  - Unfortunately, this feature was not able to be implemented at this stage. 
  - As an alternative, a premade puzzle layout was made for each of the four difficulty selections.

[Back to top ⇧](#)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Hovering over the Navigation bar elements will trigger the `hover` effect, highlighting the icon for the user.

<details>
<summary>Navbar hover effect</summary>

![Navbar hover effect](assets/testing-files/navbar-hover.gif)

</details>
     
- Clicking on the Navigation Bar's links will bring the user to the specified page.

<details>
<summary>Navbar page links</summary>

![Navbar page links](assets/testing-files/navbar-function.gif)

</details>
     
- Clicking on the Social Media links will open a new tab

  LinkedIn:

<details>
<summary>LinkedIn Social Media link</summary>

![LinkedIn Social Media link](assets/testing-files/linkedin.gif)

</details>
     
  GitHub:

<details>
<summary>GitHub Social Media link</summary>

![GitHub Social Media link](assets/testing-files/github.gif)

</details>
     
### Game Page
Manual testing was conducted on the following elements of the [Game Page](https://irishbecky91.github.io/Do-you-Sudoku/game.html):

- Clicking the Start New Game button will create a new grid using the user's chosen settings.

<details>
<summary>Start New Game Button - Game Page</summary>

![Start New Game Button - Game Page](assets/testing-files/start-btn.gif)

</details>

- Selecting the different difficulties changes the layout of the grid.

<details>
<summary>Difficulty Grid Layouts - Game Page</summary>

![Difficulty Grid Layouts - Game Page](assets/testing-files/grid-layout.gif)

</details>
     
- Selecting the different time settings will change the length of the timer.

<details>
<summary>Timer Settings - Game Page</summary>

![Timer Settings - Game Page](assets/testing-files/timer.gif)

</details>
     
- Selecting a square in the grid and a number in the number selector moves that number to the chosen square.

<details>
<summary>Assign Number To Square - Game Page</summary>

![Assign Number To Square - Game Page](assets/testing-files/assign-number.gif)

</details>
     
- When an incorrect number is assigned to a box, the user loses a life.

<details>
<summary>Lose A Life - Game Page</summary>

![Lose A Life - Game Page](assets/testing-files/lives.gif)

</details>

- Show the win and lose messages when the game ends.

<details>
<summary>Game Over - Game Page</summary>

![Game Over - Game Page](assets/testing-files/game-over.gif)

</details>
     
### Responsiveness
Manual testing was conducted on all three site pages for responsiveness:

- Responsivenss of Home Page.

<details>
<summary>Resposiveness - Home Page</summary>

![Resposiveness - Home Page](assets/testing-files/responsive-home.gif)

</details>
     
- Responsivenss of Instructions/Rules Page.

<details>
<summary>Resposiveness - Rules Page</summary>

![Resposiveness - Rules Page](assets/testing-files/responsive-rules.gif)

</details>

- Responsivenss of Game Page.

<details>
<summary>Resposiveness - Game Page</summary>

![Resposiveness - Game Page](assets/testing-files/responsive-game.gif)

</details>
     
[Back to top ⇧](#)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML` and `CSS` code used. The [JSHint JavaScript Code Quality Tool](https://jshint.com/) was also used to validate the sites `JS` code.

**Results:**

- Home Page

<details>
<summary>Home Page HTML Validation Results</summary>

![Home Page HTML Validation Results](assets/testing-files/validate-html-home.gif)

</details>

- Rules Page

<details>
<summary>Rules Page HTML Validation Results</summary>

![Rules Page HTML Validation Results](assets/testing-files/validate-html-rules.gif)

</details>

- Game Page

<details>
<summary>Game Page HTML Validation Results</summary>

![Game Page HTML Validation Results](assets/testing-files/validate/validate-html-game.gif)

</details>

- CSS stylesheet

<details>
<summary>Style sheet Validation results</summary>

![Style sheet Validation results](assets/testing-files/validate-css.gif)

</details>

- JavaScript 

<details>
<summary>JavaScript Validation results</summary>

![JavaScript Validation results](assets/testing-files/validate-js.gif)

</details>

### Browser Validation
- Chrome - [Chrome test image](assets/testing-files/validate-chrome.PNG)
- Edge - [Edge test image](assets/testing-files/validate-edge.PNG)
- Opera - [Opera test image](assets/testing-files/validate-opera.PNG)
- Firefox - [Firefox test image](assets/testing-files/validate-firefox.PNG)

## User testing 
My husband and the lovely people of Slack were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes to create a better experience. 

## Deployment

This project was developed using [GitPod](https://www.gitpod.io/ "Link to GitPod site"), which was then committed and pushed to GitHub using the GitPod terminal.

### Deploying on GitHub Pages
To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/Irishbecky91/Do-you-Sudoku "Link to GitHub Repo").
3. At the top of the repository, select Settings from the menu items.
4. Scroll down the Settings page to the "Pages" section.
5. Under "Source" click the drop-down menu labelled "None" and select "Main".
6. Upon selection, the page will automatically refresh meaning that the website is now deployed.
7. Scroll back down to the "Pages" section to retrieve the deployed link.
    

    
## Credits 

### Content
- Some of the Home Page text was borrowed from an entry on [Britannica's Website](https://www.britannica.com/topic/sudoku "Link to Britannica's page on Sudoku").

### Media
- The image of Maki Kaji was borrowed from [The Sydney Morning Herald](https://www.smh.com.au/world/asia/sudoku-creator-maki-kaji-who-saw-life-s-joy-in-puzzles-dies-20210818-p58jrt.html "Link to The Sydney Morning Herald's article - Sudoku creator Maki Kaji, who saw life’s joy in puzzles, dies").

### Code 
The developer consulted multiple sites to better understand the code they were trying to implement. The following sites were used on a more regular basis:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")

[Back to top ⇧](#)

## Acknowledgements

- I would like to thank my family for their valued opinions and critic during the process of design and development.
- I would like to thank my tutor, Kasia, and my mentor, Seun, for their invaluable help and guidance throughout the process.
- I would like to thank the kind and patient tutors of the tutor support system who helped when I was struggling with a piece of code, specifically John and Sheryl.
- Lastly, I would like to extend my deepest gratitude to the amazing people in Slack who helped me rigorously test every aspect of my site.

[Back to top ⇧](#) -->