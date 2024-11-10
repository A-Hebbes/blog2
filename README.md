# Book Blog

![Book Blog Image](readme/assets/images/book-blog-responsive.png)

[Book Blog] (https://blog2-8708e1fd0f42.herokuapp.com/) is a site to share book reviews. The site allows users to read about books and to engage in the conversation. 

## Table of contents

* [Purpose](#purpose)
* [UX Design](#ux-design)
* [Wireframes](#wireframes)
* [Design](#design)
* [Features](#features)
* [Data Model](#data-model)
* [Testing](#testing)
* [Technologies](#technologies)
* [Deployment](#deployment)
* [Credits](#credits)

# Purpose
The purpse of Book Blog is to share my passion for literature and reading. The site aims to provide honest, insightful reviews of books so that others can make more informed choices of the books they wish to read. It is also an opportunity to build a community around reading, with users being able to comment on reviews. 

# Agile Development

This project was completed using agile methodologies and a process of iterative development. I used a Kanban board to manage and track user stories and tasks. This allowed flexibility and continuous improvement throughout the project.

Key aspects of the agile methodology used:

- User Stories: These stories were established at the outset of teh project to guide the development process. 
- Kanban Board: This was used to visualise the project workflow and track progress. 
- Continuous commits: I regularly commited the code to GitHub to keep a track of progress and ensure up to date code.

![Kanban 1](/readme/assets/images/book-blog-kanban-1.png)
![Kanban 2](/readme/assets/images/book-blog-kanban-2.png)

# UX Design
## User Stories

As a user:
1. I can view an organised list of previous posts so that I can select and view relevant posts.

   Acceptance Criteria:
   - With multiple posts in the database, the posts will be listed.
   - A list of previous posts is easily visible when the main page is opened.
   - Pagination allows the user to select what they wish to read.

As an admin:
2. I am able to draft posts and then finish them later.

   Acceptance Criteria:
   - Logged in users are able to save draft blog posts.
   - Saved posts can be finished at a later time.

As a site user or admin:
3. I can review comments associated with individual posts to engage in the conversation.

   Acceptance Criteria:
   - Admins can access and review user comments.
   - Site users can navigate to the comment thread to participate in the discussion.

As a site user:
4. I can contribute to the conversation by leaving comments on posts.

   Acceptance Criteria:
   - User comments are approved or disapproved.
   - Once approved, a comment can be replied to.
   - In the case of more than one reply, there will be a conversation function.


As a site user:
5. I can delete or modify my comments on posts.

   Acceptance Criteria:
   - Logged in users can edit their comments.
   - Logged in users can delete their comments.

As a site user:
6. I can register an account to enable commenting on posts.

   Acceptance Criteria:
   - Users can register an account using their email.
   - Users are able to log in.
   - Logged in users are able to leave comments.

As a site admin:
7. I can perform CRUD operations on posts to effectively manage blog content.

   Acceptance Criteria:
   - Site admin can create a new blog post.
   - Site admin can view blog posts.
   - Site admin can update existing blog posts.
   - Site admin can delete blog posts.

As a Site User:
8. I can access the full text of a post by clicking on its title.

   Acceptance Criteria:
   - Upon clicking on a blog post title, the user is presented with a detailed view of the post.

As a site user:
9. I can see what reviews are to be released so that I can know if anything of interest is coming to the site soon.

   Acceptance Criteria:
   - Users can view basic details of blog posts which are currently set as drafts.


## Structure

### Home Page
![Home Page](/readme/assets/images/book-blog-home.png)
- The home page displays the site's name and provides a paginated list of blog posts displaying the blog title and creation information. 
    #### User Goal:
    >   - To quickly see a range of posts that can be navigated to easily. 
    >   - To see a navigation menu which can direct to other areas of the site. 
    >   - To be able to click on relevant areas and be accurately taken to where I intend.
    
    #### Website Goal:
    >   - To give users a clear communication of the site's layout. 
    >   - To provide the user key information to use the site effectively. 

### Full Post Page
![Full Post](/readme/assets/images/book-blog-full-post.png)
- This is the page in which readers can view a post and, if logged in, can comment on the post. 
    #### User Goal:
    >   - To read a blog post about a book I may be interested in. 
    >   - If I am logged in, to comment on the posts and provide my input to the conversation. 
    #### Website Goal:
    >   - To clearly display the blog article.
    >   - To give the user the opportunity to comment on posts if they are logged in. 

### Upcoming Post Page
![Upcoming Posts](/readme/assets/images/book-blog-upcoming-post.png)
- This page allows to see a list of upcoming posts. 
    #### User Goal:
    >   - To see what future posts are planned so that I can be aware of anything of interest that is upcoming. 
   
    #### Website Goal:
    >   - To display only the basic information of draft posts so that users can be informed of what is comming up. 

### Sign-in / Sign-up Pages
![Sign In](/readme/assets/images/book-blog-sign-in.png)
- This page provides the ability for site administration.
    #### User Goal:
    >   - To manage users, posts, and comments.
    >   - To moderate content and control site settings.
   
    #### Website Goal:
    >   - To ensure site access for users and quality content.
    >   - To give admins control over the blog.

### 7. Admin Page
![Admin Page](/readme/assets/images/book-blog-admin.png)
- Gives easy to use site administration
- Allows for management of users, posts, and comments
- Enables easy content moderation and site configuration
- Offers detailed views and filtering options for all models 


# Wireframes
![Wireframe Home](/readme/assets/images/book-blog-wireframe-home.png)
![Wireframe Full Post Page](/readme/assets/images/book-blog-wireframe-full-post.png)
![Wireframe Upcoming Post](/readme/assets/images/book-blog-wireframe-upcoming-post.png)


# Design
The design used muted green shades, this aimed to provide a calm environment such as one that would be conducive for reading.
[Coolors] (https://coolors.co/) was used to find a good colour palette. 

![Colour Palette](/readme/assets/images/book-blog-colour-palette.png)


# Features

## Existing Features

### 1. Blog Post List
- Displays an organized list of blog posts
- Includes pagination for easy navigation

### 2. Full Blog Post View
- Shows full content of a post when title is clicked

### 3. Comments System
- Users can view comments on posts
- Registered users can leave comments
- Users can edit and delete their own comments
- Comments require approval before being displayed

### 4. User Authentication
- User registration functionality
- User login/logout

### 5. Admin Features
- CRUD operations for blog posts
- Ability to save drafts and publish later
- Comment moderation ability

### 6. Upcoming Posts Preview
- Shows a list of upcoming blog posts which are currently in draft


## Future Features

- Category/tag filtering for posts
  - Allows users to find posts related to specific genres/topics.

- User ratings for books
  - Users could rate books on a scale, this will help increase engagemnet and allow other users to get an idea of how popular a book is.

- Newsletter signup
  - Users will be able to subscribe to a newsletter.

- Enhanced user profiles
  - Users could have profiles and the ability to connect with other users. This will allow for users to contact each other about books that have been reviewed and others which also may be of interest.

# Data Model

This project used a relational database model. The main models are: User, Post, and, Comment. Below is an overview of the data model.

![ERDs](/readme/assets/images/book-blog-ERD.png)

## User Model
The User model is from Django's built-in authentication system. It is used to store user information and is a foreign key in other models.

## Post Model
The Post model represents blog posts and contains:
- Title (CharField)
- Slug (SlugField)
- Author (ForeignKey to User)
- Content (TextField)
- Created On (DateTimeField)
- Status (IntegerField)

## Comment Model
The Comment model is used to represent user comments on posts:
- Post (ForeignKey to Post)
- Author (ForeignKey to User)
- Body (TextField)
- Approved (BooleanField)
- Created (DateTimeField)

## Relationships
- A User can create multiple Posts (One-to-Many)
- A Post can have multiple Comments (One-to-Many)
- A User can write multiple Comments (One-to-Many)


# Testing

## Manual Testing

### User Interface Elements

#### Navigation Bar
1. Home Link
- Expected: Clicking "Home" navigates to homepage
- Testing: Clicked home link from various pages
- Result: Successfully redirected to homepage
- Fix: No fixes needed

2. Responsive Menu (Mobile)
- Expected: Menu collapses into hamburger on mobile screens
- Testing: Tested on various screen sizes under 768px
- Result: Menu correctly collapses and expands
- Fix: No fixes needed

#### Authentication Features

1. Login Form
- Expected: Users can login with valid credentials
- Testing: Tested with:
 - Valid username/password
 - Invalid username
 - Invalid password
 - Empty fields
- Result: 
 - Valid credentials: Successfully logged in
 - Invalid/empty fields: Appropriate error messages shown
- Fix: No fixes needed

2. Registration Form
- Expected: New users can create accounts with valid details
- Testing: Tested with:
 - Valid information
 - Existing username
 - Non-matching passwords
 - Invalid email format
- Result: Form validation works correctly
- Fix: No fixes needed

#### Blog Features

1. Comment Submission
- Expected: Logged-in users can post comments on blog posts
- Testing: Tested:
 - Submitting valid comment
 - Submitting empty comment
 - Submitting as logged-out user
- Result: 
 - Valid comments posted successfully
 - Empty comments rejected with error message
 - Logged-out users redirected to login
- Fix: No fixes needed

2. Edit Comment Button
- Expected: Users can edit their own comments only
- Testing: Tested editing:
 - Own comment
 - Another user's comment
 - As admin user
- Result: Edit button only appears for own comments and admin
- Fix: No fixes needed

### Responsiveness Testing

Tested on following devices/screen sizes:
1. Desktop (1920x1080)
- Expected: Full layout with sidebar visible
- Testing: Checked all pages and features
- Result: Layout renders correctly
- Fix: No fixes needed

2. Tablet (768px)
- Expected: Responsive layout with collapsed menu
- Testing: Tested navigation and content flow
- Result: Some content overflow on blog posts
- Fix: Added media query to adjust padding on blog containers

3. Mobile (320px)
- Expected: Single column layout, stacked elements
- Testing: Checked all interactive elements
- Result: All elements accessible and functional
- Fix: No fixes needed

## Automated Testing

Automated tests were used to ensure reliability and functionality of key parts of the project. Two test files were created:

### 1. Blog Views Tests (`test_views.py`)

This file holds tests for the blog views:

- `setUp`: Creates a test superuser and a test blog post.
- `test_post_full_with_comment_form`: 
  - Checks if blog post_full view loads as expected.
  - It verifies that post content is displayed.
  - It also ensures that a comment form is on the page.
- `test_successful_comment_submission`:
  - Tests the comment submission users who are logged-in.
  - Checks for a success message after comment submission.

[Views Unit Tests Screenshot](readme/assets/images/views_unit-test.png)
  

### 2. Comment Form Tests (`test_forms.py`)

This file focuses on testing the comment form validation:

- `test_valid_comment_submission`: Makes sure that comments are accepted if they are valid.
- `test_empty_comment_rejection`: Tests to check that empty comments do not get published and that error message shows. 

![Unit Tests Screenshot](readme/assets/images/unit-tests.png)

### Running the Tests

The following command was used to run the tests in the terminal: python manage.py test


## Code Validation

   - Flake8 was used to check python code of the project. 
   - [JSHint] (https://jshint.com/) was used to check the JavaScript File. There were no issues raised that required changing.
   - [W3C Validation](https://validator.w3.org/) was used to validate the HTML. Minor issues like unclosed divs and extra spaces in 
      closing tags were fixed. Remaining warnings were related to the use of Django template tags.
   - [W3C CSS Jigsaw](https://jigsaw.w3.org/css-validator/) was used to validate the CSS. No errors were found in the CSS code.

## Lighthouse

There were considerable issues flagged by Lighthouse when the test was run locally. It was not clear to me why these issues were being flagged and the reports I could find seemed to find issues with files that I had not created e.g. bootstrap.css. After attempting to find fixes for the issues and not making progress. I contacted Code Institute tutors for advice. When Lighthouse was run by the tutor, it returned with a far more favourable review of the site. I am still unclear as to why the test was failing locally, other than that it is perhaps that the internet connection where I am presently is unstable. Below are images of the test which I ran locally (white backgorund) and the tutor's screen shot (black background). I hope that this will suffice in this area of the project write up. 

![Local Lighthouse](/readme/assets/images/book-blog-lighthouse-own.png)
![Tutor's Lighthouse](/readme/assets/images/book-blog-tutor-lighthouse.png)

# Technologies
## Languages
- HTML
- CSS
- JavaScript
- Python
- Django Template Language
- SQL

## Frameworks, Libraries & Programs
- Django: The main Python web framework used for the project
- Bootstrap: For responsive front-end design
- Git: For version control
- GitHub: To store the repository
- Heroku: For deploying the live site 
- Gunicorn: To run Django on Heroku
- PostgreSQL: Database 
- SQLite: Local development database when main server was down
- Django Allauth: For user authentication, registration, and account management 
- Django Crispy Forms: For styling Django forms 
- Summernote: For text editing in the admin panel 
- Font Awesome: For icons 
- Google Fonts: For custom typography 
- jQuery: 
- Whitenoise: For serving static files 
- Balsamiq: For creating wireframes


# Deployment

This project was deployed on Heroku using Code Institute's PostgreSQL server. See below for deployment steps:

### Prerequisites

- Python
- Django
- Bootstrap
- Heroku account
- Code Institute PostgreSQL server access

### Database Setup

The database uses the Code Institute server follow the Code Institute guidelines to setup this server. 

### Deployment Process

1. Log in to your Heroku account.
2. On Heroku create a new app.
3. In Heroku app settings add the required environment variables. 
4. Connect the GitHub repository to the Heroku app.
6. The project can be deployed manually or automatically from Heroku. 

### Important Notes

- Ensure `DEBUG` is set to `False` before deployment on Heroku.
- Include the Heroku app in the `ALLOWED_HOSTS` in settings.py.


# Credits

## Code Institute Walkthrough

The code institute project walkthrough 'I Think Therefore I Blog' formed the basis for this project. I used it to guide me through the steps of development and to inform my use of Django and Bootstrap in particular. 

## Course Leader

Laura, my cohort facilitator was a great source of ecouragement and guidance on this project. 

## Tutor Assistance

The Code Institute tutors were also very helpful at a couple of points with this project. Their guidance helped to solve a couple of issues I was having. The guidance and time was very much appreciated.

## AI Assistance
ChatGPT and Claude AI were used to help provide guidance in a number of project areas. In the early stages they were used to develop the blog content, this allowed for the site to be populated with meaningful content whilst also allowing me time to focus on the main job of working on the project. I also used the AI tools mentioned to help provide guidance for debugging when things went wrong. As a novice, I often find that I struggle to know where to begin when a problem occurs. Using the AI tools as a kind of tutor helped to shed light on where issues may have occured.  

## Ollie Grubb
Ollie Grubb gave effective and informative advice on the use of databases. He helped in particular to outline the function of ERDs and how these are useful in the development process. 

## Other Sources of Guidance

The below were used at various points of the project to help guide the development: 

- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)

## Media

The image of a library was found on [Unsplash](https://unsplash.com/) and was taken by photographer, Janko Ferlic.

