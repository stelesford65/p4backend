# Project Overview

## Project Schedule

This schedule will be used to keep track of your progress throughout the week and align with our expectations.  

You are **responsible** for scheduling time with your squad to seek approval for each deliverable by the end of the corresponding day, excluding `Saturday` and `Sunday`.

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Day 2| Working RestAPI | Complete
|Day 3| Core Application Structure (HTML, CSS, etc.) | Complete
|Day 4| MVP & Bug Fixes | Complete
|Day 5| Final Touches and Present | Complete

## Project Description

Use this section to describe your final project and perhaps any links to relevant sites that help convey the concept and\or functionality.

## Google Sheet

Include link to your google sheet here.  Here is the sample [Suresh had used in class](https://docs.google.com/spreadsheets/d/1V1M3Eq1NXH2PNmeTlVviRhEjX9kenq769Vo2P5mMtro/edit#gid=0) 

## Wireframes

Upload images of wireframe to cloudinary and add the link here with a description of the specific wireframe. Do not include the actual image and have it render on the page.  

- [Mobile](https://git.generalassemb.ly/SEIR-629/project-1-portfolio/blob/master/readme-assets/mobile.png)
- [Tablet](https://git.generalassemb.ly/SEIR-629/project-1-portfolio/blob/master/readme-assets/nav-highlight.gif)
- [Desktop](https://git.generalassemb.ly/SEIR-629/project-1-portfolio/blob/master/readme-assets/desktop.png)

Wireframing Resources:

- [Mockflow](https://mockflow.com/app/#Wireframe)
- [Figma](https://www.figma.com/)


## Time/Priority Matrix 

Include a full list of features that have been [prioritized](https://res.cloudinary.com/doaftkgbv/image/upload/v1583773146/ValueVSComplexity_u2inhx.png) based on the `Time and Priority` Matix.  This involves drawing a a square.  In the middle of the square, on the x axis draw a line.  The most left part of the line should start with 0hrs and the end of the line should include 2hrs.  This line will be used to estimate how much time any one feature will take to complete. 

Now draw a vertical line on the y axis.  The top of this line should have `High` and the bottom `Low`.  This line will be used to assign a priority to to each feature you wish to include in the project.  

Now create a separate list starting with A and assign it one of the features.  Continue to assign each feature a letter.  Once complete add each letter to the matrix assigning based on what your feel it's prioirty is an how long it will take to implement. If any one feature takes longer than 2hrs to complete than break it down into smaller tasks and reassign them a new letter. 

Once complete tally up the time and determine how long the project will take to complete. Now break those features into MVP and PostMVP so you can guarantee you will have a fully functioning project to demo. 

### MVP/PostMVP - 5min

The functionality will then be divided into two separate lists: MPV and PostMVP.  Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion.  

#### MVP (examples)

- Pull data using google json api
- Render data on page 
- Allow user to choose favorites 
- Save their choices in firebase

#### PostMVP 

- Anything else that is not MVP

## Functional Components

Based on the initial logic defined in the previous sections try and breakdown the logic further into functional components, and by that we mean functions.  Try and capture what logic would need to be defined if the game was broken down into the following categories.

Time frames are also key in the development cycle.  You have limited time to code all phases of the game.  Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe.

#### MVP - FRONTEND
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Hamburger | H | 1hr | 1hr | 1hr|
| Project Previews | H | 2hr | 1hr | 1hr|
| Regular Nav | H | 0.5hr | 0.5hr|0.5hr|
| Adding Form | H | 1.5hr| 0.5hr | 0.5hr |
| Other sections and flex| M | 0.5hr | 0.5hr | 0.5hr|
| Working with API | H | 12hrs| 48hr | 48hr |
| Responsive | H | 3hr | 1hr | 1hr|
| Social Media Icons | L | 1hr | 0.5hr | 0.5hr|
| Total | H | 20hrs| 54hr | 54hr |

#### MVP - BACKEND
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Models | H | 1hr | 1hr | 1hr|
| Serializer | H | 1hr | 1hr | 1hr|
| Authentication | H | 1hr | 1hr | 1hr|
| Settings| H | -hr| 0.5hr | 0.5hr |
| views| H | 4hr | 2hr | 2hr|
| Total | H | 7 hrs| 5.5hr | 5.5hr |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Project Hover | L | 3hr | -hr | -hr|
| Banner letters wiggle | L | 1hr | -hr | -hr|
| Interactive Banner | M | 4hr | -hr | -hr|
| Materialize | H | 4hr | -hr | -hr|
| Bootstrap | H | 4hr | -hr | -hr|
| Make own icon | L | 4hr | -hr | -hr|
| Total | H | 20hrs| -hrs | -hrs |



## Additional Libraries
 Use this section to list all supporting libraries and thier role in the project. 
```
asgiref==3.2.10
authentication==1.1.0
click==7.1.2
dj-database-url==0.5.0
Django==3.1.1
django-cors-headers==3.5.0
django-heroku==0.3.1
django-serializer==0.0.8
djangorestframework==3.11.1
djangorestframework-jwt==1.11.0
djangorestframework-simplejwt==4.4.0
Flask==1.1.2
future==0.18.2
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
passlib==1.7.2
Pillow==7.2.0
psycopg2==2.8.6
pycryptodome==3.9.8
PyJWT==1.7.1
pytz==2020.1
redis==3.5.3
serializers==0.2.4
sqlparse==0.3.1
Werkzeug==1.0.1
whitenoise==5.2.0
WTForms==2.3.3

```
## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
 newPicture: function(){
      const {tokens} = this.$route.query
      console.log(tokens)
      fetch("https://stp4backend.herokuapp.com/api/pictures/",{
      method: 'post',
      headers:{
        authorization: `JWT ${tokens.token}`,
        'Content-Type':'application/json',
      },
        body: JSON.stringify({image: this.image})
    })
      .then(() =>{
        this.getPicture()
      })
    },

	I am proud of this snippet of code because I wasn't sure how to allow users to add a new image to my frontend
```

## Issues and Resolutions
 ```
 ISSUE: Users could log in even with incorrect password
 SOLUTION: Add an if statemnt to check for 400 status

 ISSUE: Couldn't get my blogs to display
 SOLUTION: Fixed a simple syntax error (blog_entry.results rather than blog_entry)
 ```

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

## Previous Project Worksheet
 - [Readme's](https://github.com/jkeohan/fewd-class-repo/tree/master/final-project-worksheet/project-worksheet-examples)
 - [Best of class readme](https://github.com/jkeohan/fewd-class-repo/blob/master/final-project-worksheet/project-worksheet-examples/portfolio-gracie.md)
