import random as rd


# numb - number to be guessed and feedback - feedback message
def psvt_step(numb, feedback):
    # When gs_nm is too far from num
    if feedback == 'higher positive':
        b = numb//2
        step_val = rd.randint(0, b)
    # When gs_nm is too close to num
    elif feedback == 'lower positive':
        nm = numb//4
        step_val = rd.randint(0, nm)
    else:
        # When gs_nm is Negative
        step_val = rd.randint(0, numb//2)
    return step_val


# If the selected number is positive , guess the selected
# number using the following function
def prd_postv(numb1):
    start = 0
    stop = numb1+100
    step = 1
    # Guess a number
    gs_nm = rd.randrange(start, stop, step)
    # Feedback values
    feedback_val = ['higher positive', 'lower positive', 'Select non negative']
    # Give feedback
    if gs_nm > numb1:
        feedback = feedback_val[0]
        # Decide step according to feedback
        step = psvt_step(numb1, feedback)
        # Guess number by adding step to gs_nm
        gs_nm += step

    elif gs_nm < numb1:
        feedback = feedback_val[1]
        # Number is positive
        if gs_nm > 0:
            step = psvt_step(numb1, feedback)
            gs_nm += step

        # Number is negative
        else:
            feedback = feedback_val[2]
            gs_nm = 0
            step = psvt_step(numb1, feedback)
            gs_nm += step

    return gs_nm


# gs_nm - guessed number and numbr - number to be guessed
def check_prd(gs_nm, numbr):
    number = 0
    if gs_nm == numbr:
        print("Selected number is:", numbr)
    else:
        number = prd_postv(numbr)
        if number == numbr:
            return number
        else:
            number = prd_postv(numbr)
    return number
