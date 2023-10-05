<h1>Testing Section - The Swede Restaurant</h1>

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

Go back to BDD (Behavior Driven Development) module.
Add checklist for manual testing and make it well structured. 

| TEST PASS | USER STORY | TEST |
| ------------- | ------------  | ------------  |
|  | #1 Navigation Bar: As a site user I can easily find the navigation bar so that I can navigate the different pages of the website. | ------------  |
|  | #2 Logo Link: As a site user I can click the restaurant logo to get to the home page so that it is easy to navigate back if necessary.   | -----------  | 
|  | #3 Find Menu: As a site user I can easily find the menu so that I can explore the food options.   | ------------  | 
|  | #4 Find Reservation Form: As a site user I can easily find where to make a reservation so that I can schedule when to visit the restaurant.   | ------------  | 
|  | #5 Find Contact Details: As a site user I can find the contact information to the restaurant so that I know how to contact them if needed.   | ------------  |
|  | #6 Home Page: As a site user I can get a clear first impression of what the site is about so that I can decide if I want to explore the website further. | ------------  | 
|  | #7 View Menu: As a site user I can view a clean and simple menu with relevant information so that I can quickly decide what I want to eat.   | ------------  | 
|  | #8 View Images of Food: As a site user I can view images of the food so that I know what it looks like.   | ------------  | 
|  | #9 Social Media Links: As a site user I can easily find the restaurants social media links so that I can learn more about their business.   | ------------  | 
|  | #10 Design: As a site user I can enjoy a clean and simple design so that it is not a distraction when looking for information.   | ------------  | 
|  | #11 Leave Review: As a site user I can find where to leave a review so that I can share my experience with others.  | ------------  | 
|  | #12 Download Menu: As a site user I can download the menu so that I can access it whenever.   | ------------  | 
|  | #13 Opening Hours: As a site user I can easily find the opening hours of the restaurant so that I know when it is possible to visit.   | ------------  | 
|  | #14 View Map: As a Site User I can view the location of the restaurant on Google Maps so that I know where it is located.   | ------------  | 
|  | #15 Create Account: As a site user I can create an account so that I can make, save, and manage my reservations.   | ------------  | 
|  | #16 Login: As a registered user I can log in to my account so that I can access my information and reservations.   | ------------  | 
|  | #17 Logout: As a registered user I can log out from my account so that I can protect my personal information.   | ------------  | 
|  | #18 Forgot Password: As a registered user I can reset my password so that I can keep my account save and access my information even if I forget my login information.   | ------------  | 
|  | #19 Delete Account: As a registered user I can delete my account so that I have the choice to remove my information from the site.   | ------------  | 
|  | #20 Admin Panel: As a restaurant owner/site manager I can view reservations from an admin panel so that I can plan my business. | ------------  |
|  | #21 Make Reservation: As a registered user I can make a reservation at the restaurant through a form so that I can schedule a date and time to visit  | ------------  | 
|  | #22 View Reservations: As a registered user I can view my reservation(s) so that I can check the details.   | ------------  | 
|  | #23 Manage Reservation: As a registered user I can manage my reservation after its been saved in my account so that I can keep the restaurant updated if something changes.   | ------------  | 
|  | #24 Cancel Reservation: As a registered user I can cancel my reservation so that the date and time get available for other customers  | ------------  |

## Additional Testing

Could also be a checklist. Make sure all features of the application are tested.