import csv
import src.settings as settings


class ScriptManager:

    # Inputs script into a csv file as an array
    @staticmethod
    def saveScript(script_array, url):
        try:
            with open(url, 'w', newline='') as f:
                csv_writer = csv.writer(f, delimiter=',')
                csv_writer.writerows(script_array)
            print('your script has been saved')
        except:
            print('An error has occured script not saved')

    # Extracts the script array from the csv file
    @staticmethod
    def loadScript(url):
        print(url)
        try:
            file_name = url.split('/')[-1]
            print(f'running {file_name}')
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
