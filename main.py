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

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

# User signup form
form = """
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
                    <input type="password" required name="passwordMatch" />
                    <span class="error">%(passwordMatch_error)s</span>
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

# reg expressions for username, password, email

# defining what a valid username is

# defining what a valid password is

# defining what a valid email is

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
