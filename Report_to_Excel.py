#This code was written to aid in exporting text file reports to Excel Files
#it was written using python 3.6 and the only dependancy is Pandas



import pandas as pd

class Report():
    """Make a Report Class to Take Report Generated by ChemStation
        and Return Pandas DataFrame Object"""

    #Initiate the Instance of the Class
    def __init__(self, filename):

        #List of Fatty acids we measure
        falist = ['Sa','Sb','S1','Sc','S2','T1','M1','S3','M2','S4','T2','M3','S5','U3','S6',
                'T3','T4','C2','T5','M6','M7','U12','S7','T6','T7','T8','P1','S8','P2','T10','M10',
                'P3','P4a','P5','S10','P6','P8','S11','P9','P10','S12','M12','P12','P13','P14']
        #Read Text File In
        mf = open(filename, "r")       
        #Object to call for each line
        line = mf.readlines()
        #Clean Data
        clean = []
        self.start = 0
        for i in range(0, len(line)):
            clean.append(line[i].replace("\x00","").strip("\n"))
        print(os.getcwd())
        



        #Get Method Info 
        for i in range(0, 50):
            if "Method Info" in clean[i]:
                self.method_info = clean[i][18:50]

        #If Method Info is NOT a WASH or Un-Integrated get all info for Report Class
        if "A quick iso-octane wash method" not in self.method_info and "Run method for Statler" not in self.method_info:
            #Get each proporty of the class
            for i in range(0, 200):
                if "Injection Date" in clean[i]:
                    self.date = clean[i][18:50].strip(' ')
                if "Signal 1" in clean[i]:
                    self.start = i+10
                if "Sample Name" in clean[i]:
                    self.sample_name = clean[i][13:]
                if "Data File" in clean[i]:
                    self.location = clean[0][-17:]
                if "Operator" in clean[i]:
                    self.operator = clean[i][18:35].strip(' ')
                if "Acq. Instrument" in clean[i]:
                    self.instrument = clean[i][18:35].strip(' ')
                if "Totals" in clean[i]:
                    self.total_pas = clean[i][27:38].strip(' ')#Total area (pA*s)
                    self.total_pct = clean[i][38:48].strip(' ')#Total Percent Area)       




            #Get Block of Data and turn into Pandas Df
            data = []
            for i in range(self.start,self.start+90):
                sm = []
                if i%2 == 0:
                    #peak #
                    sm.append(clean[i][0:5].strip(' '))
                    #ret time
                    sm.append(clean[i][5:13].strip(' '))
                    #width
                    sm.append(clean[i][20:28].strip(' '))
                    #area pas
                    sm.append(clean[i][28:38].strip(' '))
                    #area%
                    sm.append(clean[i][38:48].strip(' '))
                    #name
                    sm.append(clean[i][48:54].strip(' '))
                    #nest small array into data array
                    data.append(sm)
            #convert to pandas dataframe
            data = pd.DataFrame(data)
            #add col names
            my_columns = ["Peak #", "Ret. Time (min)","Width (min)", "Area (pA*s)", "Area%", "Name"]
            data.columns = my_columns
            #data attribute
            self.data = data
            #fatty acid list
            self.falist = falist

            #get only the pct and totals needed
            my_array = data.loc[:,'Area%'].values
            a2 = []
            for i in my_array:
                a2.append(float(i))
            a2.append(0)
            a2.append(float(self.total_pas))
            a2.append(float(self.total_pct))
            df = pd.DataFrame(a2)
            self.template_data = df

        #close the opened file
        mf.close()

#______________________________________________________________________

#______________________________________________________________________

#______________________________________________________________________

#This Function will turn all valid reports from a directory into excel file\
### NOTE REQUIRES REPORT CLASS (*SEE TOP OF PAGE) ###
def mult_to_excel(directory, outfile):
    """Convert Multiple Reports to Single Excel Sheet"""
    #Main Directory
    main_dir = directory
    #List of Files in Main Directory
    files = os.listdir(main_dir)
    #A DataFrame to Store Info
    temp = pd.DataFrame()
    #Loop All ".D" Folders in Main Directory
    for i in files:
        if i[-1:] == "D":
            #Go into ".D" Folder
            os.chdir(main_dir+'/'+str(i))
            #Get all Files in the ".D" Folder
            sub_files = os.listdir(os.getcwd())
            #Go through Each file to find Report.TXT File
            for j in sub_files:
                if j == 'Report.TXT':
                    #Use instance of the Report Class
                    df = Report(j)
                    #Make sure Report is NOT a WASH or Un-intergrated
                    if df.start != 0:
                        #If Report Valid Get its info and update our DataFrame
                        temp[df.sample_name] = df.template_data[0]
    #Make sure Stored as DataFrame Object
    temp = pd.DataFrame(temp)
    #Go to Main Directory To save new File
    os.chdir(main_dir)
    temp.to_csv(outfile, index = False)
    #Return a DataFrame Object
    return temp
#_______________________________________________________________________

#This Function will turn all valid Locations of reports from a directory into excel file
### NOTE REQUIRES REPORT CLASS (*SEE TOP OF PAGE) ###

def locations(directory, outfile):
    #Main Directory
    main_dir = directory
    #List of Files in Main Directory
    files = os.listdir(main_dir)
    #A List to Store Info
    temp = []
    #Loop All ".D" Folders in Main Directory
    for i in files:
        if i[-1:] == "D":
            #Go into ".D" Folder
            os.chdir(main_dir+'/'+str(i))
            #Get all Files in the ".D" Folder
            sub_files = os.listdir(os.getcwd())
            #Go through Each file to find Report.TXT File
            for j in sub_files:
                if j == 'Report.TXT':
                    #Use instance of the Report Class                    
                    df = Report(j)
                    #Make sure Report is NOT a WASH or Un-intergrated
                    if df.start != 0:
                        #If Report Valid Get its info and update our DataFrame                        
                        temp.append(df.location)
    #Make sure Stored as DataFrame Object
    temp = pd.DataFrame(temp)
    #Go to Main Directory To save new File
    os.chdir(main_dir)
    #Save DataFrame to csv
    temp.to_csv(outfile, index = False)
    #return the DataFrame if wanted
    return temp




#_______________________________________________________________________

#_______________________________________________________________________

#_______________________________________________________________________

###Example Use###
import os
path = "C:/Barry's Chromes/Phospholipid Exp/chromes/20181210S-Back-MissLabel"
locations(path, "locations.csv")
mult_to_excel(path,"Reports.csv")




#Advanced Use
falist = ['Sa','Sb','S1','Sc','S2','T1','M1','S3','M2','S4','T2','M3','S5','U3','S6',
                'T3','T4','C2','T5','M6','M7','U12','S7','T6','T7','T8','P1','S8','P2','T10','M10',
                'P3','P4a','P5','S10','P6','P8','S11','P9','P10','S12','M12','P12','P13','P14']
x = mult_to_excel(path, "Reports.csv")
import scipy.stats
y = x.transpose()
z = scipy.stats.zscore(y.iloc[:,:-3])
import matplotlib.pyplot as plt
z = pd.DataFrame(z)
z.columns = falist
z.plot.box(rot = 45, grid = True)
plt.title("Z-Score Boxplots For Run 20181210S-Back")
plt.show()
