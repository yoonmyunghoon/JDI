def solution(phone_book):
    answer = True
    dic = {}
    for pb in phone_book:
        len_pb = len(pb)
        for k in range(len_pb):
            if pb[k] in info:
                dic[k]

    return answer

#
# info =
# {
#     1 : {
#         2 : {
#             -1 : 1,
#             3 : {
#                 -1 : 1,
#                 5 : {
#                     -1 : 1
#                 }
#             }
#
#         }
#     },
#     5 : {
#         6 : {
#             7 : {
#                 -1 : 1
#             }
#         }
#     },
#     8 : {
#         8 : {
#             -1 : 1
#         }
#     }
#
# }

P = ["12", "123", "1235", "567", "88"]
solution(P)