# keyword arguments

def funckeyword(arg1, arg2='Genesis', arg3='InSoft'):
  print("arg1=", arg1, "arg2=", arg2, "arg3=", arg3)

funckeyword(10)
funckeyword(arg1="value1")
funckeyword(10, arg2="Qualcomm")
funckeyword(10, arg3="Qualcomm", arg2="Genesis")
funckeyword(arg3="Hyderabad", arg1="value1")
