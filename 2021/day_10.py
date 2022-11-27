input_data_tmp = ["[({(<(())[]>[[{[]{<()<>>",
              "[(()[<>])]({[<{<<[]>>(",
              "(((({<>}<{<{<>}{[]{[]{}",
              "{<[[]]>}<{[{[{[]{()[[[]",
              "<{([{{}}[<[[[<>{}]]]>[]]"]

input_data = [
    "{[<<([[{{[<[[[<>()]{[]<>}]]<[[{}()>{[]{}}]>>][((<{{}[]}{[][]}>({{}{}}{{}[]})))([{({}[])}(<",
    "[[{[<[<[<<([[<<>[]>([]())][<<>[]><<>{}>>][(<{}()><<>>)]){{<<(){}><[]<>>>{([][])<[]{}>}}{[<[]<",
    "<[([[[({[([<<[[]()]{[]{}}>(<[]{}>{{}()})>{{(<><>)[{}()]}([()<>][<>])}]{[{({}())[[]{}]}]((<<>[]>)<(<>())",
    "{[(({<{[{{[{[[[][]]<[]()>]<[{}[]]>}[<(()<>)<{}[]>>{([][])(()())}]](<<{()<>}>[{<>{}}{{}<>}]>)}(([([(){}]<<",
    "<{[[{[<<[({(({<>{}}(<>{})){{{}()}(<>{})})<<<<>()>{()}>{[{}()][()<>]}>}{([{{}{}}]<{{}()}((){})>)({<[](",
    "<<<[[<({(<(([<{}()>]([()]{()}))<{{{}<>}<<>()>}[[()<>]<<><>>]>)>)[({[({<><>}<<>[]>){[{}()]{()<>}}][{<{",
    "{{(({<<{{[((<(<>[])<[]()>><[<>[]](()[])>)[({()}({}[]))[({}<>)[{}<>]]])[([([]<>)<()<>>}{[(){}]",
    "<{[{<(([{[{{{{<>[]}<()<>>}(((){})<[][]>)}{[[{}<>]]<{<>{}}{<><>}>}}]}{<{[<[()()][<>()]>(<<>[]><()<>})](",
    "(<((<[<(([[((({}<>)<{}()>){{[]}[()<>]})([{[][]}<<>()>])]{<[{<>()}[<>()]][([]())<[]()>]>[(<{}[]>(()())){([",
    "[{(<{[<(([<<<<[]()>[<>{}]>[((){})(()<>)]><(([]<>){()<>}){[{}]{[]()}}>>([<<<>[]>{<>{}}>{<[]{",
    "<{[<({{[(<<<[{()[]}][[(){}]<<>()>]>>>((<[<[]()>(<>())][[[]<>](<><>)]>(<<[]()><<>[]>>({()}<<>[]>)))[",
    "{(([[(<[[<{[(<[]<>><<><>>)]}>]]>{[[{([{<{}{}>[<>[]]}<[<>{}]<()<>>>][{<{}>{<><>}}{{{}[]}([]())}])",
    "{<<{<[<[<<({{(()[])}<{{}{}}([]())>})[(<{{}{}}((){})>[[<>[]][<>[]]])[{<[]()>{{}<>}}{{[]{}}<[]()>}]]>>]>{",
    "<([{{{{(<((<{[{}[]][[]<>]}>{<(<>{})(<><>)}})[{(<<>>({}{}))(({}{}){[]})}])<<<{<<>[]>{()[]}}>{<({}[])>[[[]<",
    "({<{<(<[<<(<{[<><>]<{}()>}[({}{}){()[]}]><<(()<>){{}{}}>(<[][]>[[][]])>)>{<[(<{}[]>[()()])({[]()}<",
    "{[{({<(((<[{(({}())(<><>))<[<>{}]{()[]}>}([([]<>)([][])}(<[]{}><[]{}>))](([([][])({}<>)]([[]()]{[]",
    "(((([<[(<[<<[{<><>}{{}<>}]<<()>>>>]>{([{<({}{})>[(()<>)[()()]]}[{([]())[{}[]])({{}<>}{{}{}})]])[((<<(){}",
    "{([(({[[<[{([[<>()]][(<>[])([]{})]><<(()<>)([]{})>([<>{}])>}([<<{}[]>(<>[])>{[()<>]<()[]>}]{[[[][]][[]()]]",
    "[[<({<<<<(<([({}())[<>{}]]{[()<>]{{}[]}})((<<><>>[<>{}])<(<>{}){{}()}>)]<<<{<>{}}((){})>([[]()]{{}})><(({}<",
    "<[{[{{<([(({[[<><>]{<><>}]}<((()<>))[<()()>{[][]}]>)[(({<><>}({}())){<[]()>})])<(<<[()<>]((){})><[()<>](<>",
    "[{{{{[[{{{(<{{[]<>}{<>{}}}<{[]{}}[[]]>><({()()}{<><>})[(<><>)]>)}[(<<(<><>)([][])>[[()[]]{()<>}]>{(<",
    "((<({(<({{{[{{{}<>}<[]{}>}{{[]{}}{{}[]}}](<[<>()]>)}}<([{[{}{}]{<>()}}<<()[]>([]<>)>]<<[()[",
    "<[<([(<{[(<[[{[]{}}{{}}](([]{})([][]))][[<[][]>{{}<>}]<[{}<>][[]]>]>[{<({}{})<[][]>>[{<>}]}{<[{}[]]>}]",
    "{(({{[<([[{((([]<>)[<>()])[({}{})(()<>)])(<{[]<>}([]<>)>{<<>()>({}<>}})}][<{[{<>{}}<()<>>](<<><>>({",
    "<{({(({{<{[(({{}<>})[<[][]>])]<<[<{}[]>(()[])]<(<><>)[<><>]>]{{{()[]}(<><>)}({()()}[<>{}])}>",
    "<[<<[<[{({[<[<()()><[]{}>]{<{}{}>[[]{}]}>[<[[]<>]<<>[]>><{<>[]}([]{})>]]})}[[[<[<[<>]<()()>>({()[]}<()<>>",
    "[(<<{<[[{((<({[]<>}[()[]])(<[]{}>({}[]))>(((<><>)<{}<>>)<{[]{}}<[][]>>)))}[<[((<(){}>{[]})[[[]<>]([]<",
    "[{[({[{<<{<<(<<>{}>{[]()})[{[][]}<{}{}>]><([{}[]][<>()])({[][]})>>[<{<()()>[{}<>]}<([]{})(<>{})>><[(()()){(",
    "{<([[{<[(<<<[<[][]>]({()[]}{[][]})>>{{{[{}<>][[]{}]}[{{}()}(<>())]}<([[][]]{()[]})<{{}{}}<(){}>>>}>[[(",
    "({[[((<<{[<{{([][])(<>[])}<[()[]][[]{}]>}[<[<>{}]([]{})><(<>[])<(){}>>]>[[[({}{})((){})){<()<>>{{}",
    "{<<{({({[{{{{(<>{})({})}<({}()>(()[])>}[<[<>[]]>{{<>{}}(()<>)}]}[<{<()<>>{<>{}}}[<[]{}>(<>())]>(<[{}(",
    "[[{<((<<[[{<(<()[]>([]{}))<<<>{}>(())>>[({[]<>}(()<>))<({}<>)<[]<>>>]}](({<[()[]][{}]>}<(([]<>)<<>>)",
    "<{{((((<{([([(<>[]){()()}]{(<>())([]())})]{[<(<>[])>{[()[]]<[]<>>}]<(({}<>)({}()))>})<[<{<{",
    "<[({<<[{<[<([([]{})[()())][<()[]><<>()>])([(<>())])><[<[()<>]><{<><>}<[]>>]>]([{[[<>{}]{{}{}}]<{",
    "<[{[[<{[<({<((()[]){{}[]})<(<>[])[<>()]>>})>]}>][(([((<[{({}{})<[]{}>}]<([<>{}](()()))(<<>{}><(",
    "<{[[([{[<([(<(<>[])><([][])[[][]]>)(({<>[]}[{}()])[{()<>}{<>}])]<(<(()[])<<>{}>>{<<><>>[[]()]}){<{<>()}{",
    "{<{<{{<({<(<<{()()}>({[]{}}[{}{}])>)<<({{}()}({}{}))<{[]()}{<><>}>>[[<()()>(<>())]]>]})<<{[[((",
    "((<((<<([({([{[]<>}[()()]][[[][]]({}())])})(([<<[]<>>(<>)>]<{({}[]){{}}}{<{}[]>({}())}>){<",
    "{<((<<[<{{[({<[]()>{[]{}}}({[][]}[{}{}]))[<[[]{}]{{}[]}>]]}[{[<[()()]<<>[]>>]{[<<>{}>(<>{})](",
    "<{<<{({[<<<<([()<>]<<>[]>)(<()><{}()))><{<[]{}>[[]]}>>>[{([[{}<>]](<<>[]><{}<>>))[(({}{}){{}[]})((<>[])[<>(",
    "{<[{(<<[{(<(((()())[{}{}])<{()<>}[{}]>){{{()}{[]<>}}[[[]<>]{<><>}]}>)}({<<(({}()))<([]()}[<><>]>>{[[<>()]",
    "<([[[<<([(<([(()())][<{}()>((){})])(([<>()]{<>[]})[[(){}]<()<>>])>)(([[{{}[]}[{}()]][<(){}><(){}>]]{{<<>{}>",
    "(([([{{{<([<<{(){}}<()<>>>{<<><>>[{}()]}>({<<>{}>[()()]}<<<>{}>>}])[{{[([]())({}<>)]<<<>()>[()[]]",
    "{(<({<([{([{(({}))[{<>[]}[{}()]]}[({()<>}{<>()})<([]()){{}()}>]]({<<[][]>([]<>)><{()<>}{(){}}>",
    "[[{({{{({<(<[({}<>)([]())]>(({{}{}}{()<>})>)[{{<<>{}><[]{}>}<<[][]><[][]>>}<(([]<>)<{}{}>)>]>",
    "([{{([(({({<[{()[]}<[]()>]<<{}<>><()[]>>>(<(<>[])<{}{}>>([{}{}]({}())))}([({{}[]>{{}{}})<<{}()><{}>>]<{<{}{}",
    "[<((<<[{[[[<(<<><>><<>()>)>]]]{<{<<[{}<>][{}{}]>(<{}[]>([]()))><<<<>{}>>{[<>{}]{<>[]}}>}[{(",
    "(((<({{[(({[[([]{})({}{})](([]{}){{}{}})]{(<[]{}>[[]()])(<()()><()<>>)}}))<{[{(<{}>{[]<>})}{",
    "[([{{(<<({(<<<[][]>{[]<>}){({}())[[]{}]}>){[({<>[]}{[]<>})]{({()<>}{()[]})}}}[(([[()[]][()()]](<<>{}>",
    "[<{({<<([<[[{[[]{}>{<>()}}<[<>{}]{()<>}>]]>{[(<([]{}){{}[]}>{{[]{}}(<>[])})((({}<>)(()()))[<",
    "<<<([{{<[<([[{<>()}[[]<>]]][<<()()>{()<>}>[[<>{}]<{}<>>]]){((<[]{}><{}<>>))}>[[(<([]())>(({}[])))",
    "{({<([[{({{{[{<>{}]<[]()>]}([<[]<>><()<>>][([]<>)<{}()>])}[{<{{}{}}<()<>>>}]}[{[[<<>[]>([][])][<<>{}>[<",
    "(((([[[((<[<[((){})<{}<>>]>(<[{}](()<>)><[<>{}][<>()]>)]>([(([()[]]<{}>)([<>[]]{()()}))]))(<[<<{<>()}<{}>>(",
    "<{[((([[({[<<[{}()>[{}{}]>>{[(()())[{}{}]]}]})<[[((([]<>)<<>[]>){({}<>){<>()}})<<[<>[]]([]())>([{}[]",
    "{<([[{<[{{<{{([][]><<><>>}<{()()}<[]()>>}<(({}<>)<{}[]>)>>}}[{(([(<><>)<[][]>]{(()())}){{(()[",
    "<(({([({<[(((<[]>)({{}<>}[[]{}])))[[[(<><>)(<>[])]<{<>}([]{})>]{(({}{}))<{{}<>}{[]{}}>}]]{<{{([",
    "<[[{(<[{(<([(([]<>)[<>])])>)}<{[({({()<>}[<>{}])<{<><>}<{}{}>>}{<[<>[]]<<>[]>>[{()()}[{}<>]]}){{<<[][]>({}<",
    "<[{(<{[[[[{[[<[]{}>{[]<>}]<[{}{}]<{}<>>>]((<{}<>>)[{()}(<>[])])}({[{{}()}[{}()]][<(){}}(()<>)]}<[[",
    "<<(<[[<<([{<({()<>}(()<>)>([()][[]{}])>}])>{[([[<[<><>]({}{})>(<<><>>{()<>})]][(({{}()}{()()})<{<>()}[[]<",
    "<(<({<[{<{<[{{{}()}({}<>)}<[[]()][<>{}]>]>((<[()<>]{[]<>}>((<>())<[]()>)))}{[(([()()]<(){}>){<()<>>[",
    "[[[([{<([<<<{[()<>]{()[]}}<([]())[{}[]]>><<[[]<>]>{<[]{}><<>()>}>>([{{[]<>}(()())}[<<>>{<>{}}]](([<>()]<<>()",
    "{<([{[{{<[<[[{{}}([]{})]]<<{<>{}}><[(){}]>>>(([(<>)<()[]>][{{}[]}(<>[])]){<{<>[]}<<>[]>>{<<>[]>{",
    "{[[{<[[<<[[([{()[])[[][]]]{{()()}})]]>>[{{<[{(<><>)}<<()[]>({}())>]<[({}<>)]>>[[{[[]()]<<>{}>}[[<>{}]<()",
    "[({{{<[([[{[[({}{})][<<>{}>{{}[]}]]({<[][]>}(({}<>)({}<>)))}<[{({})}({()()}<[]{}>>]((<[]{}>[{}{}]))>]{{{<{[]{",
    "<[<<[{[{{<(<{{()<>}{{}{}}}[[[]{}]]>[[<()()><[]()>]([[]{}])])>[{[[([]()){()}][([]())[<>[]]]]}]}}{<[[[(<{}()>{{",
    "<[{<{[[<<([[{(<><>)[(){}]}]]((([()<>]<<>[]>)[<[][]>({}<>)])))[<[<[<>()][(){}]}{[()()]}]{({()()}(()",
    "[<{[((<<{((<({{}<>}{()[]}){{{}[]}(()())}]{<<{}()>{<>()}>})([{[{}{}][[]()]}<[{}[]]<<>()>>]))}<<{(",
    "{({{([([[{{(<<()<>><(){}>>)<[({}())(<><>)]{[<>()][()[]]}>}({[{{}<>}[[]{}}]}{(<{}[]><{}>)(<[][]>[{}<>",
    "({[[<({{[<((((()<>)<()<>>)<{[][]}[[]<>]>)({(()<>){{}[]}][(()[])[[][]]]))([<<()()>{<><>}>({{}[]}((){})",
    "{<{[(<(<({{<<(<>[])<<><>>><<[][]>(()[])>>[[([]<>)([]<>)][<()()>]]}}{(<{{<><>}(()<>)]{[[]()]",
    "[[[[<[{{[{<[<[<><>]>](<(()[]){{}[]}><(<>{})[{}()]>)>(<{{[]<>}<<><>>}[<{}<>>[{}()])>)}({[<<(",
    "[{{<{[(([{{{((<>[])<{}{}}){<{}[]>([])}}{<{<><>}({}[])>{{()[]}{[][]}}}}<<{[<>{}](<><>)}<{{}",
    "<[[{(<[{(({<<<<>[]><{}<>]><<()()><()()>>>{[<()<>>{[]}]<<()()>{[][]}>}}[{(<{}[]>[{}[]])}{[{{}<>}",
    "{[((<{([[({<([()<>][[][]])([()()]{[][]})>[[[{}]>({[][]}{[][]})]}<[[{<>[]}<()()>]{<[]()>}]>)][[<{",
    "(<<{(({[[<[<<[{}<>]>{{{}<>}((){})}>][<[{()[]}{{}[]}]>(<{<>{}}[<><>]>{[[]{}]<{}()>})]>]<[[[{[()[]]({}[])}([{}",
    "[[{([<<{[<([{{(){}}{{}[]}}[{<>()}]][<[<>{}}[[]]>({[]{}}<<>[]>)])(({[{}{}](()<>)}[(<><>){{}()}]))",
    "<<<({[{[<<((({<>{}})({<>{}}<[]<>>)))[<[<{}<>><{}<>>]([[]{}][()<>])>(([{}{}]{{}<>})({[]{}}[[]<",
    "{[[[[[{{<<<<{[{}()]([][])}{<[]()>({}{})}>([[[]{}]][[(){}][{}{}]])>{([[{}{}]({}<>)]([<><>][()<>]))}>",
    "[[<(([[(([[(([()[]]<{}<>>){{{}()}[[]()>})][<[[(){}][[]{}]][<{}[]><[]<>>]>{(<<>{}><()()>)(<()()><{}[]>)",
    "[<([(<[<<(([{{{}()}<{}[]>}[<<>()><<>()>]]))({<<{[]()}>{{[][]}<[]{}>}}[{([])<[][]>}]}{<[[[]()]{<>{}}]{<[][]>}",
    "{{{[[[{<<{<(<[{}{}](<>())>[{[][]}[{}<>]])[[(()[])({}())]{([]{})(()<>)}]>((([{}]{[]<>}))([{()[]}{{}",
    "[[(([{<[((<([{{}()}[()<>]]{<<><>>[[]<>]})([[<><>]([])]((<>()){<>[]}))><(<({})<()()>>)(<<<>{}>([]())>{<[][",
    "(<{({(<<(<{(({{}()}<[]<>>))[<<{}{}>[(){}]>]}<[(({}{})<()()>)[{()()}<[]>]](([[][]])([(){}]<[]()>))>>)",
    "<[{[<(<(({[<[(()<>)]{<()()><[]()>}>[{(<><>)[[]{}]}{({}<>)<(){}]}]]{(<[()<>]{<><>}>[{{}<>}({}[",
    "<[(<<[{{[[[<<<[]()><[]{}>>[([]()){()[]}]>({[[]()]<{}{}>}{[()[]]<{}{}>})]]]{([{<<{}[]>>}][[[[<>",
    "<{[[({{[<<<[<({})[[]]>]>>{[[[[()<>][()()]](<{}<>>)](<<[][]>[[]<>]>)]}>[<<[<<(){}>[<>()]>]<(((){}){{}",
    "[(<[<(<<{[([[{<>[]}([]())]<([]<>)[<>()]>]<[{(){}}[[][]]](<[]{}><{}<>>)>)]<{<<<[][]>>({(){}}[{}<>])",
    "{({([[{{(((<(<[]()>{<><>})(<(){}}<()[]>)><[{()[]}(()())][[{}<>]{[]{}}]>){([[{}{}](())])(<<()<>>[[][]",
    "(([[[<([[<[<[<{}{}>][<(){}>[<>[]]]>(([[]()][()]}{<[]{}><[]<>>})][(({()<>}<[]<>>)[[[]]]){[{()[]}<()()",
    "({{<[(([[{<<<[[][]]>[{()<>}<{}()>]>>(<<{()}[()<>]>><{(()<>)([]{})}>)>](<({{{()[]}[(){}]}[{{}{}}"
    ]

