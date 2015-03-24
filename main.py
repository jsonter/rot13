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
import cgi

def doRot13(cText):
	returnText = ""
	for char in cText:
		charNum = ord(char)
		if (charNum >= 97) and (charNum <= 122):
			charNum += 13
			if charNum > 122:
				charNum -= 26
		elif (charNum >= 65) and (charNum <= 90):
			charNum += 13
			if charNum > 90:
				charNum -= 26

		returnText += chr(charNum)
	return returnText


form = """
			<h1>Enter Some Text to ROT13</h1>
			<br>
			<form method="post">
				<textarea name = "text" rows="4" cols="50">{0}</textarea>
				<br>
				<input type="submit">
			</form>
		"""

class MainHandler(webapp2.RequestHandler):
	def write_form(self, displayText=""):
		self.response.write(form.format(displayText))
	
	def get(self):
		self.write_form()

	def post(self):
		myText = self.request.get("text")
		newText = cgi.escape(doRot13(myText),True)
		self.write_form(newText)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)