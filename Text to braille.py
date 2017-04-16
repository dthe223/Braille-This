"""
Design Prolog 
Author:Karthik Nayak
Date: 28th Feb 2017
Purpose: to ask the user for xxxxxxx and,
use it to generate xxxxxxx

Preconditions:  xxxxxxxxxxx

Postconditions:  xxxxxxxxxx
"""

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

user_resp = ""

def main():
	global user_resp
	
    app = Flask(__name__)   # Setup: Our basic app instance.
    
    ask = Ask(app, "/") # Setup: Our Amazon Skills Kit instance
    
    @ask.launch
    def prompt_text():  # What is asked on application launch
        input_prompt = render_template('prompt')    # "prompt" is stored in templates.yaml
        return question(input_prompt)
    
    @ask.intent("MessageIntent", convert={'response':str})
    def get_text(response): # Gets the user's message, passes it into the another program.
        # Some function that translates the response will go here
        global user_resp
    
        if user_resp == "":
            isRight = render_template('confirmStatement', response=response)
            user_resp = response
            return question(isRight)
        else:
            if response.lower() == "yes":
				input_text = user_resp;
				
				
				text_file = open("braille_to_stl.scad", 'w')
				
				output = "";
				
				position = [0, 0, 0]
				
						 
				
				for x in range(0, len(input_text)):
			 
						
					text_file.write("translate(" + str(position) + ")\n")
					
					if(position[1]<121):
						position[1] = position[1] + 15
					else:
						position[1] = 0
						position[0] = position[0] + 23
						
					if input_text[x] == ' ':       
						output = text_file.write("import(\"braille_bricks_" + "space.stl\"" + ", convexity=3);\n")                          
					else:
						output = text_file.write("import(\"braille_bricks_" + input_text[x].upper() + ".stl\", convexity=3);\n")         
					
						

				
				text_file.close()
				
                return statement(render_template('correct'))
            else:
                user_resp = ""
                return question(render_template('wrong'))
    
    if __name__ == '__main__':
        app.run(debug=False)    
		
main()
