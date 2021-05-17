pass_credit = 0
defer_credit = 0
fail_credit = 0
credit_list = [0, 20, 40, 60, 80, 100, 120]

pass_list = [120, 100, 100, 80, 60, 40, 20, 20, 20, 20, 0]  # assigning the values into three seperate lists
defer_list = [0, 20, 0, 20, 40, 40, 40, 20, 20, 0, 0]
fail_list = [0, 0, 20, 20, 20, 40, 60, 80, 80, 100, 120]

for c in range(10):  # iterating through the loop 10 times to get the each value in the lists separately
    pass_credit = pass_list[c]  # assigning each value into a variable
    defer_credit = defer_list[c]
    fail_credit = fail_list[c]
    total = pass_credit + defer_credit + fail_credit

    if total != 120:  # checking the conditions starts here
        print('Total incorrect')
    if pass_credit not in credit_list or defer_credit not in credit_list or fail_credit not in credit_list:
        print('Range Error')
    else:
        if pass_credit == 120:
            print('Progress')
        elif pass_credit == 100:
            print('Progress-module trailer')
        elif fail_credit >= 80:
            print('Exclude')
        else:
            print('Do not progress-module retriever')
