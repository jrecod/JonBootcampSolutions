#### Project Overview
- I will be making a personal blog. My client requested a simple website with only a login for themselves but no user log in. The users would just use a newsletter subscription and a comment section for each individual post. Blog will be divided into 4 categories. The website will be using django and materialize. Photo hosting will be done on photobucket. Comments will be handled by disqus.




#### Functionality

- Landing Page: 
The landing page of the blog will have a nav bar with links to the about me, newsletter subscription, a keep in touch button that would display a link to my client's instagram and youtube channel. In the middle of the landing page the user would see 4 cards that would be labeled with the 4 blog categories. Clicking on the card would take the user to the next page that would contain that specific categories blog posts. 

- Blog Category Page:
On the blog category page the nav bar would contain a button for a side nav that would have links to the other categories so the user wouldn't have to go back on the browser. Under the nav the user would be able to scroll through a list of the blog posts of the category. Posts will be sorted newest to oldest. The posts would be listed with their photo with the title and date of the post to the right and clicking on the photo would take you to that specifics posts page. Bottom of the page would have a footer containing a newsletter subscribe link, about me link, and links to the youtube and instagram accounts.

- Blog Post Page: 
The blog post page would have the same nav bar as the category page. Under that in small font you would see the category of that post and under that in larger bolder font you would have the blog posts title. Bellow that you would have that post's photo. Bellow the photo you would have that post's text. Bellow the text there will be a comment input section. I will be using disqus to host the commenting. At the bottom there would be the same footer from the blog category page

- About Me Page: 
About me will be a simple page that will have my clients name, portrait and bio. At the bottom there would be the same footer from the blog category page.





#### Data Model

- Blog post:
    - title
    - body
    - image
    - date created
    - category

- Blog category:
    - category(using a foreign key to connect it to the blog post)
        







#### Schedule

- Week one: Create models and views. Create template for each page and set up the rich text editor for the blog post submission page.

- Week two: Start working on layout in the templates. Starting with the blog post page to ensure disqus is working and that the site is pulling photos from photo bucket

- Week three: Finish the templates and styling.

- post class: Finish and fix any small inconsistencies in the front end and deploy.



#### Notes

rich text editor for blog posts: tinymce

Tag blog post w/ type(fashion, health & fitness, food...etc). Many to many. (think types with pokedex)

on page load subscription modal email newsletter.(popup)
send subscribers emails when new content is posted. 
newsletters for letting subscribers know about the recent posts.


Blog Categories: Confidence, Fashion, Skin Care, Health + Fitness.