from IThekaton import calculate

def test_calculate(input,output):
    input = input.strip().split("\n")
    output = output.strip().split("\n")
    i = 0
    for example in input:
        func = calculate(example)
        response = example + " is '" + str(func) + "' but should be " + str(output[i])
        assert func == int(output[i]),response
        i += 1

input = '''
20 6 led display
100 20 led display 2020
10 20 MUST BE ABLE TO DISPLAY
55 25 Can you hack
100 20 display product text
27 15 May the Force be with you
10 40 Legen wait-for-it dary, legendary
420 100 You want the truth? You can't handle the truth
65 65 Houston, we have a problem
345 160 My mama always said life was like a box of chocolates. You never know what you're gonna get
230 130 You know nothing, Jon Snow
14 10 Dobby is free
15 80 Say 'hello' to my little friend!
100 15 Live long and prosper
23 2 Bazinga
'''

output = '''
2
9
1
8
8
3
0
26
8
22
28
2
2
7
2
'''

if __name__ == "__main__":
    test_calculate(input,output)
    print("Pass!")
