<h1>Testing Section - The Swede Restaurant</h1>

 Go back to the README documentation **[here](/README.md)**.

<a id="table-of-contents"></a>
## Table of Contents

- [Table of Contents](#table-of-contents)
- [Code Validators](#code-validators)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Accessibility](#accessibility)
- [Lighthouse Report](#lighthouse-report)
- [Manual Testing](#manual-testing)
- [Additional Testing](#additional-testing)
- [Browsers](#browsers)
- [Bugs](#bugs)
- [Unsolved Bugs](#unsolved-bugs)

<a id="code-validators"></a>
## Code Validators 

### HTML

To validate the HTML code for all pages, I used the **[W3C Markup Validation Service](https://validator.w3.org)**. Where necessary, the code was validated by direct input. The results are presented below.

<details>
<summary>Home Page</summary>

![html validation of home page](/documentation/testing/html-validator-home.png)

</details>

<details>
<summary>Menu Page</summary>

![html validation of menu page](/documentation/testing/html-validator-menu.png)

</details>

<details>
<summary>Make Reservation (unregistered user) Page</summary>

![html validation of make reservation page for unregistered users](/documentation/testing/html-validator-reservationlogin.png)

</details>

<details>
<summary>Login Page</summary>

![html validation of login page](/documentation/testing/html-validator-login.png)

</details>

<details>
<summary>Signup Page</summary>

![html validation of signup page](/documentation/testing/html-validator-signup.png)

</details>

<details>
<summary>Make Reservation (registered user) Page</summary>

![html validation of make reservation page for registered users](/documentation/testing/html-validator-add.png)

</details>

<details>
<summary>My Reservations Page</summary>

![html validation of my reservations page](/documentation/testing/html-validator-myreservations.png)

</details>

<details>
<summary>Logout Page</summary>

![html validation of logout page](/documentation/testing/html-validator-logout.png)

</details>

<details>
<summary>Contact Page</summary>

![html validation of home page](/documentation/testing/html-validator-contact.png)

</details>

### CSS

To validate the CSS code for this project, I used the **[Jigsaw W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)**. Results are presented below.

![screenshot of css w3c validation](/documentation/testing/css-validation.png)

### Python 

To validate the Python code for this project, I used the **[CI Python Linter](https://pep8ci.herokuapp.com/)**. The results are presented below.

**The Bookings App**

<details>
<summary>admin.py</summary>

![screenshot of pep8 validation for admin file](/documentation/testing/pep8-adminpy.png)

</details>

<details>
<summary>apps.py</summary>

![screenshot of pep8 validation for app file](/documentation/testing/pep8-appspy.png)

</details>

<details>
<summary>forms.py</summary>

![screenshot of pep8 validation for forms file](/documentation/testing/pep8-formspy.png)

</details>

<details>
<summary>models.py</summary>

![screenshot of pep8 validation for models file](/documentation/testing/pep8-modelspy.png)

</details>

<details>
<summary>urls.py</summary>

![screenshot of pep8 validation for urls file](/documentation/testing/pep8-urlspy.png)

</details>

<details>
<summary>views.py</summary>

![screenshot of pep8 validation for views file](/documentation/testing/pep8-viewspy.png)

</details>

**theswederestaurant Project**

<details>
<summary>asgi.py</summary>

![screenshot of pep8 validation for asgi file](/documentation/testing/pep8-asgipy.png)

</details>

<details>
<summary>settings.py</summary>

![screenshot of pep8 validation for settings file](/documentation/testing/pep8-settingspy.png)

</details>

<details>
<summary>urls.py</summary>

![screenshot of pep8 validation for urls file](/documentation/testing/pep8-urlspy-2.png)

</details>

<details>
<summary>wsgi.py</summary>

![screenshot of pep8 validation for wsgi file](/documentation/testing/pep8-wsgi.png)

</details>

### JavaScript

To validate the JavaScript code for this project, I used **[JSHint](https://jshint.com/)**. The JavaScript code only make up one function regarding how long messages are displayed on the screen. The results are presented below.

![screenshot of jshint validation](/documentation/testing/jshint-validation.png)

## Accessibility

I used the web accessibility evaluation tool **[WAVE](https://wave.webaim.org/report#/https://the-swede-restaurant-883dacef11e8.herokuapp.com/)** to test the accessibility of the site. The result is presented below.

![screenshot of WAVE accessibility testing](/documentation/testing/wave-testing-screenshot.png)

## Lighthouse Report

I ran two Lighthouse reports in Chrome DevTools, one for mobile and one for desktop, to test performance and additional testing of accessibility. The results are presented below.

**Mobile**

![screenshot of lighthouse report mobile](/documentation/testing/lighthouse-report-mobile-sh.png)

**Desktop**

![screenshot of lighthouse report desktop](/documentation/testing/lighthouse-report-device-sh.png)

## Manual Testing

An approach of Behavior Driven Development (BDD) was used for the manual testing to ensure the functionality,
usability, responsiveness and data management of the project. BDD extends the already created user stories by translating them into a testable format. Each user story with its additional testable statement is presented in the table below, along with the test results.

| TEST PASS | USER STORY | TEST |
| ------------- | ------------  | ------------  |
| ✅  | #1 Navigation Bar: As a site user I can easily find the navigation bar so that I can navigate the different pages of the website. | Given that a user visits the site, when exploring different sections, then the navbar is visible on the top of the screen at all times.  |
| ✅  | #2 Logo Link: As a site user I can click the restaurant logo to get to the home page so that it is easy to navigate back if necessary.   | Given that a user visits the page, when the logo in the navbar is clicked, then the user will be relocated to the home page. |
| ✅  | #3 Find Menu: As a site user I can easily find the menu so that I can explore the food options.   | Given that a user visits the site, when they are looking for the menu, then they can find it in the navbar visible at all times. |
| ✅  | #4 Find Reservation Form: As a site user I can easily find where to make a reservation so that I can schedule when to visit the restaurant.   | Given that a user visits the site, when they want to make a reservation, then they can find a link to making a reservation in the navbar visible at all times. |
| ✅  | #5 Find Contact Details: As a site user I can find the contact information to the restaurant so that I know how to contact them if needed.   | Given that a user visits the site, when they want to find the restaurants contact information, then they can find a link to the contact page in the navbar visible at all times. |
| ✅  | #6 Home Page: As a site user I can get a clear first impression of what the site is about so that I can decide if I want to explore the website further. | Given that a first time user visits the site, when they see the home page, then they know that it is a restaurant with Swedish theme. |
| ✅  | #7 View Menu: As a site user I can view a clean and simple menu with relevant information so that I can quickly decide what I want to eat.   | Given that a user is viewing the menu, when they are looking at the items, then it is easy to see what is available. |
| ❌ Not implemented | #8 View Images of Food: As a site user I can view images of the food so that I know what it looks like.   | Given that a user is viewing the menu, when they look at the items, then images of the food are displayed. | 
| ✅ | #9 Social Media Links: As a site user I can easily find the restaurants social media links so that I can learn more about their business.   | Given that a user is visiting the site, when looking for the restaurants social media, then they can find links in the footer on all pages. |
| ✅ | #10 Design: As a site user I can enjoy a clean and simple design so that it is not a distraction when looking for information.   | Given that a user is visiting the site, when exploring the different pages, then the design is not distracting from the information.  |
| ❌ Not implemented | #11 Leave Review: As a site user I can find where to leave a review so that I can share my experience with others.  | Given that a user is logged in, when wanting to leave a review, then they can fill out a form to create a post.  | 
|  | #12 Download Menu: As a site user I can download the menu so that I can access it whenever.   | Given that the user is viewing the menu, when clicking the download button, then the menu is downloaded as a pdf.  | 
| ✅  | #13 Opening Hours: As a site user I can easily find the opening hours of the restaurant so that I know when it is possible to visit.   | Given that a user is looking for information regarding opening hours, when clicking "contact" in the navbar where opening hours would be expected to be, then they are relocated to the contact page where opening hours are displayed. |
| ❌ Not implemented | #14 View Map: As a Site User I can view the location of the restaurant on Google Maps so that I know where it is located.   | Given that a user wants to know the restaurants physical location, when viewing the contact page, then a google map with the restaurants location pinned is displayed.  |
| ✅ | #15 Create Account: As a site user I can create an account so that I can make, save, and manage my reservations.   | Given that a user wants register, when clicking register/signup, then they can fill out a form with username and password and email (optional) to create an account. | 
|  | #16 Login: As a registered user I can log in to my account so that I can access my information and reservations.   | Given that a user wants to log in, when entering their username and password, then the user will log in and be relocated to the view visible for logged in users.  | 
| ✅ | #17 Logout: As a registered user I can log out from my account so that I can protect my personal information.   | Given that a logged in user wants to log out, when the logout button is clicked, then the user will be logged out and return to the home page.  | 
| ❌ Not implemented | #18 Forgot Password: As a registered user I can reset my password so that I can keep my account save and access my information even if I forget my login information.   | Given that a user wants to reset their password, when clicking "forgot password?", then the user will recieve an email to reset their password.  |
| ❌ Not implemented  | #19 Delete Account: As a registered user I can delete my account so that I have the choice to remove my information from the site.   | Given that a user wants to delete their account, when clicing "delete account", then the user's account will be deleted.  |
| ✅  | #20 Admin Panel: As a restaurant owner/site manager I can view reservations from an admin panel so that I can plan my business. | Given that an admin is logged in, when viewing the panel, then the admin can see all reservations that has been made. |
| ✅  | #21 Make Reservation: As a registered user I can make a reservation at the restaurant through a form so that I can schedule a date and time to visit  | Given that the user is logged in, when wanting to make a reservation, then the user can fill out a form and submit their reservation details.  |
| ✅  | #22 View Reservations: As a registered user I can view my reservation(s) so that I can check the details.   | Given that a user is logged in, when viewing "my reservations", then the user will see all their reservations (or a message if there are none).  |
| ✅  | #23 Manage Reservation: As a registered user I can manage my reservation after its been saved in my account so that I can keep the restaurant updated if something changes.   | Given that a user wants to update a reservation, when clicking the edit button, then the previously filled out form will show up and the user can change the information. |
| ✅ | #24 Cancel Reservation: As a registered user I can cancel my reservation so that the date and time get available for other customers  | Given that a user wants to cancel a reservation, when the cancel button is clicked, then the reservation will be deleted from the table.  |

The user stories/tests marked with "❌ Not implemented" are marked as "won't have" for this release in the GitHub project.


## Additional Testing

| TEST PASS | TEST |
| -------- | -------- | 
| ✅ | Links/buttons will take the user to its itended pages |
| ✅ | The social media links open in a new window |
| ✅ | The different pages are responsive and work on different screen sizes |
| ✅ | The reservations shown on "my reservations" are specific to the logged in user |
| ✅ | A user that is not authenticated cannot show content for authenticated users |
| ✅ | The 404 page is displayed when the page does not exist |
| ✅ | User feedback displays in the form of messages after different actions |
| ✅ | The alert messages disappear by themselves |

## Browsers
I have tested that the application works in the following browsers:

* Safari
* Google Chrome
* Mozilla Firefox

## Bugs

* A few buttons (links styled as buttons) were cut in half on smaller screens. Fixed by adding media queries to the CSS file.

* The "reservations" button on the home page linked to the "make reservation" page for unregistered users, no matter if the user was logged in or not. Fixed by adding if else statement to HTML code.

* The footer would not stick to the bottom of the page without covering page content. Fixed by relative/absolute positioning (solution found in **[this](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/)** article).

## Unsolved Bugs

* The "Add New Reservation" button (link) on the "My Reservations" page still gets cut in half on screen sizes around 900-1000px. This is not solved.

* There is no restriction set so that the user cannot make a reservation for a past date. This is not solved.

* There should be a "are you sure you want to cancel your reservation" alert with buttons when the cancel button is clicked on "my reservations" so that the user does not accidentally cancels their reservation . This is not solved.
  
* The time slots could look better for made reservations on smaller screens. This is not solved.

 Go back to the README documentation **[here](/README.md)**.
