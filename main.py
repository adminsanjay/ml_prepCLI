# pyrefly: ignore [missing-import]
from termcolor import colored
from data_description import DataDescription
from data_input import DataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling
class Preprocessor:
    tasks=[
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]
    data = 0
    def __init__(self):
        self.data = DataInput().get_data()
        print("\n\n"+colored("Data loaded successfully to preprocessor CLI\U0001F601",attrs=["bold"],color="green")+ "\n\n")
    
    def remove_column(self):
        print("Columns\U0001F447\n")
        for col in self.data.columns:
            print(col, end="\t")
        while(1):
            col = input("\nWhich column you want to remove? (type '-1' if you don't want to remove any)\n").lower()
            if col == "-1":
                exit()
            ch = input("Are you sure you want to remove this column? (y/n)\n").lower()
            if ch=='y':
                try:
                    self.data.drop([col],axis=1, inplace=True)
                    print(colored("Column removed successfully", attrs=["bold"], color="green"))
                except KeyError:
                    print(colored("Column not found, Please enter a valid column name", attrs=["bold"], color="red"))
                    continue
                print("Done\U0001F601")
                break
            else:
                print(colored("Please try again with a valid column name", attrs=["bold"], color="yellow"))
            return
    
    def print_data(self):
        print(self.data)

    def main(self):
        self.remove_column()
        while(1):
            print("\nTasks (Preprocessing)\U0001F447\n")
            for t in self.tasks:
                print(t)
            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? (Press -1 to exit):  "))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break
            if choice == 1:
                DataDescription(self.data).describe()
            elif choice == 2:
                self.data = Imputation(self.data).imputer()
            elif choice == 3:
                self.data = Categorical(self.data).categoricalMain()
            elif choice == 4:
                self.data = FeatureScaling(self.data).scaling()
            elif choice == 5:
                Download(self.data).download()
            elif choice == -1:
                print(colored("Exiting the Preprocessor CLI...", color="green"))
                exit()
            else:
                print(colored("Invalid Choice. Please try again", attrs=["bold"], color="red"))
if __name__ == "__main__":
    obj = Preprocessor()
    obj.main()



        

