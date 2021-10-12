import json


def read_file(name="data.txt"):
    with(open(name, 'r') as f):
        text = f.readlines()
        return text


def clear_lines(my_list):
    cleared_list = []
    for line in my_list:
        cleared_list.append(line.strip('\n').strip())
    return cleared_list


def get_tuples(my_list):
    res_list = []
    vars_list = []
    vals_list = []
    for idx in range(0, len(my_list)):
        if(idx % 2):
            vars_list.append(my_list[idx])
        else:
            vals_list.append(my_list[idx])

    res_list = list(zip(vals_list, vars_list))
    return res_list


def get_dicts(my_list):
    res_list = []
    for idx in range(0, len(my_list)):
        # Tuples (3A, 2), where: 3 - num of test, A - variant, 2 - score
        item = my_list[idx]
        num = int(item[0][:-1])
        variant = item[0][-1]
        score = int(item[1])
        # Could use tuples as keys for quick search
        # but we need to convert to .json
        # res = {(num, variant): score}
        res = {num: [variant, score]}
        res_list.append(res)
    return res_list


def write_to_json(list_of_dicts):
    with(open('out.json', 'w', encoding='utf-8') as f):
        jsonString = json.dumps(list_of_dicts)
        f.write(jsonString)


# Put your file into root directory
# and specify it's name as `read_file`
# function argument
# result will be written to out.json
content = read_file()
content = clear_lines(content)
content = get_tuples(content)
content = get_dicts(content)
write_to_json(content)

print(content)
