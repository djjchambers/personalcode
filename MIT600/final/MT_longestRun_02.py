def longest_run(L):
    ui = 0
    di = 0
    nums = {}
    dir = 1
    def add_to_dict(list, index1, index2, dict):
        run = (list[index1:index2])
        if index2 == (len(list)-1):
            print('reached the end')
            run.append(list[-1])
            print('adding the last item,', list[-1])
        # this doesn't include the last number so have to do it manually
        print('current run', run)
        # if run of this length not in nums
        if sum(run) not in dict:
            # run is over as dir has changed
            print('adding', run, 'to dict')
            dict[(len(run))] = sum(run)
        # what to return?
        return dict
        
    for n in range(1, len(L)):

        if L[n] == L[n-1]:
            print('EVEN', L[n], '==', L[n-1])
            if dir == -1:
                ui = n-1
                print('ui', ui)
            elif dir == 1:
                di = n-1
                print('di', di)
        elif L[n] > L[n-1]:
            print('UP', L[n], '>', L[n-1])
            # set new downward start to n (because next num might be less)
            if dir == -1:
                # closeout downward run
                nums = add_to_dict(L, di, n, nums)
                # reset downward run start index
                di = n-1
                print(nums)
                print('starting new downward run at', n)
                dir = 1
            elif n == len(L):
                nums = add_to_dict(L, ui, n, nums)
        elif L[n] < L[n-1]:
            print('DOWN', L[n], '<', L[n-1])
            # set new upward start to n
            if dir == 1:
                nums = add_to_dict(L, ui, n, nums)
                # reset upward run start index
                ui = n-1
                print(nums)
                print('starting new upward run at', n)
                dir = -1
            elif n == len(L):
                nums == add_to_dict(L, di, n, nums)
    if nums:
        return nums[max(nums)]
    else:
        return('ARGH!')
print(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(longest_run([100, 200, 300, -100, -200, -1500, -5000]))