task_2_data = []

def get_indentation_dict(line):
    i = 0
    indented_data = {}
    for sign in line:

        if sign in ('[', '(', '{', '<'):
            #print(f"sign: {sign}, i: {i}")

            if i not in indented_data:
                indented_data[i] = sign
            else:
                string_list = list(indented_data[i])
                string_list.append(sign)
                indented_data[i] = "".join(string_list)

            i += 1
        else:
            i -= 1
            string_list = list(indented_data[i])
            string_list.append(sign)
            indented_data[i] = "".join(string_list)
    return indented_data

points = 0
for line in input_data:
    task_2_data.append(line)
    next_line = False
    result = get_indentation_dict(line)


    for key, val in result.items():
        if next_line == True:
            task_2_data.pop(-1)
            break
        brachets = {'[': 0, '(': 0, '{': 0, '<': 0}

        for char in val:
            print(f"val: {val}")
            print(f"char: {char}")

            if char in ('[', '(', '{', '<'):
                brachets[char] += 1
            else:
                print(f"type(char): {type(char)}")
                if char == ')':
                    brachets['('] -= 1
                    if brachets['('] < 0:
                        points += 3
                        next_line = True
                        break
                if char == ']':
                    brachets['['] -= 1
                    if brachets['['] < 0:
                        points += 57
                        next_line = True
                        break
                if char == '}':
                    brachets['{'] -= 1
                    if brachets['{'] < 0:
                        points += 1197
                        next_line = True
                        break
                if char == '>':
                    brachets['<'] -= 1
                    if brachets['<'] < 0:
                        points += 25137
                        next_line = True
                        break
        print(f"brachets: {brachets}")

    print(f"result: {result}")
    print(f"brachets: {brachets}")
