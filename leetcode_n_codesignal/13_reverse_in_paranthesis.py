# Write a function that reverses characters in (possibly nested) parentheses in the input string.


def solution(inputString):
    inputString_list = [i for i in inputString]
    idxs = {}
    idxs[0] = []
    idxs[1] = []

    for i in range(len(inputString_list)):
        if inputString_list[i] == "(":  # gets the last bracket opening
            if len(idxs[0]) == 0:
                idxs[0].append(i)
            else:
                idxs[0].pop()
                idxs[0].append(i)
        if inputString_list[i] == ")":  # gets the last bracket closing
            if len(idxs[0]) == 1 and len(idxs[1]) == 0:
                idxs[1].append(i)

        if len(idxs[0]) == 1 and len(idxs[1]) == 1:
            break

    print(idxs)

    if len(idxs[0]) > 0:
        req_str_idx = idxs[0][0]
        req_end_idx = idxs[1][0]
        new_inputString = (
            inputString[:req_str_idx]
            + inputString[req_str_idx + 1 : req_end_idx][::-1]
            + inputString[req_end_idx + 1 :]
        )
        return solution(new_inputString)
    else:
        return inputString
