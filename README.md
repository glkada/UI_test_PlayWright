## Comprehensive Testing Demonstration Project
In this project, I selected an existing website to demonstrate my testing expertise. I created a Requirements Traceability Matrix (RTM), along with UI and API tests, to validate key scenarios.

# RTM (Requirements traceblity matrix)
There is an RTM attached with the name _RTM_.xlsx where I have built the RTM that covers features like App access, Ticket creation & Case creation. 

# UI tests
Framework selection: I selected **PlayWright** since our focus was only cross desktop-browser testing. As PlayWright uses chromium dev tools like protocol is alot more stable. <br />
                      Selenium uses APIs to communicate with the driver which introduces all the API related stablity issues. So it was better avoided. <br />
                      Cypress was an alternative as well, however, parallelization would be a task. <br />
                      WDIO would be my go to framework if mobile based browser testing was needed. <br />
Tests:
BeforeAll Hook: 
I first start with registering a user on the platform. Leveraged faker library here to ensure that the creation of email does not follow any specific preset pattern and is
genuinly dynamic.

Test Cases
1. Log into the platform create a ticket and asserts the ticket creation and log out. Leveraged 'expect' from PlayWright. 
2. Log into the platform creates a case and asserts the case creation and log out.


# API testing
I have added a file _API_TEST_.postman_collection.json. <br />
The API test includes: <br />
RBAC: <br />
  POST /login - Verify if we're able to login with valid credentials. Validation: Check for status 200 <br />
  POST /login - Verify if login fails if we don't pass credentials. Validation: Check for sstatus 422 <br />
  POST /login - Verify if login fails if we pass invalid credentials. Validation: Check for sstatus 403 <br />
Ticket creation: <br />
  POST /ticket - Create a new ticket for the User ID obtained after a successful login. Validation: A ticket ID should be returned. <br />
  GET /tickets - Get a list of tickets for the User ID obtained after a successful login. Validation: The ticket ID returned above should be present <br />
  PUT /ticket - Update a certain parameter for the ticket ID returned above. Validation: Check for status 200 and expect response Ticket updated. <br />
Get Cases: <br />
  GET /cases - Just logging all the cases created by the User ID obtained above. Validation: Added schema validation. <br />

# Future scope 
This script can easily be exececuted on multiple browsers in parallel. <br />
Some minor changes are needed to generate email address since we would like to generate email address only once and use it across <br />

# Project Setup Guide

This guide will walk you through installing the necessary dependencies, setting up Playwright browsers, and running tests using `pytest`.

---

# Prerequisites

Make sure you have the following installed:

1. **Python** (version 3.8 or above)  
   [Download Python](https://www.python.org/downloads/)

2. **pip** (Python's package manager)  
   Comes pre-installed with Python. You can verify by running:  
   ```bash
   pip --version
   ```

---

# 1. Install Dependencies

Run the following command to install all the dependencies:

```bash
pip install -r requirements.txt
```

---

# 2. Install Playwright Browsers

After installing the dependencies, you need to install the Playwright browsers. Use the following command:

```bash
playwright install
```

This will download and set up Chromium, Firefox, and WebKit browsers.

Alternatively, to install specific browsers only, use:

```bash
playwright install chromium firefox webkit
```

---

# 3. Running Tests with `pytest`

To run the tests using `pytest`, navigate to your project directory and execute:

Run the Playwright-integrated tests using:

```bash
pytest --headed --browser=chromium --browser=webkit
```

---

# Troubleshooting

- **`pip` command not found**: Ensure Python is added to your system's PATH.
- **Browser installation fails**: Check your internet connection and retry `playwright install`.
- **Module not found errors**: Ensure all dependencies are listed in `requirements.txt` and correctly installed.

---

# Conclusion

This guide covers the basic setup to install dependencies, install Playwright browsers, and run tests using `pytest`. For more advanced configuration, refer to the [Playwright documentation](https://playwright.dev/) or the [pytest documentation](https://docs.pytest.org/).

# Feedback/Suggestion
Thanks, for coming up with a feedback/suggestion. You can reach out to me on adityagholkar@gmail.com
