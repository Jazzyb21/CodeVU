#Directions!
# 1. install Flask - open terminal in VS CODE 
# Run this command: pip install Flask



# to build to this web service quickly I am using FLASK
# a lightweight web framework - meaning a thir party python library used for developing web applications
#need a server in place to handle request in response cycle
from flask import Flask
import json

data = '''
[
    {
        "superhero":"Batman", 
        "publisher":"DC Comics", 
        "alter_ego":"Bruce Wayne",
        "first_appearance":"Detective Comics #27",
        "characters":"Bruce Wayne"
    },
    {
        "superhero":"Superman", 
        "publisher":"DC Comics", 
        "alter_ego":"Kal-El",
        "first_appearance":"Action Comics #1",
        "characters":"Kal-El"
    },
    {
        "superhero":"Flash", 
        "publisher":"DC Comics", 
        "alter_ego":"Jay Garrick",
        "first_appearance":"Flash Comics #1",
        "characters":"Jay Garrick, Barry Allen, Wally West, Bart Allen"
    },
    {
        "superhero":"Green Lantern", 
        "publisher":"DC Comics", 
        "alter_ego":"Alan Scott",
        "first_appearance":"All-American Comics #16",
        "characters":"Alan Scott, Hal Jordan, Guy Gardner, John Stewart, Kyle Raynor, Jade, Sinestro, Simon Baz"
    },
    {
        "superhero":"Green Arrow", 
        "publisher":"DC Comics", 
        "alter_ego":"Oliver Queen",
        "first_appearance":"More Fun Comics #73",
        "characters":"Oliver Queen"
    },
    {
        "superhero":"Wonder Woman", 
        "publisher":"DC Comics", 
        "alter_ego":"Princess Diana",
        "first_appearance":"All Star Comics #8",
        "characters":"Princess Diana"
    },
    {
        "superhero":"Martian Manhunter", 
        "publisher":"DC Comics", 
        "alter_ego":"J'onn J'onzz",
        "first_appearance":"Detective Comics #225",
        "characters":"Martian Manhunter"
    },
    {
        "superhero":"Robin/Nightwing", 
        "publisher":"DC Comics", 
        "alter_ego":"Dick Grayson",
        "first_appearance":"Detective Comics #38",
        "characters":"Dick Grayson"
    },
    {
        "superhero":"Blue Beetle", 
        "publisher":"DC Comics", 
        "alter_ego":"Dan Garret",
        "first_appearance":"Mystery Men Comics #1",
        "characters":"Dan Garret, Ted Kord, Jaime Reyes"
    },
    {
        "superhero":"Black Canary", 
        "publisher":"DC Comics", 
        "alter_ego":"Dinah Drake",
        "first_appearance":"Flash Comics #86",
        "characters":"Dinah Drake, Dinah Lance"
    },
    {
        "superhero":"Spider Man", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Peter Parker",
        "first_appearance":"Amazing Fantasy #15",
        "characters":"Peter Parker"
    },
    {
        "superhero":"Captain America", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Steve Rogers",
        "first_appearance":"Captain America Comics #1",
        "characters":"Steve Rogers"
    },
    {
        "superhero":"Iron Man", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Tony Stark",
        "first_appearance":"Tales of Suspense #39",
        "characters":"Tony Stark"
    },
    {
        "superhero":"Thor", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Thor Odinson",
        "first_appearance":"Journey into Myster #83",
        "characters":"Thor Odinson"
    },
    {
        "superhero":"Hulk", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Bruce Banner",
        "first_appearance":"The Incredible Hulk #1",
        "characters":"Bruce Banner"
    },
    {
        "superhero":"Wolverine", 
        "publisher":"Marvel Comics", 
        "alter_ego":"James Howlett",
        "first_appearance":"The Incredible Hulk #180",
        "characters":"James Howlett"
    },
    {
        "superhero":"Daredevil", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Matthew Michael Murdock",
        "first_appearance":"Daredevil #1",
        "characters":"Matthew Michael Murdock"
    },
    {
        "superhero":"Hawkeye", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Clinton Francis Barton",
        "first_appearance":"Tales of Suspense #57",
        "characters":"Clinton Francis Barton"
    },
    {
        "superhero":"Cyclops", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Scott Summers",
        "first_appearance":"X-Men #1",
        "characters":"Scott Summers"
    },
    {
        "superhero":"Silver Surfer", 
        "publisher":"Marvel Comics", 
        "alter_ego":"Norrin Radd",
        "first_appearance":"The Fantastic Four #48",
        "characters":"Norrin Radd"
    }
]'''
# this app calls the server
# Whenever the Python interpreter reads a source file, it does two things:
# it sets a few special variables like __name__, and then
# it executes all of the code found in the file
app = Flask(__name__)

deserialized_json = json.loads(data)
@app.route("/", methods=['GET'])
def welcome():
    return 'Welcome to my web service!!'
#decorator
@app.route("/hero/getHeroes", methods=['GET'])
def get_heroes():
    return json.dumps(deserialized_json)

@app.route('/hero/getHero/<superhero>', methods=['GET'])
def get_hero(superhero):
    #list comprehension syntax
    #super_hero =[hero for hero in deserialized_json if(hero['superhero'] == superhero)]
    for hero in deserialized_json:
        if (hero['superhero'] == superhero):
            return json.dumps(hero)

if(__name__ == "__main__"):
    app.run()
