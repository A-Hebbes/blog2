# Book Blog

![Book Blog Image](/readme/assets/book-blog-responsive.png)

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
![Home Page](/readme/assets/book-blog-home.png)
- The home page displays the site's name and provides a paginated list of blog posts displaying the blog title and creation information. 
    #### User Goal:
    >   - To quickly see a range of posts that can be navigated to easily. 
    >   - To see a navigation menu which can direct to other areas of the site. 
    >   - To be able to click on relevant areas and be accurately taken to where I intend.
    
    #### Website Goal:
    >   - To give users a clear communication of the site's layout. 
    >   - To provide the user key information to use the site effectively. 

### Full Post Page
![Full Post](/readme/assets/book-blog-full-post.png)
- This is the page in which readers can view a post and, if logged in, can comment on the post. 
    #### User Goal:
    >   - To read a blog post about a book I may be interested in. 
    >   - If I am logged in, to comment on the posts and provide my input to the conversation. 
    #### Website Goal:
    >   - To clearly display the blog article.
    >   - To give the user the opportunity to comment on posts if they are logged in. 

### Upcoming Post Page
![Upcoming Posts](/readme/assets/book-blog-upcoming-post.png)
- This page allows to see a list of upcoming posts. 
    #### User Goal:
    >   - To see what future posts are planned so that I can be aware of anything of interest that is upcoming. 
   
    #### Website Goal:
    >   - To display only the basic information of draft posts so that users can be informed of what is comming up. 

### Sign-in / Sign-up Pages
![Sign In](/readme/assets/book-blog-sign-in.png)
- These pages allow the user to sign in and sign up.  
    #### User Goal:
    >   - To be able to gain additional priviliges on the site and be able to engage in the community.  
   
    #### Website Goal:
    >   - To increase opportunity for user engagement whilst also maintaining control of the site's use.  


# Wireframes
![Wireframe Home](/readme/assets/book-blog-wireframe-home.png)
![Wireframe Full Post Page](/readme/assets/book-blog-wireframe-full-post.png)
![Wireframe Upcoming Post](/readme/assets/book-blog-wireframe-upcoming-post.png)


# Design
The design used muted green shades, this aimed to provide a calm environment such as one that would be conducive for reading.
[Coolors] (https://coolors.co/) was used to find a good colour palette. 

![Colour Palette](/readme/assets/book-blog-colour-palette.png)


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

This project used a relational database model. The main models are: User, Post, and, Comment. Here's an overview of the data model:

![ERD Place Holder](/readme/assets/book-blog-ERD.png)

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

As well as automated tests, manual testing was carried out. The following areas were manually tested:

### User Interface and Responsiveness
- Tested the website on different screen sizes to ensure responsive design.
- Verified that Bootstrap components render and work as expected.
- Checked for layout issues or overlapping elements.

### Navigation
- Tested the navigation links to ensure they go to the correct pages.
- Ensured that the active page is correctly highlighted in the navigation menu.
- Tested dropdown menu on smaller screens.

### Forms
- Tested forms to ensure expected results.
- Checked form validation works correctly.
- Verified that success and error messages are displayed when needed.

### CRUD Functionality
- Tested creating new posts / comments.
- Verified that posts and comments can be read.
- Tested editing comments to update them.
- Confirmed that comments can be deleted successfully.

### User Authentication
- Tested user registration process to ensure it works as expected.
- Checked that comment function is only available to logged-in users.

### Cross-browser Testing
- Checked that the website works as expected on different browsers.
- The website was tested on Safari, Chrome, and Explorer.

No major issues were found during manual testing. Minor adjustments were made based on observations during testing.


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

### 2. Comment Form Tests (`test_forms.py`)

This file focuses on testing the comment form validation:

- `test_valid_comment_submission`: Makes sure that comments are accepted if they are valid.
- `test_empty_comment_rejection`: Tests to check that empty comments do not get published and that error message shows. 

### Running the Tests

The following command was used to run the tests in the terminal: python manage.py test


## Code Validation
Add results here

# Technologies
## Languages
List of langs

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
Need to look into what is included here. 

# Credits
Code institute walkthoriugh, course leader, tutor assistance, chat gpt/Claude, Ollie Grubb. 