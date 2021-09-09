def solution(str1, str2):

    def make_set(input_str):
        str_list = []
        for i in range(len(input_str)-1):
            if 65 <= ord(input_str[i]) <= 90 and 65 <= ord(input_str[i+1]) <= 90:
                str_list.append(input_str[i:i+2])
        return str_list

    def make_dict(input_list):
        str_dict = {}
        for e in input_list:
            if e in str_dict:
                str_dict[e] += 1
            else:
                str_dict[e] = 1
        return str_dict

    def make_intersection(dict1, dict2):
        result = 0
        for k, v in dict1.items():
            if k in dict2:
                result += min(v, dict2[k])
        return result

    def make_union(dict1, dict2):
        result = 0
        for k1, v1 in dict1.items():
            if k1 not in dict2:
                result += v1
            else:
                result += max(v1, dict2[k1])
        for k2, v2 in dict2.items():
            if k2 not in dict1:
                result += v2
        return result

    str1 = str1.upper()
    str2 = str2.upper()
    str1_list = make_set(str1)
    str2_list = make_set(str2)
    str1_dict = make_dict(str1_list)
    str2_dict = make_dict(str2_list)
    intersection_count = make_intersection(str1_dict, str2_dict)
    union_count = make_union(str1_dict, str2_dict)
    if union_count == 0:
        return 65536
    else:
        jac_similarity = intersection_count/union_count
        return int(jac_similarity*65536)


str1_ex = 'E=M*C^2'
str2_ex = 'e=m*c^2'
print(solution(str1_ex, str2_ex))