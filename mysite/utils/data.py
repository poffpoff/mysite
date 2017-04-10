import csv
from django.http import HttpResponse
import datetime



class DataFile:
    datafiles_folder_path = "datafiles/"
    def __init__(self, name_ref):
        self.name_ref = name_ref
        self.file_ref = self.datafiles_folder_path + name_ref + ".csv"



class DataSet:
    def __init__(self, name_ref, time_set, data_set):
        self.name_ref = name_ref
        self.time = DataFile(time_set)
        self.data = DataFile(data_set)


class WriterCSV:
    def __init__(self, data_set_path):
        self.time_path = "datafiles/{0}_time.csv".format(data_set_path)
        self.data_path = "datafiles/{0}_data.csv".format(data_set_path)

    def write(self,time,data):
        time_ref = datetime.datetime.now()
        with open(self.time_path, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([time_ref,time])

        with open(self.data_path, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([time_ref,data])

# class ReaderCSV:
    #
    # # def __init__(self, data_set_path):
    # #    # self.time_path = "datafiles/{0}_time.csv".format(data_set_path)
    # #    #  self.time_path = "datafiles/YHOO_time.csv"
    # #    # self.data_path = "datafiles/{0}_data.csv".format(data_set_path)
    # #    #  self.data_path = "datafiles/YHOO_data.csv"
    #
    # def read(self):
    #
    #     with open(self.time_path, 'r', newline='') as csvfile:
    #         spamwriter = csv.reader(csvfile, delimiter=' ',
    #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         timeRows = ()
    #         timeCheckRows = ()
    #         for row in spamwriter:
    #             timeRows = timeRows + (row[1],)
    #             timeCheckRows = timeCheckRows + (row[0],)
    #
    #
    #     with open(self.data_path, 'r', newline='') as csvfile:
    #         spamwriter = csv.reader(csvfile, delimiter=' ',
    #                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         dataRows = ()
    #         dataCheckRows = ()
    #         for row in spamwriter:
    #             dataRows = timeRows + (row[1],)
    #             dataCheckRows = timeCheckRows + (row[0],)
    #
    #     if(timeCheckRows==dataCheckRows):
    #         return timeRows, dataRows
    #     else:
    #         return None



# from stockMarket.models import ShareModel; YHOO = ShareModel(name_ref = "YHOO");
