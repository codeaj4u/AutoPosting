quiz_data = [
    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'j = "Python3"\nprint(j[:-2])',
        'Options': ["A) 'Py'", "B) 'Python'", "C) 'Python3'", "D) 'Python3'"]
    },
 
    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'p = "Hello"\nq = p + "World!"\nprint(q)',
        'Options': ["A) 'Hello'", "B) 'World!'", "C) 'HelloWorld!'", "D) 'Hello World!'"]
    },
    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'r = [1, 2, 3]\nprint(len(r))',
        'Options': ["A) 1", "B) 3", "C) 6", "D) Error"]
    },
    {
        'Question': "What is the output of the following code snippet?",
        'Code': "s = {'a': 1, 'b': 2}\nprint('a' in s)",
        'Options': ["A) True", "B) False", "C) None", "D) Error"]
    },

     {
        'Question': "What is the output of the following code snippet?",
        'Code': "t = [1, 2, 3]\nt[1:3] = [4, 5]\nprint(t)",
        'Options': ["A) [1, 4, 5]", "B) [1, 2, 3, 4, 5]", "C) [1, [4, 5], 3]", "D) [1, 4, 3, 5]"]
    },
    {
        'Question': "What is the output of the following code snippet?",
        'Code': "u = {x: x * x for x in range(5)}\nprint(u)",
        'Options': ["A) {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}", "B) [0, 1, 4, 9, 16]", "C) {1, 4, 9, 16, 25}", "D) Error"]
    },

    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'x = [1, 2, 3, 4, 5]\nprint(x[1:3])',
        'Options': ["A) [2, 3]", "B) [1, 2]", "C) [2, 3, 4]", "D) [1, 3]"]
    },

    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'a = 10\nb = 5\na, b = b, a\nprint(a, b)',
        'Options': ["A) 10 5", "B) 5 10", "C) 5 5", "D) 10 10"]
    },
    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'fruits = ["apple", "banana", "cherry"]\nprint(len(fruits))',
        'Options': ["A) 3", "B) 6", "C) 5", "D) Error"]
    },
    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'num_list = [1, 2, 3, 4, 5]\nprint(num_list[-2])',
        'Options': ["A) 2", "B) 4", "C) 5", "D) -2"]
    },

    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'colors = {"red", "green", "blue"}\nprint("yellow" in colors)',
        'Options': ["A) True", "B) False", "C) None", "D) Error"]
    },
    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'text = "Hello World"\nprint(text.split())',
        'Options': ["A) ['Hello', 'World']", "B) ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']",
                    "C) ['Hello World']", "D) Error"]
    },

    {
        'Question': "What will be printed by the following code snippet?",
        'Code': 'num = 5\nprint(num > 3 and num < 10)',
        'Options': ["A) True", "B) False", "C) Error", "D) None"]
    },
    {
        'Question': "What will be the output of the following code snippet?",
        'Code': 'names = ["Alice", "Bob", "Charlie"]\nprint(names[-1])',
        'Options': ["A) Bob", "B) Alice", "C) Charlie", "D) Error"]
    },
    {
        'Question': "What is the result of the following code snippet?",
        'Code': 'age = 20\nis_teen = age > 12 and age < 20\nprint(is_teen)',
        'Options': ["A) True", "B) False", "C) None", "D) Error"]
    },

    {
        'Question': "What is the output of the following code snippet?",
        'Code': 'nums = [1, 2, 3]\nnums.extend([4, 5])\nprint(nums)',
        'Options': ["A) [1, 2, 3, 4, 5]", "B) [1, 2, 3, [4, 5]]", "C) [1, 2, 3, 4, [5]]", "D) Error"]
    },
    {
        'Question': "What will be printed by the following code snippet?",
        'Code': 'word = "Python"\nprint(word[::-1])',
        'Options': ["A) 'Pyt'", "B) 'P'", "C) 'nohtyP'", "D) 'nohtyP'"]
    },

    {
        'Question': "What is the output of this code?",
        'Code': 'x = 5\ny = x * 2\nprint(y)',
        'Options': ["A) 5", "B) 10", "C) 52", "D) Error"]
    },
    {
        'Question': "What will be printed?",
        'Code': 'text = "Hello"\nprint(text[:2] + "Python")',
        'Options': ["A) HePython", "B) PyHello", "C) HePythonlo", "D) Error"]
    },
    {
        'Question': "What will be the output?",
        'Code': 'numbers = [1, 2, 3, 4]\nnumbers.pop(2)\nprint(numbers)',
        'Options': ["A) [1, 3, 4]", "B) [1, 2, 4]", "C) [1, 2, 3]", "D) Error"]
    },
    {
        'Question': "What does this code print?",
        'Code': 'sample = "abcdefgh"\nprint(sample[::2])',
        'Options': ["A) 'aceg'", "B) 'abcde'", "C) 'bdfh'", "D) Error"]
    },

    {
        'Question': "What will this code output?",
        'Code': 'data = {"a": 1, "b": 2, "c": 3}\nprint(data.get("d", 4))',
        'Options': ["A) 4", "B) None", "C) Error", "D) 3"]
    },
    {
        'Question': "What is the output?",
        'Code': 'animals = ["dog", "cat", "rabbit"]\nprint(len(animals[0]))',
        'Options': ["A) 4", "B) 3", "C) 5", "D) Error"]
    },
     {
        'Question': "What is the output of this code?",
        'Code': 'x = 10\ny = 3\nprint(x % y)',
        'Options': ["A) 1", "B) 0", "C) 3", "D) 10"]
    },
    {
        'Question': "What will be printed?",
        'Code': 'word = "Goodbye"\nprint(word[-3:])',
        'Options': ["A) 'bye'", "B) 'ood'", "C) 'God'", "D) Error"]
    },
    {
        'Question': "What is the result?",
        'Code': 'nums = [1, 2, 3]\nnums.append([4, 5])\nprint(len(nums))',
        'Options': ["A) 4", "B) 5", "C) 6", "D) Error"]
    },
    {
        'Question': "What does this code output?",
        'Code': 'phrase = "Hello, World!"\nprint(phrase.split(","))',
        'Options': ["A) ['Hello', ' World!']", "B) ['Hello, World!']", "C) ['Hello', 'World!']", "D) Error"]
    },
    {
        'Question': "What will be printed by this code?",
        'Code': 'my_list = [5, 6, 7, 8]\nmy_list[1:3] = [1, 2, 3]\nprint(my_list)',
        'Options': ["A) [5, 1, 2, 3, 8]", "B) [5, 1, 2, 3]", "C) [5, 1, 2, 3, 6, 7, 8]", "D) Error"]
    },
    {
        'Question': "What is the output of this code snippet?",
        'Code': 'numbers = [1, 2, 3, 4, 5]\nprint(numbers.index(3))',
        'Options': ["A) 2", "B) 3", "C) 4", "D) Error"]
    },

    {
        'Question': "What is the output of this code?",
        'Code': 'a = [1, 2, 3]\nb = a\nc = a.copy()\nb.append(4)\nc.append(5)\nprint(a, b, c)',
        'Options': ["A) [1, 2, 3] [1, 2, 3, 4] [1, 2, 3, 5]", "B) [1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 5]",
                    "C) [1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3]", "D) Error"]
    },
    {
        'Question': "What will be printed by this code?",
        'Code': 'word = "apple"\nprint(word[::-1])',
        'Options': ["A) 'elppa'", "B) 'leppa'", "C) 'appl'", "D) 'lppa'"]
    },
    {
        'Question': "What is the result of this code?",
        'Code': 'nums = [1, 2, 3]\nnums.insert(1, [4, 5])\nprint(nums)',
        'Options': ["A) [1, 4, 5, 2, 3]", "B) [1, [4, 5], 2, 3]", "C) [1, 2, [4, 5], 3]", "D) Error"]
    },
    {
        'Question': "What does this code output?",
        'Code': 'values = {"a": 1, "b": 2, "c": 3}\nprint(values.pop("b"))',
        'Options': ["A) 'a'", "B) 2", "C) 'b'", "D) Error"]
    },

    {
        'Question': "What will be printed by this code?",
        'Code': 'my_string = "Python Programming"\nprint(my_string[2:10:2])',
        'Options': ["A) 'to P'", "B) 't nPg'", "C) 'tnPor'", "D) Error"]
    },
    {
        'Question': "What is the output of this code snippet?",
        'Code': 'data = [10, 20, 30, 40, 50]\nprint(data[-3:])',
        'Options': ["A) [20, 30, 40]", "B) [30, 40, 50]", "C) [40, 50]", "D) Error"]
    },


     {
        'Question': "What will be the output of this code?",
        'Code': 'a = [1, 2, 3]\nb = a[:]\nb.append(4)\nprint(a, b)',
        'Options': ["A) [1, 2, 3] [1, 2, 3, 4]", "B) [1, 2, 3, 4] [1, 2, 3, 4]", "C) [1, 2, 3, 4] [1, 2, 3]", "D) Error"]
    },
    {
        'Question': "What does this code output?",
        'Code': 'string = "Hello, World!"\nprint(string.split())',
        'Options': ["A) ['Hello']", "B) ['Hello, World!']", "C) ['Hello', 'World!']", "D) Error"]
    },
    {
        'Question': "What will be the result of this code?",
        'Code': 'nums = [1, 2, 3, 4, 5]\nnums.pop(3)\nprint(nums)',
        'Options': ["A) [1, 2, 3, 5]", "B) [1, 2, 3, 4]", "C) [1, 2, 3]", "D) Error"]
    },
    {
        'Question': "What is the output?",
        'Code': 'text = "Python is fun"\nprint(text[::2])',
        'Options': ["A) 'Pto sfn'", "B) 'Pto s un'", "C) 'Ptni un'", "D) 'Pto n'"]
    },

    {
        'Question': "What is the output?",
        'Code': 'colors = ["red", "blue", "green"]\nprint("yellow" in colors)',
        'Options': ["A) True", "B) False", "C) None", "D) Error"]
    },
    {
        'Question': "What will be printed by this code?",
        'Code': 'my_list = [5, 6, 7, 8]\nmy_list[1:3] = [1, 2, 3]\nprint(my_list)',
        'Options': ["A) [5, 1, 2, 3, 8]", "B) [5, 1, 2, 3]", "C) [5, 1, 2, 3, 6, 7, 8]", "D) Error"]
    },



  
]


print(quiz_data)
