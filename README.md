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
![](image_placeholder)
- The home page displays the site's name and provides a paginated list of blog posts displaying the blog title and creation information. 
    #### User Goal:
    >   - To quickly see a range of posts that can be navigated to easily. 
    >   - To see a navigation menu which can direct to other areas of the site. 
    >   - To be able to click on relevant areas and be accurately taken to where I intend.
    
    #### Website Goal:
    >   - To give users a clear communication of the site's layout. 
    >   - To provide the user key information to use the site effectively. 

### Full Post Page
![](image_placeholder)
- This is the page in which readers can view a post and, if logged in, can comment on the post. 
    #### User Goal:
    >   - To read a blog post about a book I may be interested in. 
    >   - If I am logged in, to comment on the posts and provide my input to the conversation. 
    #### Website Goal:
    >   - To clearly display the blog article.
    >   - To give the user the opportunity to comment on posts if they are logged in. 

### Upcoming Post Page
![](image_placeholder)
- This page allows to see a list of upcoming posts. 
    #### User Goal:
    >   - To see what future posts are planned so that I can be aware of anything of interest that is upcoming. 
   
    #### Website Goal:
    >   - To display only the basic information of draft posts so that users can be informed of what is comming up. 



# Wireframes
Add wireframes

# Design
Discuss colours mention coolors

# Features
## Existing Features
Features, 

# Features

## Existing Features

### Navigation


### Home Page


### Blog Post List


### Individual Blog Post View


### Upcoming Posts List


### Comments Section


### User Authentication
- Login/logout functionality
- User registration 


### Admin Panel



## Future Features
- Category/tag filtering for posts
- User ratings for books
- Newsletter signup
- User profiles

# Data Model
Describe data model and addd diagram 

# Testing

## Manual Testing

### Browser Compatibility
Test on different browsers 

### Responsiveness
Describe how done, what screen sizes etc.

### Navigation
Check each link works as intended

### CRUD Functionality
Manual test of Create, Read, Update, and Delete operations 
- Blog posts (as admin)
- Comments (as user)

### User Authentication
Test -->
- User registration
- User login
- User logout


### Forms
Test forms
- Comment submission


### Content Display

- Blog posts display correctly with all elements (title, content, author, date)
- Images load properly
- Upcoming posts list is accurate

### User Interactions
- Leaving comments
- Edit / Delete comments 


### Error Handling
What happens if form isnt filled correctly or url is incorrect

### Performance
I observed the loading times and overall performance on different devices and connection speeds.


## Automated Testing
Describe automated tests

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