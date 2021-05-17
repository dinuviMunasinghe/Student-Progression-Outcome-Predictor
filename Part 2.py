pass_credit = 0
defer_credit = 0
fail_credit = 0
credit_list = [0, 20, 40, 60, 80, 100, 120]
no_students_progressed = 0
no_students_trailing = 0
no_students_excluded = 0
no_students_retriever = 0
count = 0


def rangecheck(credit):
    if credit not in credit_list:
        checked = "Range Error"
        return checked


def creating_histogram(no_students_progressed, no_students_trailing, no_students_retriever,
                       no_students_excluded):  # defining the function that creates the horizintal histogram
    print("Progress", no_students_progressed, ":", "*" * no_students_progressed)
    print("Trailing", no_students_trailing, ":", "*" * no_students_trailing)
    print("Retriever", no_students_retriever, ":", "*" * no_students_retriever)
    print("Excluded", no_students_excluded, ":", "*" * no_students_excluded)
    print(count, "outcomes in total")


while (pass_credit != 'q') or (defer_credit != 'q') or (fail_credit != 'q'):
    try:
        pass_credit = int(input(
            'Enter the number of credits at pass.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
        while rangecheck(pass_credit) == "Range Error":
            print("Range Error")
            print("please re-eneter as there is a range error")
            pass_credit = int(input('Enter the number of credits at pass.'))

        defer_credit = int(input(
            'Enter the number of credits at defer.'))  # until the user enters  valid data to defer_credit it keeps on asking the user to input
        while rangecheck(defer_credit) == "Range Error":
            print("Range Error")
            print("please re-eneter as there is a range error")
            defer_credit = int(input('Enter the number of credits at defer.'))

        fail_credit = int(input(
            'Enter the number of credits at fail.'))  # until the user enters  valid data to fail_credit it keeps on asking the user to input
        while rangecheck(fail_credit) == "Range Error":
            print("Range Error")
            print("please re-eneter as there is a range error")
            defer_credit = int(input('Enter the number of credits at fail.'))

        total_credits = pass_credit + defer_credit + fail_credit

        while total_credits != 120:
            print('Total incorrect')

            pass_credit = int(input(
                'Enter the number of credits at pass.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
            while rangecheck(pass_credit) == "Range Error":
                print("Range Error")
                print("please re-eneter as there is a range error")
                pass_credit = int(input('Enter the number of credits at pass.'))

            defer_credit = int(input(
                'Enter the number of credits at defer.'))  # until the user enters  valid data to defer_credit it keeps on asking the user to input
            while rangecheck(defer_credit) == "Range Error":
                print("Range Error")
                print("please re-eneter as there is a range error")
                defer_credit = int(input('Enter the number of credits at defer.'))

            fail_credit = int(input(
                'Enter the number of credits at fail.'))  # until the user enters  valid data to fail_credit it keeps on asking the user to input
            while rangecheck(fail_credit) == "Range Error":
                print("Range Error")
                print("please re-eneter as there is a range error")
                fail_credit = int(input('Enter the number of credits at fail.'))

            total_credits = pass_credit + defer_credit + fail_credit


        else:
            if pass_credit == 120:  # checking if the student have been progressed
                print('Progress')
                no_students_progressed = no_students_progressed + 1  # if so incrementing the variable that holds the number of students that have been progressed
            elif pass_credit == 100:  # checking if the student have been trailing
                print('Progress-module trailer')
                no_students_trailing = no_students_trailing + 1  # if so incrementing the variable that holds the number of students that have been trailing
            elif fail_credit >= 80:  # checking if the student have been excluded
                print('Exclude')
                no_students_excluded = no_students_excluded + 1  # if so incrementing the variable that holds the number of students that have been excluded
            else:
                print('Do not progress-module retriever')
                no_students_retriever = no_students_retriever + 1  # else incrementing the variable that holds the number of students that have been retriever
        count = count + 1

    except:
        creating_histogram(no_students_progressed, no_students_trailing, no_students_retriever, no_students_excluded)
        break
