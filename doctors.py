# Class 1 : Doctor

class Doctor:

    def __init__(self):
        self.id = ""
        self.name = ""
        self.specialist = ""
        self.time = ""
        self.qualification = ""
        self.roomNumber = ""

    def formatDrInfo(self, formatted):
        self.formatted = '_'.join(formatted)
        return self.formatted +  '\n'

    def enterDrInfo(self):
        self.id = input("Enter doctor ID: ")
        self.name = input("Enter doctor Name: ")
        self.specialist = input("Enter doctor Specialist: ")
        self.time = input("Enter doctor Time: ")
        self.qualification = input("Enter doctor Qualification: ")
        self.roomNumber = input("Enter doctor Room Number: ")
        return [self.id, self.name, self.specialist, self.time, self.qualification, self.roomNumber]


    def readDoctorsFile(self):
            self.file = open("doctors.txt", "r")
            self.list = self.file.readlines()
            self.file.close()
            return self.list

    def searchById(self, id):
        self.doctor_list = self.readDoctorsFile()
        self.n_list = []

        for n in range(len(self.doctor_list)):
            self.n_list.append([])
            self.n_list[n] = self.doctor_list[n].split("_")

        self.ask = input("\n Enter the doctors ID:\n\n")

        self.possibility = False
        for n in range(len(self.n_list)):
            if self.n_list[n][0] == self.ask:
                self.displayDoctorInfo(self.n_list[n])
                self.possibility = True
        if self.possibility == False:
            print("Cannot find doctor with that ID, try again")

    def searchByName(self, name):
        # Search for a doctor with the specified Name
        self.doctor_list = self.readDoctorsFile()
        self.n_list = []
        for n in range(len(self.doctor_list)):
            self.n_list.append([])
            self.n_list[n] = self.doctor_list[n].split("_")

        self.ask = input("\n Enter the doctor name:\n\n")

        self.possibility = False
        for n in range(len(self.n_list)):
            if self.n_list[n][1] == self.ask:
                self.displayDoctorInfo(self.n_list[n])
                self.possibility = True
        if self.possibility == False:
            print("Can't find the doctor with the same name on the system")

    def displayDoctorInfo(self, doctor_list):
        self.doctor_list = doctor_list
        self.doctor_list[4] = self.doctor_list[4].upper()  # capitalizes qualifications due to file inconsistancy
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Time': <15}{'Qualification': <15}{'Room Number': <0}" + '\n')
        print(f"{self.doctor_list[0]: <5}{self.doctor_list[1]: <20}{self.doctor_list[2]: <15}{self.doctor_list[3]: <15}{self.doctor_list[4]: <15}{self.doctor_list[5]: <0}")

    def editDoctorInfo(self, doctor_list):
        self.doctor_list = self.readDoctorsFile()
        self.n_list = []
        for n in range(len(self.doctor_list)):
            self.n_list.append([])
            self.n_list[n] = self.doctor_list[n].split("_")

        self.ask = input("Please enter the id of the doctor that you want to edit their information:\n\n")

        self.possibility = False
        for n in range(len(self.n_list)):
            if self.n_list[n][0] == self.ask:
                self.n_list[n][1] = input("\nEnter new Name:\n\n")
                self.n_list[n][2] = input("\nEnter new Specialist in:\n\n")
                self.n_list[n][3] = input("\nEnter new Time slot: \n\n")
                self.n_list[n][4] = input("\nEnter new Qualification: \n\n")
                self.n_list[n][5] = input("\nEnter new Room number:\n\n")
                self.doctor_list[n] = self.formatDrInfo(self.n_list[n])
                self.writeListOfDoctorsToFile(self.doctor_list)
                self.possibility = True
        if self.possibility == False:
            print("Can't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self, doctor_list):
        self.doctor_list = self.readDoctorsFile()
        self.n_list = []

        for n in range(len(self.doctor_list)):
            self.n_list.append([])
            self.n_list[n] = self.doctor_list[n].split("_")

        del self.n_list[0]

        print(
            f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}" + '\n')
        for n in range(len(self.n_list)):
            print(
                f"{self.n_list[n][0]: <5}{self.n_list[n][1]: <20}{self.n_list[n][2]: <15}{(self.n_list[n][3].lower()): <15}{(self.n_list[n][4].upper()): <15}{self.n_list[n][5]: <0}")
    def writeListOfDoctorsToFile(self, doctor_list):
        self.file = open("doctors.txt", "w")
        self.main = 0
        for entries in doctor_list:
            self.file.write(doctor_list[self.main])
            self.main += 1
        self.file.close()

    def addDrToFile(self, doctor, filename):
        with open("doctors.txt", "a") as f:
            f.write(doctor['Id'] + "," + doctor['Name'] + "," + doctor['Specialist'] + "," + doctor['Time'] + "," + doctor[
                        'Qualification'] + "," + doctor['RoomNumber'] + "\n")
            f.close()

        self.doctor_list.append(self.doctor_to_add)
        self.writeListOfDoctorsToFile(self.doctor_list)
