def arithmetic_arranger(questions, answers=False):
    if len(questions) > 5:
        return 'Error: Too many problems.'
    print1, print2, print3, print4 = "", "", "", ""
    for inpNums in questions:
        nums = inpNums.split()
        if nums[1] != '+' and nums[1] != '-':
            return 'Error: Operator must be \'+\' or \'-\'.'
        num1, num2 = None, None
        try:
            num1 = int(nums[0])
            num2 = int(nums[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        if num1 > 9999 or num2 > 9999:
            return 'Error: Numbers cannot be more than four digits.'
        max_len = max(len(nums[0]), len(nums[2]))
        line1, line2, line3 = "", "", ""
        if max_len == len(nums[0]):
            line1 = "  " + nums[0]
            line2 = nums[2]
            for i in range(len(line1) - len(line2) - 1):
                line2 = " " + line2
            line2 = nums[1] + line2
        else:
            line2 = nums[1] + " " + nums[2]
            line1 = nums[0]
            while len(line1) < len(line2):
                line1 = " " + line1
        for _ in range(len(line1)):
            line3 += "-"
        print1 += (line1 + "    ")
        print2 += (line2 + "    ")
        print3 += (line3 + "    ")
        if answers:
            ans = None
            if nums[1] == '-':
                ans = str(num1 - num2)
            else:
                ans = str(num1 + num2)
            while len(line1) > len(ans):
                ans = " " + ans
            print4 += (ans + "    ")
    if answers:
        return print1.rstrip() + "\n" + print2.rstrip() + "\n" + print3.rstrip() + "\n" + print4.rstrip()
    else:
        return print1.rstrip() + "\n" + print2.rstrip() + "\n" + print3.rstrip()