print(f"points: {points}")

print("")
print(f"TASK_2_DATA:")


def clean_up_closed(string):
    string_list = list(string)

    return "".join(string_list[-1])



scores = []
for line in task_2_data:
    print("")
    print(f"Line: {line}")
    result = get_indentation_dict(line)
    print(f"result: {result}")
    missing_chars = []
    score = 0
    for key, val in sorted(list(result.items()), key=lambda x: x[0], reverse=True):
        score = score*5
        if len(val) % 2 == 1:
            clean_val = clean_up_closed(val)
            if clean_val == '(':
                score += 1
                missing_chars.append(')')
            if clean_val == '[':
                score += 2
                missing_chars.append(']')
            if clean_val == '{':
                score += 3
                missing_chars.append('}')
            if clean_val == '<':
                score += 4
                missing_chars.append('>')
    print(f"missing_chars: {missing_chars}")
    print(f"score: {score}")
    scores.append(score)

print(f"scores: {scores}")
print(f"len(scores): {int(len(scores)/2)}")
sorted_scores = sorted(scores)
print(f"sorted_scores: {sorted_scores}")

result = sorted_scores[int(len(scores)/2)]
print(f"result: {result}")


# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
# So, the last completion string above - ])}> - would be scored as follows:
#
# Start with a total score of 0.
# Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
# Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
# Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
# Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
#[339, 4658, 9248, 42489,
# 44814, 45614, 117031, 202482,
# 207371, 213444, 213656, 264124,
# 280797, 290539, 380221, 604319,
# 620298, 933464, 935231, 935934,
# 1151499, 1160587,
# 1317731, # Wrong
# 1389538,1446092,
# 1503969, 1530798, 1552857, 1787366,
# 1819784, 1842734, 1851563, 2573287,
# 2992164, 3035864, 3117819, 3311483,
# 3725944, 4446167, 4446421, 5758423,
# 7789093, 7789567, 8745187, 9586499]