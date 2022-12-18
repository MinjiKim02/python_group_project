
# Class 2 : Facility

fileFacilities = 'facilities.txt'

class Facility:
    def __init__(self, facilityName=''):
        if facilityName != '':
            self.facilityName = facilityName

    # read facilities file
    def readFacilitiesFile(self):
        file = open(fileFacilities, 'r')  # read = 'r'
        facilities_list = []
        for lines in file:
            facilities_list.append(lines.rstrip().split('_'))
        file.close()
        return facilities_list


    # adds and writes the facility to the file
    def addFacility(self):
        facilities_list = self.readFacilitiesFile()
        facility_add = input("Enter Facility name: \n")
        facilities_file = open(fileFacilities, 'a')  # add = 'a'
        facilities_file.write(facility_add)
        facilities_file.close()
        self.writeListOfFacilitiesToFile(facilities_list)



    # displays the list of facilities
    def displayFacilities(self):
        facilities_list = self.readFacilitiesFile()
        for lines in facilities_list:
            formatted = ''.join(lines)
            print(formatted)


    # writes the facilities list to facilities.txt
    def writeListOfFacilitiesToFile(self, facilities_list):
        facilities_list = self.readFacilitiesFile()
        facilities_file = open(fileFacilities, 'w')  # write = 'w'
        for lines in facilities_list:
            formatted = ''.join(lines)
            facilities_file.write(formatted)
            facilities_file.write('\n')
        facilities_file.close()

# Class 3 : Laboratory

fileLaboratories = 'laboratories.txt'
listLaboratories = []
class Laboratory:

    # laboratory class constructor
    def __init__(self, lab_name='', cost=''):
        if lab_name != '':
            self.lab_name = lab_name
        if cost != '':
            self.cost = cost

    # adds and writes the lab name to the file in the format of the data that is in the file
    def addLabToFile(self):
        listLaboratories = self.readLaboratoriesFile()
        self.writeListOfLabsToFile(listLaboratories)
        lab_to_add = self.enterLaboratoryInfo()
        laboratories_file = open(fileLaboratories, 'a')
        laboratories_file.write(self.formatLabInfo(lab_to_add))
        laboratories_file.write('\n')
        laboratories_file.close()

    # writes the list of labs into the file laboratories.txt
    def writeListOfLabsToFile(self, listLaboratories):
        laboratories_file = open(fileLaboratories, 'w')
        for each_line in listLaboratories:
            line = self.formatLabInfo(each_line)
            laboratories_file.write(line)
            laboratories_file.write('\n')
        laboratories_file.close()

    # displays the list of laboratories
    def displayLabsList(self):
        listLaboratories = self.readLaboratoriesFile()
        total_rows = len(listLaboratories)
        current_row = 0
        while current_row < total_rows:
            print(
                f'{listLaboratories[current_row][0]:<12}' + listLaboratories[current_row][1])
            current_row += 1

    # formats the Laboratory object similar to the laboratories.txt file
    def formatLabInfo(self, txt_format):
        formatted = '_'.join(txt_format)
        return formatted

    # asks the user to enter lab name and cost and forms a Laboratory object
    def enterLaboratoryInfo(self):
        self.lab_name = input("Enter Laboratory facility:\n")
        self.cost = int(input("Enter Laboratory cost:\n"))
        return [self.lab_name, str(self.cost)]

    # reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def readLaboratoriesFile(self):
        file = open(fileLaboratories, 'r')
        listLaboratories = []
        for each_line in file:
            listLaboratories.append(each_line.rstrip().split('_'))
        file.close()
        return listLaboratories



# Class 4 : Patient

filePatients = 'patients.txt'


class Patient:
    def __init__(self, pid=-1, name='', disease='', gender='', age=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if disease != '':
            self.disease = disease
        if gender != '':
            self.gender = gender
        if age != -1:
            self.age = age

    # formats patient information to be added to the file
    def formatPatientInfo(self, txt_format):
        # print("formats patient information to be added to the file")
        formatted = '_'.join(txt_format)
        return formatted

    # asks the user to enter the patient info
    def enterPatientInfo(self):
        self.pid = int(input("Enter patients’s ID: \n"))
        self.name = input("Enter patient’s name: \n")
        self.disease = input("Enter patient's disease: \n")
        self.gender = input("Enter patient's gender: \n")
        self.age = int(input("Enter patient's age: \n"))
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]


    # reads from file patients.txt
    def readPatientsFile(self):
        # print("reads from file patients.txt")
        file = open(filePatients, 'r')
        listPatients = []
        for each_line in file:
            listPatients.append(each_line.rstrip().split('_'))
        file.close()
        return listPatients

    # searches for a patient using their ID
    def searchPatientByID(self):
        # print("searches for a patient using their ID")
        id_number = int(input("Enter the Patient's ID: \n"))
        listPatients = self.readPatientsFile()
        total_rows = len(listPatients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        while current_row < total_rows:
            if str(id_number) == listPatients[current_row][0]:
                print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
                print(f'{listPatients[current_row][0]:<10}' +
                      f'{listPatients[current_row][1]:<15}' +
                      f'{listPatients[current_row][2]:<15}' +
                      f'{listPatients[current_row][3]:<15}' +
                      listPatients[current_row][4])
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system")
            current_row += 1



    # Asks the user to edit patient information
    def editPatientInfo(self):
        id_number = int(input("Please enter the id of the patient that you want to edit their information: \n"))
        self.pid = id_number
        listPatients = self.readPatientsFile()
        total_rows = len(listPatients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        self.name = input("Enter new Name: \n")
        self.disease = input("Enter new disease: \n")
        self.gender = input("Enter new gender: \n")
        self.age = int(input("Enter new age: \n"))

        while current_row < total_rows:
            if str(id_number) == listPatients[current_row][0]:
                listPatients[current_row][1] = self.name
                listPatients[current_row][2] = self.disease
                listPatients[current_row][3] = self.gender
                listPatients[current_row][4] = str(self.age)
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same ID on the system")
            current_row += 1
        self.writeListOfPatientsToFile(listPatients)

    # displays patient info
    def displayPatientInfo(self):
        listPatients = self.readPatientsFile()
        total_rows = len(listPatients)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
        while current_row < total_rows:
            print(
                f'{listPatients[current_row][0]:<10}' +
                f'{listPatients[current_row][1]:<15}' +
                f'{listPatients[current_row][2]:<15}' +
                f'{listPatients[current_row][3]:<15}' +
                listPatients[current_row][4])
            current_row += 1

    # writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self, listPatients):
        patients_file = open(filePatients, 'w')
        for each_line in listPatients:
            add_line = self.formatPatientInfo(each_line)
            patients_file.write(add_line)
            patients_file.write('\n')
        patients_file.close()

    # adds a new patient into the patients.txt file
    def addPatientToFile(self):
        listPatients = self.readPatientsFile()
        self.writeListOfPatientsToFile(listPatients)
        patient_to_add = self.enterPatientInfo()
        patients_file = open(filePatients, 'a')
        patients_file.write(self.formatPatientInfo(patient_to_add))
        patients_file.write('\n')
        patients_file.close()

