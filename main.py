# An entrypoint of your application
import requests.exceptions
from plot import PlotGraph


draw_bar = PlotGraph()
while True:
    cont_checking = input("Would you like to scrap a site? 'y'/'n': ").lower()
    if cont_checking == "y":
        try:
            draw_bar.make_graph()
        except requests.exceptions.MissingSchema:
            print("Invalid URL")
        except requests.exceptions.ConnectTimeout:
            print("404 error loading page")
        except requests.exceptions.ConnectionError:
            print("Connection error. Please try again later")

    elif cont_checking == "n":
        print("Thanks for analyzing! Come back again!")
        break
    else:
        print("Please enter y or n")