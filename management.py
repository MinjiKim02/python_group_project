
from main import Doctor, Facility, Laboratory, Patient


this_doctor = Doctor()
this_facility = Facility()
this_laboratory = Laboratory()
this_patient = Patient()



# Class 5: Management

class Management:
    def DisplayMenu(self):
        option = -1
        while option != 0:
            option = int(input("Welcome to Alberta Hospital (AH) Management system\n"
                               "Select from the following options, or select 0 to stop:\n"
                               "1 - Doctors\n"
                               "2 - Facilities\n"
                               "3 - Laboratories\n"
                               "4 - Patients\n"))
            while option == 1:
                doctorsmenu = int(input("Doctors Menu:\n"
                                        "1 - Display Doctors List\n"
                                        "2 - Search for doctor by ID\n"
                                        "3 - Search for doctor by name\n"
                                        "4 - Add doctor\n"
                                        "5 - Edit doctor info\n"
                                        "6 - Back to the Main Menu\n"))
                if doctorsmenu == 1:
                    this_doctor.displayDoctorsList(self)
                    print("\nBack to the previous Menu")

                elif doctorsmenu == 2:
                    this_doctor.searchById(self)
                    print("\nBack to the previous Menu")

                elif doctorsmenu == 3:
                    this_doctor.searchByName(self)
                    print("\nBack to the previous Menu")

                elif doctorsmenu == 4:
                    this_doctor.enterDrInfo()
                    print("\nBack to the previous Menu")

                elif doctorsmenu == 5:
                    this_doctor.editDoctorInfo(self)
                    print("\nBack to the previous Menu")

                elif doctorsmenu == 6:
                    option = int(input("Welcome to Alberta Hospital (AH) Management system \n"
                                       "Select from the following options, or select 0 to stop:\n"
                                       "1 - Doctors\n"
                                       "2 - Facilities\n"
                                       "3 - Laboratories\n"
                                       "4 - Patients\n"))
            while option == 2:
                facilitiesmenu = int(input("Facilities Menu:\n"
                                           "1 - Display Facilities list\n"
                                           "2 - Add Facility\n"
                                           "3 - Back to the Main Menu\n"))
                if facilitiesmenu == 1:
                    this_facility.displayFacilities()
                    print("\nBack to the previous Menu")

                elif facilitiesmenu == 2:
                    this_facility.addFacility()
                    print("\nBack to the previous Menu")

                elif facilitiesmenu == 3:
                    option = int(input("Welcome to Alberta Hospital (AH) Management system \n"
                                       "Select from the following options, or select 0 to stop:\n"
                                       "1 - Doctors\n"
                                       "2 - Facilities\n"
                                       "3 - Laboratories\n"
                                       "4 - Patients\n"))
            while option == 3:
                laboratoriesmenu = int(input("Laboratories Menu:\n"
                                             "1 - Display laboratories list\n"
                                             "2 - Add laboratory\n"
                                             "3 - Back to the Main Menu\n"))
                if laboratoriesmenu == 1:
                    this_laboratory.displayLabsList()
                    print("\nBack to the previous Menu")

                elif laboratoriesmenu == 2:
                    this_laboratory.addLabToFile()
                    print("\nBack to the previous Menu")

                elif laboratoriesmenu == 3:
                    option = int(input("Welcome to Alberta Hospital (AH) Management system \n"
                                       "Select from the following options, or select 0 to stop:\n"
                                       "1 - Doctors\n"
                                       "2 - Facilities\n"
                                       "3 - Laboratories\n"
                                       "4 - Patients\n"))
            while option == 4:
                patientsmenu = int(input("Patients Menu:\n"
                                         "1 - Display patients list\n"
                                         "2 - Search for patient by ID\n"
                                         "3 - Add patient\n"
                                         "4 - Edit patient info\n"
                                         "5 - Back to the Main Menu\n"))
                if patientsmenu == 1:
                    this_patient.displayPatientInfo()
                    print("\nBack to the previous Menu")

                elif patientsmenu == 2:
                    this_patient.searchPatientByID()
                    print("\nBack to the previous Menu")

                elif patientsmenu == 3:
                    this_patient.addPatientToFile()
                    print("\nBack to the previous Menu")

                elif patientsmenu == 4:
                    this_patient.editPatientInfo()
                    print("\nBack to the previous Menu")

                elif patientsmenu == 5:
                    option = int(input("Welcome to Alberta Hospital (AH) Management system \n"
                                       "Select from the following options, or select 0 to stop:\n"
                                       "1 - Doctors\n"
                                       "2 - Facilities\n"
                                       "3 - Laboratories\n"
                                       "4 - Patients\n"))

this_management = Management()
this_management.DisplayMenu()

