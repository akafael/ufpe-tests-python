import itertools

def exp(a,b,c):
    return ((a or b) and c)

numArgs = 3
listOLists = [[True,False]]*numArgs
permList = itertools.product(*listOLists)

# Generate Truth Table
tableCases = dict()
for i,l in enumerate(permList):
    tableCases[l]=i

print("index ,(x == 0),(y > 0),(z < 0), result")
for var,index in tableCases.items():
    print("{0}, {1}, {2}, {3}, {4}".format(index,*var,exp(*var)) )

## Geerated Table
# index ,(x == 0),(y > 0),(z < 0), result
# 0, True, True, True, True
# 1, True, True, False, False
# 2, True, False, True, True
# 3, True, False, False, False
# 4, False, True, True, True
# 5, False, True, False, False
# 6, False, False, True, False
# 7, False, False, False, False

# Generate Test Case Tables
tableCasesA = tableCases.copy()
tableCasesB = tableCases.copy()
tableCasesC = tableCases.copy()

# Check for valid test combinations for each variable
for testCase in tableCases:
    testCaseModifiedA = not testCase[0],testCase[1],testCase[2]
    testCaseModifiedB = testCase[0],not testCase[1], testCase[2]
    testCaseModifiedC = testCase[0],testCase[1],not testCase[2]

    if testCase in tableCasesA and (exp(*testCase) == exp(*testCaseModifiedA)):
        tableCasesA.pop(testCase)
        tableCasesA.pop(testCaseModifiedA)

    if testCase in tableCasesB and (exp(*testCase) == exp(*testCaseModifiedB)):
        tableCasesB.pop(testCase)
        tableCasesB.pop(testCaseModifiedB)

    if testCase in tableCasesC and (exp(*testCase) == exp(*testCaseModifiedC)):
        tableCasesC.pop(testCase)
        tableCasesC.pop(testCaseModifiedC)

## Print All Valid Test Cases
print("\nValid test cases A")
for testCase,index in tableCasesA.items():
    print(f"{index},{testCase}")

print("\nValid test cases B")
for testCase,index in tableCasesB.items():
    print(f"{index},{testCase}")

print("\nValid test cases C")
for testCase,index in tableCasesC.items():
    print(f"{index},{testCase}")

## Manually Generated List considering the result
# (x == 0) -> {2,6},{3,7}
# (y > 0) -> {4,6},{5,7}
# (z < 0) -> {0,1},{2,3},{4,5}

# result: {0,1,4,6}