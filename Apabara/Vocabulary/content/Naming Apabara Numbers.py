
unes = {
  0:"nul",
  1:"un",
  2:"du",
  3:"san",
  4:"xar",
  5:"kin",
  6:"xes",
  7:"sep",
  8:"ba",
  9:"nin"
}

des_powa = {
  0:"mil",
  1:"des",
  2:"xen"
}

miliones = {
  0:"",
  1:"milion",
  2:"ilion"
}

def func(num:int)->str:
  if num == 0:
    return "nul"
  else:
    s = ""
    n = 0
    while 0 < num:
      if n > 0:
        if n % 6:
          pass
      s = unes[num % 10] + des_powa[n % 3] + " " + s
      n += 1
      num //= 10
  return s

print(func(12345))
