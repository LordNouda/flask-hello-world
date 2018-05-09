# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True


# use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    """Return the 'Hello, World!' example."""
    return "Hello, World!?!?!?!"


# use the decorator pattern to pass input
# <value> is treated as string (unicode)
# <int:value> is treated as an integer
# <float:value> is treated as a floating point
# <path:some/great/path/> is treated as a path
@app.route("/test/<search_query>")
# dynamic route
def search(search_query):
    """Return a greeting string."""
    return "Hello " + str(search_query)


@app.route("/int/<int:value>")
def int_type(value):
    """Return correct after printing the input value."""
    print(value + 1)
    return "correct"


@app.route("/float/<float:value>")
def float_type(value):
    """Return correct after printing the input value."""
    print(value + 1)
    return "correct"


@app.route("/path/<path:value>")
def path_type(value):
    """Return correct after printing the input value."""
    print(value)
    return "correct"


# return can take the form of a tuple (response, status, header)
# if nothing but the response is provided, flask finds out the correct missing
# tuple entries by "magic."
@app.route("/name/<name>")
def index(name):
    """Return a greeting if the correct name is entered."""
    if name.lower() == "michael":
        return "Hello, {}".format(name), 200  # using (response, status) tuple
    else:
        return "Not Found", 404


# start the development server using the run() method
if __name__ == "__main__":
    app.run()
