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
        print("Range Error")


while (pass_credit != 'q') or (defer_credit != 'q') or (
        fail_credit != 'q'):  # until the letter q is enetered the loop iterates
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
            if pass_credit == 120:
                print('Progress')
                no_students_progressed = no_students_progressed + 1
            elif pass_credit == 100:
                print('Progress-module trailer')
                no_students_trailing = no_students_trailing + 1
            elif fail_credit >= 80:
                print('Exclude')
                no_students_excluded = no_students_excluded + 1
            else:
                print('Do not progress-module retriever')
                no_students_retriever = no_students_retriever + 1
        count = count + 1

    except:
        high = 0

        # finding the highest number of students from the four categories
        if no_students_progressed > no_students_excluded and no_students_progressed > no_students_trailing and no_students_progressed > no_students_retriever:
            high = no_students_progressed
        elif no_students_excluded > no_students_trailing and no_students_excluded > no_students_retriever:
            high = no_students_excluded
        elif no_students_trailing > no_students_retriever:
            high = no_students_trailing
        else:
            high = no_students_retriever

        count_1 = 1
        print("Progressed", " ", "Trailing", " ", "Retriever", " ",
              "Excluded")  # starts to print the vertical histogram
        p_count = 1
        t_count = 1
        e_count = 1
        r_count = 1
        while count_1 <= high:  # printing the stars starts here

            if p_count <= no_students_progressed:
                print("*", end="              ")
                p_count = p_count + 1
            else:
                print(" ", end="              ")
            if t_count <= no_students_trailing:
                print("*", end="            ")
                t_count = t_count + 1
            else:
                print(" ", end="            ")
            if r_count <= no_students_retriever:
                print("*", end="            ")
                r_count = r_count + 1
            else:
                print(" ", end="            ")
            if e_count <= no_students_excluded:
                print("*", end="            ")
                e_count = e_count + 1
            else:
                print(" ", end="            ")

            print('\n')

            count_1 = count_1 + 1
        break
