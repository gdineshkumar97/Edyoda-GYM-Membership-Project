import time
class Gym:
    list_of_members = {}
    regimen = {}
    member_login_details = {}
    list_of_regimen = {(0.00, 18.49): {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Rest', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Rest','Sun': 'Rest'},(18.50, 24.99): {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps','Sat': 'Legs', 'Sun': 'Rest'},(25.00, 29.99): {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps','Sat': 'Legs', 'Sun': 'Cardio'},(30.00, 50.00): {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio', 'Thu': 'Back', 'Fri': 'Triceps','Sat': 'Cardio', 'Sun': 'Cardio'}}

    def admin_home(self):
        self.start_action = input("Press 1 --> Super user \nPress 2 --> Gym Member\n")
        if self.start_action == '1':
            self.ad_action = input('Press 1 --> Sign Up \nPress 2 --> Log in\n')
            if self.ad_action == '1':
                self.new_admin()
            elif self.ad_action == '2':
                self.login_admin()
            else:
                print('Invalid Input')
                self.admin_home()
        elif self.start_action == '2':
            self.member_login()
        else:
            print('Invalid Input')
            self.admin_home()
    def member_login(self):
        print('User Login Page!')
        self.phn_no = input("Enter Phone Number->")
        self.password = input("Enter Password->")
        if self.phn_no in Gym.list_of_members:
            if self.password in Gym.member_login_details[self.phn_no]:
                print("User Logged in Successfully")
                self.member_log_in = True
                self.main_menu()
            else:
                print("Incorrect credentials")
                self.member_log_in = False
                self.member_login()
        else:
            print('User not signed up')
            self.admin_home()

    def main_menu(self):
        print('*******************************Main Menu*******************************')
        self.main_action = input("Press 1 --> My Regimen \nPress 2 --> My Profile \nPress 0 --> Log Out\n")
        if self.main_action == "1":
            self.my_regimen()

        elif self.main_action == "2":
            self.my_profile()

        elif self.main_action == '0':
            self.member_logout()

        else:
            print("Input not matching. Please Try again.")
            self.main_menu()

    def my_regimen(self):

        print('Your Regimen')

        for key in Gym.regimen[self.phn_no]:
            print(key, ':', Gym.regimen[self.phn_no][key])

        self.ac = input("Press 0 --> Main Menu->")
        if self.ac == '0':
            self.main_menu()
        else:
            print('Invalid Input')
            self.main_menu()

    def my_profile(self):

        print("Your Profile")

        for key in Gym.list_of_members[self.phn_no]:
            print(key, ":", Gym.list_of_members[self.phn_no][key])
        self.ac = input("Press 0 --> Main Menu->")
        if self.ac == '0':
            self.main_menu()
        else:
            print('Invalid Input')
            self.main_menu()

    def member_logout(self):

        self.member_log_in = False
        print("Member logged out.")
        print('Please wait loading...')
        time.sleep(1)
        self.admin_home()
#==========================================================================================================================


class admin(Gym):

    list_of_admins = {}
    login_admin = []

    def __init__(self):
        print("Dinesh's Gym Welcomes You")
        self.admin_home()

    def new_admin(self):
        print('Admin Sign Up page')

        self.username = input("Enter Username->")
        self.password = input("Enter Password->")

        if self.username in admin.list_of_admins:

            print("The username is already taken. Please try again with new combination...")
            self.new_admin()

        else:

            admin.list_of_admins[self.username] = [self.password]
            print("New admin added..")
            print("Redirecting to login page..")
            time.sleep(1)
            self.login_admin()

    def login_admin(self):
        # Admin Log in
        self.username = input("Enter Username->")
        self.password = input("Enter Password->")

        if self.username in admin.list_of_admins:

            if self.password in admin.list_of_admins[self.username]:

                print("Logged in...")
                self.admin_log_in = True
                self.admin_mainmenu()

            else:

                print("Incorrect credentials")
                self.admin_log_in = False
                self.login_admin()

        else:

            print('Admin not signed in')
            time.sleep(1)
            print('Redirecting to sign up page...')
            self.new_admin()

    def admin_mainmenu(self):

        print(
            '****************************************************************************************************************************')
        self.main_menu_action = input(
            'Press 1 --> Create Member \nPress 2 --> View Member \nPress 3 --> Delete Member \nPress 4 --> Update Member \nPress 5 --> Regimen \nPress 0 --> Logout\n')

        if self.main_menu_action == '1':
            self.add_member()

        elif self.main_menu_action == '2':
            self.view_member()

        elif self.main_menu_action == '3':
            self.delete_member()

        elif self.main_menu_action == '4':
            self.update_member()

        elif self.main_menu_action == '5':
            self.regimen_menu()

        elif self.main_menu_action == '0':
            self.admin_logout()

        else:
            print('Invalid Input')
            self.admin_mainmenu()

    def add_member(self):

        try:
            if self.admin_log_in == True:

                self.name = input("Enter Full Name->")
                self.age = input("Enter Age->")
                while True:
                    self.gender = input("Enter Gender (M/F/O):")
                    if self.gender == "M" or self.gender == "F" or self.gender == "O":
                        self.phn_no = input("Enter Contact No->")

                        while True:
                            self.email = input("Enter Email ID->")
                            if '@' in self.email and '.com' in self.email:
                                self.password = input("Enter Password->")

                                while True:
                                    self.confirm_password = input("Enter Confirm Password->")
                                    if self.confirm_password == self.password:

                                        Gym.member_login_details[self.phn_no] = self.password

                                        l = self.bmi_calculator()

                                        while True:
                                            self.membership = input(
                                                'Select Applicable Membership (in months): \n-> 1\n-> 3\n-> 6\n-> 12\n')
                                            if self.membership in ['1', '3', '6', '12']:

                                                Gym.list_of_members[self.phn_no] = {"Name": self.name,
                                                                                       "Age": self.age,
                                                                                       "Gender": self.gender,
                                                                                       "Phone Number": self.phn_no,
                                                                                       "Email Address": self.email,
                                                                                       "BMI": l[0],
                                                                                       "Membership Duration (in months)": self.membership}
                                                Gym.regimen[self.phn_no] = l[1]

                                                print("New member successfully added.")
                                                break
                                            else:
                                                print('Option not Available')

                                        self.temp_action = input("Press 1 --> Enter New Member \nPress 0 --> Main Menu\n")
                                        if self.temp_action == '1':
                                            self.add_member()
                                        elif self.temp_action == '0':
                                            self.admin_mainmenu()
                                        else:
                                            print('Invalid Input')
                                            print('Please wait loading...')
                                            time.sleep(1)
                                            self.admin_mainmenu()
                                        break

                                    else:
                                        print('Password does not match. ')
                            else:
                                print('Enter valid email id-->')
                    else:
                        print('Enter Input between given Options.')

        except AttributeError:
            print('Admin not logged in')

    def view_member(self):

        try:
            if self.admin_log_in == True:

                self.phn_no = input('Enter Phone Number of the Member->')

                if self.phn_no in Gym.list_of_members:

                    for key in Gym.list_of_members[self.phn_no]:
                        print(key, ':', Gym.list_of_members[self.phn_no][key])

                    print("Regimen")
                    for key in Gym.regimen[self.phn_no]:
                        print(key, ':', Gym.regimen[self.phn_no][key])
                    print(
                        '****************************************************************************************************************************')
                    self.temp_action = input("Press 1 --> View Another Member \nPress 0 --> Main Menu\n")
                    if self.temp_action == '1':
                        self.view_member()
                    elif self.temp_action == '0':
                        self.admin_mainmenu()
                    else:
                        print('Invalid Input')
                        print('Please wait loading...')
                        time.sleep(1)
                        self.admin_mainmenu()
                else:
                    print('Phone Number not present in system.')
                    self.admin_mainmenu()

        except AttributeError:
            print('Admin not logged in')

    def delete_member(self):

        try:
            if self.admin_log_in == True:

                self.phn_no = input('Enter Phone Number of the Member->')

                if self.phn_no in Gym.list_of_members:
                    del Gym.list_of_members[self.phn_no]
                    del Gym.regimen[self.phn_no]
                    del Gym.member_login_details[self.phn_no]
                    print('Deleting Info...')
                    time.sleep(1)
                    print('Member Information Successfully Deleted from System')
                    self.temp_action = input("Press 1 --> Delete Another Member \nPress 0 --> Main Menu\n")
                    if self.temp_action == '1':
                        self.delete_member()
                    elif self.temp_action == '0':
                        self.admin_mainmenu()
                    else:
                        print('Invalid Input')
                        print('Please wait loading...')
                        time.sleep(1)
                        self.admin_mainmenu()

                else:
                    print('Incorrect Phone Number.')
                    self.admin_mainmenu()

        except AttributeError:
            print('Admin not logged in')

    def update_member(self):

        try:
            if self.admin_log_in == True:

                self.phn_no = input('Enter Phone Number of the Member->')
                if self.phn_no in Gym.list_of_members:

                    self.update_action = input(
                        "Press 1 --> Update Name \nPress 2 --> Update Age  \nPress 3 --> Update Email \nPress 4 --> Update Password \nPress 5 --> Update Membership \nPress 0 --> Return to Main Menu \n")

                    if self.update_action == '1':
                        self.new_name = input("Enter New Name->")
                        Gym.list_of_members[self.phn_no]["Name"] = self.new_name
                        print("Name Updated Successfully")
                        self.admin_mainmenu()

                    if self.update_action == '2':
                        self.new_age = input("Enter Age->")
                        Gym.list_of_members[self.phn_no]["Age"] = self.new_age
                        print("Age Updated Successfully")
                        self.admin_mainmenu()

                    if self.update_action == '3':
                        self.new_email = input('Enter New Email->')
                        if self.new_email == self.email:
                            print("New email cannot be same as existing email")
                            self.update_profile()
                        else:
                            Gym.list_of_members[self.phn_no] = self.new_email
                            print("Email Updated Successfully")
                            self.admin_mainmenu()

                    if self.update_action == '4':
                        self.new_password = input('Enter New Password->')
                        if self.new_password == self.password:
                            print("New Password cannot be same as existing Password")
                            self.update_profile()
                        else:
                            while True:
                                self.new_cnf_password = input('Confirm Password->')
                                if self.new_cnf_password == self.new_password:

                                    Gym.member_login_details[self.phn_no] = self.new_password
                                    print("Password Changed Successfully")
                                    self.admin_mainmenu()

                                else:
                                    print('Password does not match.')

                    if self.update_action == '5':
                        self.new_membership = input("Press 1 --> Extend Membership: \nPress 2 --> Revoke Membership \n ")
                        if self.new_membership == '1':

                            self.extend_action = input(
                                "Select Applicable Membership (in months): \n-> 1\n-> 3\n-> 6\n-> 12\n")

                            Gym.list_of_members[self.phn_no]['Membership Duration (in months)'] = self.extend_action

                            print('Membership Updated Successfully')
                            self.admin_mainmenu()

                        elif self.new_membership == '2':

                            self.revoke_input = input(
                                'Do you also want to delete the data of the member? \nPress (Y/y) --> Yes \nPress (N/n) --> No \n ')

                            if self.revoke_input == "y" or self.revoke_input == 'Y':
                                self.delete_member()

                            elif self.revoke_input == "n" or self.revoke_input == 'N':
                                Gym.list_of_members[self.phn_no]['Membership Duration (in months)'] = 'expired'
                                print('Membership Revoked.')
                                self.admin_mainmenu()

                            else:
                                print('Invalid Input')
                                self.admin_mainmenu()

                    if self.update_action == '0':
                        self.admin_mainmenu()

                else:
                    print('Phone number not found.')
                    self.admin_mainmenu()


        except AttributeError:
            print('Admin not logged in')

    def bmi_calculator(self):

        time.sleep(1)
        self.height_input = float(input('Enter Height(centimetres)->'))
        self.weight_input = float(input('Enter Weight(kilograms)->'))
        print('Calculating BMI....')
        time.sleep(1)

        self.height_in_metre = self.height_input / 100
        self.bmi = round(self.weight_input / self.height_in_metre ** 2, 1)

        print('Your BMI is->', self.bmi)
        for i in Gym.list_of_regimen:
            if i[0] <= self.bmi <= i[1]:

                print('Regimen Suitable to your BMI->')
                for key in Gym.list_of_regimen[i]:
                    print(key, ':', Gym.list_of_regimen[i][key])

            return [self.bmi, Gym.list_of_regimen[i]]

    def regimen_menu(self):

        try:
            if self.admin_log_in == True:
                print(
                    '****************************************************************************************************************************')
                self.regimen_menu_action = input(
                    'Press 1 --> Create Regimen \nPress 2 --> View Regimen \nPress 3 --> Delete Regimen \nPress 4 --> Update Regimen \nPress 0 --> Esc to Previous Menu\n')

                if self.regimen_menu_action == '1':
                    self.create_regimen()

                if self.regimen_menu_action == '2':
                    self.view_regimen()

                if self.regimen_menu_action == '3':
                    self.delete_regimen()

                if self.regimen_menu_action == '4':
                    self.update_regimen()

                if self.regimen_menu_action == '0':
                    self.admin_mainmenu()


        except AttributeError:
            print('Admin not logged in')

    def create_regimen(self):

        list_of_bmi = []
        self.start = float(input('BMI Initial Value->'))
        self.end = float(input('BMI Final Value->'))

        new_range = (self.start, self.end)

        for i in Gym.list_of_regimen:
            list_of_bmi.append(i)
            list_of_bmi.sort()

        max_end = 0
        found = 0

        for i in list_of_bmi:
            max_end = max(max_end, i[1])

        for i in range(len(list_of_bmi) - 1):

            if new_range[0] > list_of_bmi[i][1] and new_range[1] < list_of_bmi[i + 1][0]:

                Gym.list_of_regimen[new_range] = {'Mon': 'None', 'Tue': 'None', 'Wed': 'None', "Thu": 'None',
                                                     'Fri': 'None', 'Sat': 'None', 'Sun': 'None'}

                mon_input = input("Monday:>")
                Gym.list_of_regimen[new_range]['Mon'] = mon_input
                tue_input = input("Tuesday:>")
                Gym.list_of_regimen[new_range]['Tue'] = tue_input
                wed_input = input("Wednesday:>")
                Gym.list_of_regimen[new_range]['Wed'] = wed_input
                thu_input = input("Thursday:>")
                Gym.list_of_regimen[new_range]['Thu'] = thu_input
                fri_input = input("Friday:>")
                Gym.list_of_regimen[new_range]['Fri'] = fri_input
                sat_input = input("Saturday:>")
                Gym.list_of_regimen[new_range]['Sat'] = sat_input
                sun_input = input("Sunday:>")
                Gym.list_of_regimen[new_range]['Sun'] = sun_input

                print('New Regimen Added.')

                for key in Gym.list_of_regimen[new_range]:
                    print(key, ':', Gym.list_of_regimen[new_range][key])
                found = 1

                break

        if new_range[0] > max_end and found == 0:

            Gym.list_of_regimen[new_range] = {'Mon': 'None', 'Tue': 'None', 'Wed': 'None', "Thu": 'None',
                                                 'Fri': 'None', 'Sat': 'None', 'Sun': 'None'}

            mon_input = input("Monday:>")
            Gym.list_of_regimen[new_range]['Mon'] = mon_input
            tue_input = input("Tuesday:>")
            Gym.list_of_regimen[new_range]['Tue'] = tue_input
            wed_input = input("Wednesday:>")
            Gym.list_of_regimen[new_range]['Wed'] = wed_input
            thu_input = input("Thursday:>")
            Gym.list_of_regimen[new_range]['Thu'] = thu_input
            fri_input = input("Friday:>")
            Gym.list_of_regimen[new_range]['Fri'] = fri_input
            sat_input = input("Saturday:>")
            Gym.list_of_regimen[new_range]['Sat'] = sat_input
            sun_input = input("Sunday:>")
            Gym.list_of_regimen[new_range]['Sun'] = sun_input

            print('New Regimen Added.')

            for key in Gym.list_of_regimen[new_range]:
                print(key, ':', Gym.list_of_regimen[new_range][key])

            found = 1

        if found == 0:
            print('Range not Available')
        self.temp_action = input("Press 1 --> Create Another Regimen \nPress 0 --> Previous Menu\n")
        if self.temp_action == '1':
            self.create_regimen()
        elif self.temp_action == '0':
            self.regimen_menu()
        else:
            print('Invalid Input')
            print('Please wait loading...')
            time.sleep(1)
            self.admin_mainmenu()

    def view_regimen(self):
        try:
            if self.admin_log_in == True:

                #View Regimen
                self.v_reg = input('Press 1 --> Enter BMI \nPress 2 --> View All Regimens \nPress 0 --> Previous Menu \n')
                if self.v_reg == '1':

                    found = 0
                    self.bmi_input = float(input('Enter BMI->'))
                    for i in Gym.list_of_regimen:

                        if self.bmi_input >= i[0] and self.bmi_input <= i[1]:

                            for key in Gym.list_of_regimen[i]:
                                print(key, ':', Gym.list_of_regimen[i][key])
                            found = 1

                            inp = input('Press 0 --> Previous Menu->')
                            if inp == '0':
                                self.regimen_menu()
                            else:
                                print('Invalid Input')
                                self.admin_mainmenu()

                    if found == 0:
                        print('BMI range not found')
                        self.view_regimen()

                elif self.v_reg == '2':

                    for i in Gym.list_of_regimen:
                        print(i)
                        for j in Gym.list_of_regimen[i]:
                            print(j, ':', Gym.list_of_regimen[i][j])
                    inp = input('Press 0 --> Previous Menu->')
                    if inp == '0':
                        self.regimen_menu()
                    else:
                        print('Invalid Input')
                        self.admin_mainmenu()

                elif self.v_reg == '0':
                    self.regimen_menu()

                else:
                    print('Invalid Input')
                    self.admin_mainmenu()


        except AttributeError:
            print('Admin not logged in')

    def delete_regimen(self):
        try:
            if self.admin_log_in == True:

                start, end = float(input('Enter start BMI range->')), float(input('Enter end BMI range->'))

                l = [start, end]
                t = tuple(l)

                if t in Gym.list_of_regimen:
                    Gym.list_of_regimen.pop(t)
                    print('Regimen Deleted')

                    inp = input('Press 0 --> Previous Menu->')
                    if inp == '0':
                        self.regimen_menu()
                    else:
                        print('Invalid Input')
                        self.admin_mainmenu()
                else:
                    print('BMI range not matched')
                    self.regimen_menu()


        except AttributeError:
            print('Admin not logged in')

    def update_regimen(self):

        try:
            if self.admin_log_in == True:

                print('Update Regimen')
                start, end = float(input('Enter start BMI range->')), float(input('Enter end BMI range->'))

                l = [start, end]
                t = tuple(l)

                if t in Gym.list_of_regimen:
                    self.mon_input = input('Monday:>')
                    Gym.list_of_regimen[t]['Mon'] = self.mon_input
                    self.tue_input = input('Tuesday:>')
                    Gym.list_of_regimen[t]['Tue'] = self.tue_input
                    self.wed_input = input('Wednesday:>')
                    Gym.list_of_regimen[t]['Wed'] = self.wed_input
                    self.thu_input = input('Thursday:>')
                    Gym.list_of_regimen[t]['Thu'] = self.thu_input
                    self.fri_input = input('Friday:>')
                    Gym.list_of_regimen[t]['Fri'] = self.fri_input
                    self.sat_input = input('Saturday:>')
                    Gym.list_of_regimen[t]['Sat'] = self.sat_input
                    self.sun_input = input('Sunday:>')
                    Gym.list_of_regimen[t]['Sun'] = self.sun_input

                    print('Regimen Updated')
                    for i in Gym.list_of_regimen[t]:
                        print(i, ':', Gym.list_of_regimen[t][i])

                    inp = input('Press 0 --> Previous Menu->')
                    if inp == '0':
                        self.regimen_menu()
                    else:
                        print('Invalid Input')
                        self.admin_mainmenu()

        except AttributeError:
            print('Admin not logged in')

    def admin_logout(self):

        self.admin_log_in = False
        print("Admin logged out.")
        print('Please wait loading...')
        time.sleep(1)
        self.admin_home()


dinesh = admin()