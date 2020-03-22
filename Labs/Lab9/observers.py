"""
This module contains observer objects that use data in a 2d array of width 2.
"""
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import abc


# commented out because:
# All observers need to adhere to the interface given below. This should be
# implemented informally. That means, do not implement an ABC that matches the
# diagram below. Please adhere to the method and class names exactly as I may
# use a script to help grade your labs.
# class IObserver:
#     def __call__(self, title:str, data:list,labels:list,
#                  output_name:str)->None:
#

class Graph(abc.ABC):
    """
    The Graph class represents a template for an observer that creates a graph.
    """

    @abc.abstractmethod
    def __call__(self, title: str, data: list, labels: list,
                 output_name: str) -> None:
        """
        Abstract method, each observer is implemented as a callable object.
        :param title: str
        :param data: list of Series objects
        :param labels: list
        :param output_name: str
        """
        pass


class LineGraph(Graph):
    """
    LineGraph is an observer that creates a graph when called.
    """

    def __init__(self, line_style: str, has_fill: bool,
                 fill_color: str) -> None:
        """
        Initializes the LineGraph object.
        :param line_style: str
        :param has_fill: bool
        :param fill_color: str
        """
        self.line_style = line_style
        self.has_fill = has_fill
        self.fill_color = fill_color

    def __call__(self, title: str, data: list, labels: list, output_name:
    str) -> None:
        """
        Creates a line graph .png from provided information.
        :param title: str
        :param data: list of Series objects
        :param labels: list
        :param output_name: str
        """
        plt.clf()
        if self.has_fill:
            plt.fill_between(data[0], data[1], color=self.fill_color)
        plt.title(title)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.plot(data, self.line_style)
        output_name += '_line'
        plt.savefig(output_name)


class BarGraph(Graph):
    """
    BarGraph is an observer that creates a graph when called.
    """

    def __init__(self, is_horizontal: bool, edge_color: str,
                 bar_color: str) -> None:
        """
        Initializes the BarGraph object.
        :param is_horizontal: bool
        :param edge_color: str
        :param bar_color: str
        """
        self.is_horizontal = is_horizontal
        self.edge_color = edge_color
        self.bar_color = bar_color

    def __call__(self, title: str, data: list, labels: list,
                 output_name: str) -> None:
        """
        Creates a bar graph .png from provided information.
        :param title: str
        :param data: list of Series objects
        :param labels: list
        :param output_name: str
        """
        plt.clf()
        plt.title(title)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        if self.is_horizontal:
            plt.barh(data[0], data[1], color=self.bar_color, \
                     edgecolor=self.edge_color)
        else:
            plt.bar(data[0], data[1], color=self.bar_color, \
                    edgecolor=self.edge_color)
        output_name += '_bar'
        plt.savefig(output_name)


class TableGenerator:
    def __init__(self, align: str) -> None:
        """
        Initializes the TableGenerator object.
        :param align: str
        """
        self.align = align

    def __call__(self, title: str, data: list, labels: list, output_name:
    str) -> None:
        """
        Creates a txt table from provided information.
        :param title: str
        :param data: list of Series objects
        :param labels: list
        :param output_name: str
        """
        table = PrettyTable()
        table.align = self.align
        table.title = title
        table.field_names = labels
        for i in range(0, len(data[0])):
            table.add_row([data[0][i], data[1][i]])
        print(table)
        output_name += '.txt'
        with open(output_name, 'w') as file:
            file.write(str(table))
