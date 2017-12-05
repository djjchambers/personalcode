import time

def clockify(time):
    print(time, "which equals")
    # days floor div time = whole days
    days = time // 365.25
    # print the days plus a separator
    print("Time =: ", days, " days, ")
    # days modulus 365.25 goes into tot_for_hours
    tot_for_hours = time % 365.25
    # print the hours plus separator
    print(":", tot_for_hours, " hours, ")
    # tot_for_hours modulus 60 goes into tot_for_min
    tot_for_min = tot_for_hours % 60
    # print the mins plus separator
    print(":", tot_for_min, " mins, ")
    # tot_for_min modulus 60 goes into tot_for_secs
    tot_for_secs = tot_for_min % 60
    # print secs
    print(":", tot_for_secs, " seconds.")

time = time.time()
clockify(time)