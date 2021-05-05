#%%
#import dependencies
from flask import Flask, render_template
from flask import Flask, request

#**********************************************
#%%

app = Flask(__name__)
   

# Create the routes

## <ROUTES REFLECTING DIFFERENT WEBPAGES> 
@app.route("/")
def home():
        return render_template ("home.html") 
#-------Route will return the webpage with turnout based on voter demographics: visualizations


@app.route("/schedule")
def Schedule():
    return render_template ("schedule.html")


@app.route("/faithstatement")
#----- Route will return the webpage with reasons why people don't turn out: visualizations
def Faithstatement():
    return render_template ("faithstatement.html")


@app.route("/guidelines")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Guidelines():
    return render_template("guidelines.html")

@app.route("/facilitators")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Facilitators():
    return render_template("facilitators.html")


@app.route("/chapter1")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chapter1():
    return render_template("chapter1.html")

@app.route("/chapter2-3")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chaptertwothree():
    return render_template("chapter2-3.html")

@app.route("/chapter567")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chapterfivesixseven():
    return render_template("chapter567.html")

@app.route("/chapter48")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chapterfoureight():
    return render_template("chapter48.html")

@app.route("/chapter910")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chapternineten():
    return render_template("chapter910.html")

@app.route("/chapter11-13")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chaptereleventwelvethirteen():
    return render_template("chapter11-13.html")

@app.route("/chapter1617")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Chaptersixteenseventeen():
    return render_template("chapter1617.html")

#FACILITATOR RESOURCE LINKS
@app.route("/resources")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Resourcesaddictions():
    return render_template("sexualAddictionnotes.html")

@app.route("/separategroups")
#---- Route will return the webpage with visualizations depicting turnout based on voter competitiveness
def Resourcesgroups():
    return render_template("separategroups.html")


if __name__ == "__main__":
    app.run()

