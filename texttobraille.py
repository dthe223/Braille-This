"""
Author:Karthik Nayak, Jacob Pawlak
Date: April 15th, 2017
"""

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

def main():
      
        alexa_file  = open("alexa_output.txt", "r")
        
        input_text = alexa_file.read() 
        alexa_file.close()
        
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
    
main()
