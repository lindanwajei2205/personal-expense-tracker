
#### img for responsiveness mobile/tablet and laptop
![Amiresponsive](documents/amiresp.png)

#### Deployed link 
- [Deployed](https://personal-expense-tracker-ci-e0fff526207f.herokuapp.com/ "link to the deployed site")

# Personal Expense Tracker

The Personal Expense Tracker is a web application designed to help users manage and track their finances with ease. Users can categorise their expenses, and monitor their spending habits. 

With a simple, intuitive interface and graphical representation of your spendings, this app provides valuable insights into personal finances, helping users make informed decisions and take control of their financial future.

## Table of content

- [User experience (UX)](#user-experience-ux)
    * [Key project goals](#key-project-goals)
    * [Target audience](#target-audience)
    * [User requirement and expectations](#user-requirements-and-expectations)



- [Epics and user stories](#epics-and-user-stories)
  * [Epics](#epics)
  * [User stories](#user-stories)

- [Features](#features)
  * [Logo and navbar](#logo-and-navbar)
  * [Clear indication as to whether the user is logged in or out at all times](#clear-indication-as-to-whether-the-user-is-logged-in-or-out-at-all-times)
  * [Django alert messages](#django-alert-messages)
  * [Call to action button](#call-to-action-button)
  * [User dashboard](#user-dashboard)
  * [Landing page](#landing-page)
  * [Sign form](sign-form)
- [Wireframe](#wireframe)
- [Manual testing](#manual-testing)
- [Future features](#future-features)

- [Html and Css Validations](#html-and-css-validations)
- [Python Validations](#python-validations)
- [Database](#database)
- [Deployment steps](#deployment-steps)
- [Technologies and tools](#technologies-and-tools)
- [Credits](#credits)

 

## User experience (UX)

### Key Project goals
- Enable users to record their expenses, and categorise them for easy tracking and analysis.
- Provide graphical representations (pie charts) to help users visualize their spending habits.
- Ensure the app has an intuitive, easy-to-use interface, making financial tracking accessible for everyone, even with no prior experience.
- Build a responsive web application that works seamlessly across all devices
- Create an admin panel to managing expense categories and overall web app

### Target audience
- Users who are interested in tracking their expenses
- Young professionals starting their careers and need help tracking their spending/expenses inorder to safe for the future
- People comfortable with using web applications to track their expenses, and who prefer visual insights (charts, graphs) for better understanding.

### User requirements and expectations
- A web app that works seamlessly across different screen sizes
- An intuitive and easy-to-navigate interface with minimal setup.
- Ability to quickly add items in the categories
- ability to easily Register, log in, and manage their accounts.
- A bility to categorize expenses (e.g., Food, Transportation) for easy tracking
- Ability to add a comment whilst creating items
- Ability to read and have an understanding of what the app does in the about section
- clear and interactive visualizations (like bar or pie charts) of their spending patterns.

## Epics and user stories
### Epics
1. Database and admin set up
2. A fully functional landing page
3. Register/signup form
4. Login page and form
5. Logout page
6. Graphical Representation of expenses in the insight databoard when a category is clicked
7. Previous comments can be seen when adding new comments on expenses.
8. Update, edit and delete expense items 
9. Profile page that contains users details such as username and email address
10. Support Email
11. Social links

### User stories
- As a superuser, I can:
1. perform backend crud operations(part of epic 1)
2. create new Category(part of epic 1)


- As a potential registered user, I can:
3. I can view a clear, concise headline that explains its purpose within the first few seconds of visiting.(part of epic 2)
4. I can view a short introductory section and call-to-action that guides visitors on how to get started or explore the website.(part of epic 2)


- As a website user, I can:
5. Quickly grasp the website's purpose to efficiently navigate and utilize its features.(part of epic 2)
6. Create an account to access the services available to registered members (part of epic 3)
7. Log in to access my account and utilize the full features of the website(part of epic 4)

- As a Logged in web user, I can:
8. Navigate to the 'insight data dashboard' to gain a comprehensive understanding of the app's features and functionality.(part of epic2)
8. Add expense items to the appropriate category(Part of Epic 8)
9. View the graphical representation of my expenses (Part of Epic 6).
10. Edit expense items within the selected category (Part of Epic 8).
11. Add comments(via the insight databoard or comment on expense pgae) to my added or edited items to note important details or reasons for their inclusion or deletion (Part of epic 8)
12. View my profile (part of 9)
13. Log out of the website to securely end my session and protect my account(part of epic 5)

## Features
### Logo and Navbar
The navigation bar and logo are positioned at the top of the page, offering a responsive and user-friendly design. Prioritizing a "mobile-first" approach, the navigation bar features a clickable hamburger icon with a dropdown menu on mobile devices. As the screen size increases (from tablets to laptops and beyond), the hamburger icon disappears, and the navigation bar expands to display options for navigating to different pages, including Registration/Sign Up, Login, and About. Please refer to the screenshots below for visual reference.

#### Mobile navigation using burger menu
![Mobile-nav](documents/mobilenav.png)

![Mobile-nav-signin](documents/signin-mobile.png)

#### Larger screen navigation using burger menu
![Monitor-nav](documents/largescreen.png)

![Large-signin](documents/large-signin.png)

### Clear indication as to whether the user is logged in or out at all times
The base HTML checks whether the user is logged in and displays either "You are logged in as [username]" or "You are not logged in," based on the authentication state.

#### The image below indicates when a user is signed in

![User Signedin](documents/user-signedin.png)

#### The image below indicates when a user is signedout
![User Signedout](documents/user-signedout.png)



### Django alert messages
For every comment, the user is alerted. for example when a comment is added regarding userss' expense items, either via the the insight databoard or via the comment on expenses page, upon successfully  logs in and when user logs out.

#### Django alert message example 1
The first example is an alert that shows "successfully signed in as username" upon sign in.

![Login Alert Message](documents/alerts/django-alert1.png)

#### Django alert message example 2
The second example is an alert that shows 'You have signed out' after the prompt 'Are you sure you want to sign out?'. Once the 'Yes' button is clicked, the alert pops up. See the images below:

![Logout Alert Message](documents/alerts/django-alert2.png)

![Confirm Signout](documents/alerts/confirm-signout.png)

#### Django alert message example 3
The third example is an alert that shows 'Comment added successfully.' This pops up when a user adds a comment and clicks 'Save.' See the image below:

![Comment Alert Message](documents/alerts/django-alert3.png)

### Landing page
This is where users or site visitors are directed when they click the URL/link to the site. It contains a header with the title 'Personal Expense Tracker' and an icon, a sign-in and sign-out navbar, a hero container with the text: 'Ready to track and take full control of your spending? Sign up now and take the first step towards financial management and freedom!' along with a call-to-action button beneath. It also includes brief but detailed information on why to choose our tracker. Additionally, there is a footer containing brief details about the web app, its features, social media icons, and a support email.

![Landing page](documents/Landing-page.png)




### Call to action button
When a visitor accesses the site, a call-to-action button is visible on the landing page. One of the key project goals is to 'build a web app that encourages and directs users to explore the expense tracker.' The button displays the text 'Get Started,' and the user is directed to the sign-in or sign-up page, depending on whether they are an already registered user or a site visitor.

![Call to action button](documents/call-to-action.png)

### User dashboard
Upon successful login, users are directed to the insights dashboard, where they can track and analyse their expenses in an interactive graph and table, view previous comments on their expenses, add comments, and create, read, update/edit, and delete expense items. Users can also view their profile.

#### Insight databoard
This board contains different expense categories, a graphical representation of users' expenses, and a comment box where users can share their thoughts or suggest improvements regarding their spending. see images below:

![Insight databoard](documents/user-dashboard/insight-databoard.png)
![Insight databoard 2](documents/user-dashboard/insight-databoard2.png)

#### Expense items
Here, users can view their already listed expenses with images, they can choose to edit or delete their expenses aswell.
![Expense items](documents/user-dashboard/expense-itemlist.png)

#### Add item
Users can add items, choose the category of the item, add a description, purchase-date, price, quantity and choose to upload image. see below:

![Add item](documents/user-dashboard/add-expenses.png)

#### Comments on expenses
Users can view their previous comments along with the date and time they were created. They can add more comments and select an expense category as well. Once they click 'Save,' the comments are added immediately.

![Comment on expenses](documents/user-dashboard/comments.png)

#### Profile
Users can view their profile. The profile page contains the username, email, and the date they registered.

![Profile](documents/user-dashboard/profile.png)

### Footer
This include a little 'about us' information, features, social media icons and an email for support.

![Footer](documents/user-dashboard/footer.png)

### Sign form

#### Sign in form
This is a straightforward form that prompts for a username and password.
![Signin form](documents/user-dashboard/signin-form.png)

#### Sign up form
This is a simple form to register a new user. It includes fields for the username, email, and password. The password must be entered twice for confirmation, and the form also specifies the requirements for an acceptable password.

![Signup form](documents/user-dashboard/signup-form.png)

#### Sign out 
This page asks users if they are sure they want to sign out. It includes a red logout button underneath, and a button that takes the user back to the insights dashboard if they choose to remain logged in.

![Sign out](documents/user-dashboard/signout-form.png)

### Wireframe 
- Mobile
![Mobile](documents/mobile.jpg)

- Ipad 
![Ipad](documents/ipad.jpg)

- Laptop
![Laptop](documents/laptop.jpg)

### Manual testing

| Feature                    | Tested?  | User Input Required | User Feedback Provided     | Pass/Fail | Fix |
|----------------------------|----------|---------------------|----------------------------|-----------|-----|
| Navbar Logo and Icons | Yes | Click | sign in and sign up takes user to the form to either sign in or register. | Pass | - |
| Features on home page | Yes | click | takes users to the 'Get started' call to action button | Pass | - |
| Sign Up Page               | Yes      | Username/ Email / Password | Empty fields deliver prompt to user, email field demands '@' symbols, password requirements need to be met | Pass | - |
| Sign In | Yes | Username and Password | Username//Password must be exactly as registered originally in either lowercase/uppercase or mixture | Pass | - |
| Home Page Buttons/Get started| Yes | Click | First button goes to sign in or sign up if not registered | Pass | - |
| Social Media Buttons | Yes | Click | Each icon takes you to the relevant social media site. | Pass | - |
| Insight databoard | Yes | click on any categories | Shows the visual anayltics of users' expenses for that category | Pass | - |
| Expense items| Yes | Click on expense items | View users' expense list with options to edit/delete. | Pass | - |
| Add item | Yes | Click on add item | Form contains item name, category,description,date of purchse, price, quantity, upload image option and comment| Pass | - |
| Comment on expenses | Yes | Click  | list of previous comment and a form to add new comment on chosen expense category | Pass | - |
| profile | Yes | click | Users' profile which includes username, email and date registered | Pass | - |
| change email| Yes | option to add/change email| 'part of future feature. | fail | - |
| pie chart | Yes | Press delete button | correlates with the expense item added and updates automatically once new iten is added to a category | Pass |

## Future features
#### Email Verification
Emails can be verified, and upon request, users can change or add their email address to their existing profile.

#### Forget password link
Users who cannot remember their login passwords can click the 'Forgot Password' link and receive an email to set a new password.


## Html and Css Validations
Validations for HTML and CSS 

### Landing pageHtml
![Landing html](documents/html-and-css-validator/landing_page.png)

### Insight datahtml
![Insight html](documents/html-and-css-validator/data-insight.png)

### Add expensehtml
![Add expensehtml](documents/html-and-css-validator/add_expense.png)

### Item  listhtml
![Item listhtml](documents/html-and-css-validator/item_list.png)

### Commentshtml
![Commentshtml](documents/html-and-css-validator/comment.png)

### Edit expense
![Editexpense html](documents/html-and-css-validator/edit_expense.png)

### Logout
![Logout](documents/html-and-css-validator/logout.png)

### Signin validation
![Signin html](documents/html-and-css-validator/sign_in.png)

### Signup validation
![Signup html](documents/html-and-css-validator/signup.png)

### CSS
![Css](documents/html-and-css-validator/css-stylesheet.png)

### JS validattion
![Javascript](documents/Js-validation.png)

## Python Validations
Python validations for the below;

### Category model
![Category model](documents/python-validator/category-model.png)

### Category view
![Category view](documents/python-validator/category-view.png)

### Comment form
![Comment form](documents/python-validator/comment-form.png)

### Comment view
![Comment view](documents/python-validator/comment-view.png)

### Insight view
![Insight view](documents/python-validator/insight-view.png)

### Item form
![Item form](documents/python-validator/item-form.png)

### Item modal
![Item modal](documents/python-validator/item-model.png)

### Item view
![Item view](documents/python-validator/item-view.png)

## Lighthouse 
Perf
![Lighthouse](documents/lighthouse/1.png)
![Lighthouse2](documents/lighthouse/2.png)

## Entity realtionship diagram
![ERD](documents/ERD.png)

### Database

- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) was used as the PostgreSQL database for this project

## Deployment steps

The site was deployed to Heroku. The steps to deploy are as follows:
- Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
- In the Procfile write 'web: gunicorn expensetracker.wsgi'
- In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
- In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list
- git add, commit and push to github
- Navigate to the Heroku dashboard
- Create a new Heroku app
- Give it a name and select the region 'Europe'
- Navigate to settings tab and scroll down to Config Vars
- Click 'Reveal Config Vars'
- Add the following keys:
    - key = DATABASE_URL | value = (my secret database url)
    - key = SECRET_KEY | value = (my secret key)
- Navigate to Deploy tab
- Connect to GitHub and select the repo 'lunar-lists'
- Scroll down to 'Manual deploy' and select the 'main' branch

## Technologies and tools

- [VS Code](https://code.visualstudio.com/ "link to visual studio code webpage") was used as the ide for this whole project
- [Cloudinary](https://cloudinary.com/ "link to cloudinary homepage") was used to host images
- [GitHub](https://github.com/ "link to github webpage") was used to store the code files, README files and assets
- [Git](https://git-scm.com/ "link to official git website") was used as a version control software to commit and push the code to the GitHub repository
- [Heroku](https://id.heroku.com/login "link to Heroku login") was used for deployment
- [dbeaver](https://dbeaver.io/ "link to dbeaver") was used to make a diagram of the database schema.
- [Prettier](https://prettier.io/ "link to official prettier website") was used as the default formatter in Visual Studio Code IDE, for html and css files.
- [Bootstrap](https://getbootstrap.com/ "link to official bootstrap website") was used to quickly layout, position and size critical website features
- [Balsamiq](https://balsamiq.com/wireframes/ "link to official balsamiq website") was used in early planning to create wireframes
- [Google Fonts](https://fonts.google.com/ "link to official google fonts website") was used to import fonts
- [Favicon Generator](https://favicon.io/favicon-generator/ "link to official favicon generator website") was used to make a favicon
- [Font Awesome](https://fontawesome.com/ "link to official font awesome website") was used for all icons
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/ "Link to official chrome developer tools website") was used for lighthouse testing, debugging and consistently checking responsiveness
- [W3C Markup Validator](https://validator.w3.org/ "link to official html validator") was used to validate all live html
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/ "link to official css validator") was used to validate CSS code
- [JS Hint](https://jshint.com/ "link to official javascript validator") was used to validate JavaScript code
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/ "link to official python validator") was used to validate all python code
- [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/ "link to official crispy forms website") were used throughout the project to quickly create forms
- [Chat-GPT](https://chat.openai.com/ "link to chat gpt")  used to create the text content.
- [Deep-seek](https://www.deepseek.com/ "link to deepseek") used to create the text content aswell.

## Credits

- [Code Institute](https://learn.codeinstitute.net/dashboard/ "link to Code Institute LMS") Code Institute walkthroughs

- [Google chrome](https://www.google.com/chrome/ "link to google chrome") to generate item images
- [Youtube](https://www.youtube.com/ "link to youtube")

- [Facebook](https://www.facebook.com/ "link to facebook") social media icon link
- [X](https://www.X.com/ "link to X") social media icon link
- [instagram](https://www.instagram.com/ "link to instagram") social media icon link
- [Chat-GPT](https://chat.openai.com/ "link to chat gpt")  used to create the text content.
- [Deep-seek](https://www.deepseek.com/ "link to deepseek") used to create the text content aswell.





















