import csv

class Client: # a class to of client, used to save all the data.

    def __init__(self, id, age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed, Output):
        self.id = id                         # 0
        self.age = age                       # 1
        self.job = job                       # 2
        self.marital = marital               # 3
        self.education = education           # 4
        self.default = default               # 5
        self.housing = housing               # 6
        self.loan = loan                     # 7
        self.contact = contact               # 8
        self.month = month                   # 9
        self.day_of_week = day_of_week       # 10
        self.duration = duration             # 11
        self.campaign = campaign             # 12
        self.pdays = pdays                   # 13
        self.previous = previous             # 14
        self.poutcome = poutcome             # 15
        self.emp_var_rate = emp_var_rate     # 16
        self.cons_price_idx = cons_price_idx # 17
        self.cons_conf_idx = cons_conf_idx   # 18
        self.euribor3m = euribor3m           # 19
        self.nr_employed = nr_employed       # 20
        self.Output = Output                 # 21

    def displayClient(self):
        print self.id, self.age, self.job, self.marital, self.education, self.default, self.housing, self.loan, self.contact, self.month, self.day_of_week, self.duration, self.campaign, self.pdays, self.previous, self.poutcome, self.emp_var_rate, self.cons_price_idx, self.cons_conf_idx, self.euribor3m, self.nr_employed, self.Output

client_list = [];  # a list, type of this list is Class Client, used to save all the information of all clients

csvFile = open("train.csv", "r")
reader = csv.reader(csvFile)
for item in reader:
    client_temp = Client(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14],item[15],item[16],item[17],item[18],item[19],item[20],item[21])
    #  client_temp.displayClient()  #  for test
    client_list.append(client_temp)
csvFile.close()

# print len(client_list) # for test