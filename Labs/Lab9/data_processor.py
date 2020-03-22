"""
This module contains a program that loads an excel file and creates charts
from it.
"""
import pandas

from Labs.Lab9.observers import *


class DataProcessor:
    """
    Class DataProcessors is the core that observers can subscribe to.
    If the internal state of the core changes, the all the observers
    get notified.
    """

    def __init__(self) -> None:
        """
        Initialize a DataProcessor with an empty callback list.
        """
        self.callbacks = []

    def subscribe_callbacks(self, *args: list) -> None:
        """
        Accepts a variable number of callback objects and adds them to the
        list of callbacks.
        :param args: list of observers.
        """
        for item in args:
            self.callbacks.append(item)

    def process_data(self, excel_file: str, output_title: str) -> None:
        """
        Reads the excel file into a dataframe using pandas and extracts the
        two columns.
        :param excel_file:
        :param output_title:
        :return:
        """
        df = pandas.read_excel(excel_file)
        title = excel_file.split('.')[0]
        data = []
        labels = df.columns.ravel()
        for column in labels:
            data.append(pandas.Series(df[column]))
        for observer in self.callbacks:
            observer(title, data, labels, output_title)


def main() -> int:
    """
    Generates DataProcessor object, creates observer objects, subscribes
    them to be called, calls process_data method to generate charts from
    excel document.
    :return: int
    """
    data_processor = DataProcessor()
    line_graph_oberserver = LineGraph('--', False, 'yellow')
    bar_graph_obserserver = BarGraph(False, 'black', 'red')
    table_generator_observer = TableGenerator('left')
    data_processor.subscribe_callbacks(line_graph_oberserver,
                                       bar_graph_obserserver,
                                       table_generator_observer)
    data_processor.process_data('Temperatures.xlsx', 'temp')


if __name__ == '__main__':
    main()
