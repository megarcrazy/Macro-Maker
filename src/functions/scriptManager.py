import csv
import src.settings as settings


class ScriptManager:

    @staticmethod
    def saveScript(script_array, url='./save/demo.csv'):
        try:
            with open(url, 'w', newline='') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerows(script_array)
            print('your script has been saved')
        except:
            print('An error has occured script not saved')
          
    @staticmethod
    def loadScript(url='./save/demo.csv'):
        try:
            with open(url, 'r') as f:
                csv_reader = csv.reader(f)
                script_array = []
                for row in csv_reader:
                    script_array.append(row)
            print('you loaded the script')
            return script_array
        except:
            print('you failed to load the script')
            return []

    @staticmethod
    def deleteScript(url):
        print('you deleted the script')
