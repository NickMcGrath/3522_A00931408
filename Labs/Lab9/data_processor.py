import pandas

from Labs.Lab9.observers import *


class DataProcessor:
    def __init__(self) -> None:
        self.callbacks = []

    def subscribe_callbacks(self, *args: list) -> None:
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
        for column in df.columns.ravel():
            data.append(pandas.Series(df[column]))
        labels = df.columns.ravel()
        for observer in self.callbacks:
            observer(title, data, labels, output_title)


def main() -> int:
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
