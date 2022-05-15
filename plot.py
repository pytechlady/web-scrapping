
import matplotlib.pyplot as plt
from request import RequestUrl


class PlotGraph:
    # function to plot the pie chart
    @staticmethod
    def make_graph(res):
        new_word = []
        # res = RequestUrl()
        for item in res.count_occur():
            new_word.append(item)
        print(f'The top word is: {new_word[0]}')
        x = res.count_occur().keys()
        y = res.count_occur().values()
        plt.pie(y, labels=x, autopct="%1.1f%%")
        plt.show()