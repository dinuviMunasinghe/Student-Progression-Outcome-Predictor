pass_credit = 0
defer_credit = 0
fail_credit = 0
credit_list = [0, 20, 40, 60, 80, 100, 120]


def rangecheck(credit):
    if credit not in credit_list:
        checked = "Range Error"
        return checked


try:
    pass_credit = int(input(
        'Enter the number of credits at pass.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
    while rangecheck(pass_credit) == "Range Error":
        print('Range Error')
        print("please re-enter as there is a range error")
        pass_credit = int(input('Enter the number of credits at pass.'))

    defer_credit = int(input(
        'Enter the number of credits at defer.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
    while rangecheck(defer_credit) == "Range Error":
        print('Range Error')
        print("please re-enter as there is a range error")
        defer_credit = int(input('Enter the number of credits at defer.'))

    fail_credit = int(input(
        'Enter the number of credits at fail.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
    while rangecheck(fail_credit) == "Range Error":
        print('Range Error')
        print("please re-enter as there is a range error")
        defer_credit = int(input('Enter the number of credits at fail.'))

    total_credits = pass_credit + defer_credit + fail_credit

    while total_credits != 120:
        print('Total incorrect')

        pass_credit = int(input(
            'Enter the number of credits at pass.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
        while rangecheck(pass_credit) == "Range Error":
            print('Range Error')
            print("please re-enter as there is a range error")
            pass_credit = int(input('Enter the number of credits at pass.'))

        defer_credit = int(input(
            'Enter the number of credits at defer.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
        while rangecheck(defer_credit) == "Range Error":
            print('Range Error')
            print("please re-enter as there is a range error")
            defer_credit = int(input('Enter the number of credits at defer.'))

        fail_credit = int(input(
            'Enter the number of credits at fail.'))  # until the user enters  valid data to pass_credit it keeps on asking the user to input
        while rangecheck(fail_credit) == "Range Error":
            print('Range Error')
            print("please re-enter as there is a range error")
            fail_credit = int(input('Enter the number of credits at fail.'))

        total_credits = pass_credit + defer_credit + fail_credit


    else:
        # checking if the conditions are true for a student to be progressed, retrieved, trailing or excluded
        if pass_credit == 120:
            print('Progress')
        elif pass_credit == 100:
            print('Progress-module trailer')
        elif fail_credit >= 80:
            print('Exclude')
        else:
            print('Do not progress-module retriever')
except:
    print('Integers required')
