import matplotlib.pyplot as plt
from prettytable import PrettyTable
import abc


# class IObserver:
#     def __call__(self, title:str, data:list,labels:list,
#                  output_name:str)->None:
#

class Graph(abc.ABC):
    def __call__(self, title: str, data: list, labels: list,
                 output_name: str) -> None:
        pass


class LineGraph(Graph):
    def __init__(self, line_style: str, has_fill: bool,
                 fill_color: str) -> None:
        self.line_style = line_style
        self.has_fill = has_fill
        self.fill_color = fill_color

    def __call__(self, title: str, data: list, labels: list, output_name: str):
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
    def __init__(self, is_horizontal: bool, edge_color: str,
                 bar_color: str) -> None:
        self.is_horizontal = is_horizontal
        self.edge_color = edge_color
        self.bar_color = bar_color

    def __call__(self, title: str, data: list, labels: list,
                 output_name: str) -> None:
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
        self.align = align

    def __call__(self, title: str, data: list, labels: list, output_name: str):
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
