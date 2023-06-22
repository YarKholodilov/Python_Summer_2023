import keyword
keys_list = keyword.kwlist
text = input().replace(',', ' ,').replace('.', ' .').split()
answer = []
res = ''

for word in text:
    if word in keys_list:
        answer.append('<kw>')
    else:
        answer.append(word)
res = ' '.join(map(str, answer)).replace(' ,', ',').replace(' .', '.')
print(res)



#An example of something you can’t do with Python keywords is assign something to them. If you try, then you’ll get a SyntaxError.
# You won’t get a SyntaxError if you try to assign something to a built-in function or type, but it still isn’t a good idea.
# For a more in-depth explanation of ways keywords can be misused, check out Invalid Syntax in Python: Common Reasons for SyntaxError.
#That's true'