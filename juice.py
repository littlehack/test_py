import  re


a = "rewr890ewfkdfg900dasd"

s = re.compile(r"\d+")
b = s.findall(a)

print(b)