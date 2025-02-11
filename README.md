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
  * [Django alert messages](#django-alert-messages)
  *



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
#### img for responsiveness mobile/tablet and laptop
![Amiresponsive](documents/amiresp.png)

#### Mobile navigation using burger menu
![Mobile-nav](documents/mobilenav.png)

![Mobile-nav-signin](documents/signin-mobile.png)

#### Larger screen navigation using burger menu
![Monitor-nav](documents/largescreen.png)

![Large-signin](documents/large-signin.png)



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

### A constant display of the user's login status, showing whether they are logged in or out.
The base HTML checks whether the user is logged in and displays either "You are logged in as [username]" or "You are not logged in," based on the authentication state.

####









