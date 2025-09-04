# def merge_bruteforce(intervals):
#     if not intervals:
#         return []

#     def overlaps(a, b):
#         return not (a[1] < b[0] or b[1] < a[0])

#     changed = True
#     while changed:
#         changed = False
#         new_list = []
#         used = [False] * len(intervals)

#         for i in range(len(intervals)):
#             if used[i]:
#                 continue
#             cur = intervals[i][:]

#             for j in range(i + 1, len(intervals)):
#                 if used[j]:
#                     continue
#                 if overlaps(cur, intervals[j]):
#                     # merge
#                     cur[0] = min(cur[0], intervals[j][0])
#                     cur[1] = max(cur[1], intervals[j][1])
#                     used[j] = True
#                     changed = True

#             used[i] = True
#             new_list.append(cur)

#         intervals = new_list

#     return intervals


def merge_intervals_bf(intervals: list[list[int]]):
    # Base Case
    if not intervals:
        return []

    # work on a copy to avoid mutating caller's data
    intervals = [iv[:] for iv in intervals]

    final_list =[]
    
    def overlap(a,b):
        return not (a[1] < b[0] or b[1] < a[0])
       

    for i in range(len(intervals)):
        curr = intervals[i]                        # [1,3]
        for j in range(i+1,len(intervals)):        # [8,10]
            if overlap (curr, intervals[j]):
                curr[0] = min(curr[0],intervals[j][0])
                curr[1] = max(curr[1], intervals[j][1])
                intervals.pop(j)
                

        final_list.append(curr)

    return final_list
    


if __name__ =="__main__":
    lst = [[1,3],[8,10],[2,6],[15,18]]

    result = merge_intervals_bf(lst)
    print(result)