#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Jameson's User-Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>User Signup</h1>
"""

# User signup form
signup_form = """
    <form action="/" method="post">
        <table>
            <tr>
                <td>
                    <label for="username">Username</label>
                </td>
                <td>
                    <input type="text" required name="username" value="%(username)s" />
                    <span class="error">%(username_error)s</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="password">Password</label>
                </td>
                <td>
                    <input type="password" required name="password" />
                    <span class="error">%(password_error)s</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="passwordConfirm">Confirm Password</label>
                </td>
                <td>
                    <input type="password" required name="passwordConfirmed" />
                    <span class="error">%(passwordConfirmed_error)s</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="email">Email (optional)</label>
                </td>
                <td>
                    <input type="email" name="email" value="%(email)s"/>
                    <span class="error">%(email_error)s</span>
                </td>
            </tr>
        </table>
        <input type="submit" value="Sign Up!" />
    </form>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


# putting the page together
content = page_header + signup_form + page_footer

# reg expressions for username, password, email
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


# defining what a valid username is
def is_valid_username(username):
    return USER_RE.match(username)


# defining what a valid password is
def is_valid_password(password):
    return PASS_RE.match(password)


# defining what a valid email is
def is_valid_email(email):
    return EMAIL_RE.match(email)


class MainHandler(webapp2.RequestHandler):
    # create the form, set error variables to blank for form creation
    def write_form(self, username_error="", password_error="", passwordConfirmed_error="", email_error="", username="",
                   email=""):
        self.response.out.write(content % {"username_error": username_error,
                                        "password_error": password_error,
                                        "passwordConfirmed_error": passwordConfirmed_error,
                                        "email_error": email_error,
                                        "username": username,
                                        "email": email})

    def get(self):
        self.write_form()

    def post(self):
        # get what our variables currently are
        # should add an html escape so someone cant input html
        username = self.request.get("username")
        password = self.request.get("password")
        passwordConfirmed = self.request.get("passwordConfirmed")
        email = self.request.get("email")

        # set error messages to blank
        username_error = ""
        password_error = ""
        passwordConfirmed_error = ""
        email_error = ""

        # set error to false
        error = False

        if is_valid_username(username) == None:
            username_error = "Username is invalid"
            error = True

        if not password:
            if not passwordConfirmed:
                passwordConfirmed_error = "Password cannot be left blank"
            password_error = "Password cannot be left blank"
            error = True
        elif is_valid_password(password) == None:
            password_error = "Password is invalid"
            error = True

        if password != passwordConfirmed:
            passwordConfirmed_error = "Passwords do not match"
            error = True

        if email and is_valid_email(email) == None:
            email_error = "Email is invalid"
            error = True

        # if error is TRUE give error
        # else send to welcome page with username
        if error:
            self.write_form(username_error, password_error, passwordConfirmed_error, email_error, username, email)
        else:
            self.redirect("/welcome?name=" + username)


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("name")
        welcome_message = "<h1>Welcome, " + username + "!</h1>"
        welcome_content = page_header + welcome_message + page_footer
        self.response.out.write(welcome_content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
