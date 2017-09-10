import numpy as np
import bisect

prints = [[39.5, 55], [13.75, 21.5], [23.5, 33.5], [28, 22], [9.5, 12], [22.25, 13.375], [18.125, 24], [20, 20]]
# print(prints)

inset_frames = prints
print("Print sizes: {}".format(inset_frames))
for each in inset_frames:
    each[0] += 1.25
    each[1] += 1.25
    if each[0] >= each[1]:
        each[1] -= 3
    else:
        each[0] -= 3
print("Frame piece lengths: {}".format(inset_frames))


def build_temp(pieceslst, lngth):
    temp = []
    if pieceslst:
        for each in pieceslst:
            optsize = lngth - sum(temp)
            if each <= optsize:
                temp.append(each)
                pieceslst.remove(each)
            elif optsize < min(pieceslst):
                return temp
            elif each > lngth:
                # print('here')
                temp.append(each)
                pieceslst.remove(each)
                return temp
            else:
                i = bisect.bisect_left(pieceslst, optsize)
                if i:
                    temp.append(pieceslst[i - 1])
                    # print("Temp is: {}".format(temp))
        return temp
    else:
        return None


def optimize(frames, std_len):
    pieces = frames * 2
    pieces = [item for sublist in pieces for item in sublist]
    pieces = sorted(pieces, reverse=True)
    pieces_mod = []

    while pieces:
        templst = build_temp(pieces, std_len)
        if templst:
            pieces_mod.append(templst)
            if templst in pieces:
                pieces.remove(next(x for x in templst if templst))
                # print("Pieces list is: {}".format(pieces))
                # print("Pieces mod is: {}".format(pieces_mod))

                # print("Pieces remaining: {}".format(pieces))
                # print("Pieces mod is {}".format(pieces_mod))

    # print("before return {}".format(pieces_mod))
    # print(len(pieces_mod))
    return pieces_mod


def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output


standardlength = 36
pieces_list = optimize(inset_frames, standardlength)
remainders = [standardlength-sum(x) for x in pieces_list]
print("Will need {} pieces of {}inches long for pieces: {} and remainders: {}".format(len(pieces_list), standardlength,
                                                                               pieces_list, remainders))
