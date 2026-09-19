def intToRoman(num):
    roman = ""

    ref = {1: "I",
           4: "IV", 5: "V", 
           9: "IX", 10: "X", 
           40: "XL", 50: "L", 
           90: "XC", 100: "C", 
           400: "CD", 500: "D", 
           900: "CM", 1000: "M"}

    keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000][::-1]

    for n in keys:
        while n <= num:
            print(num, n)
            roman += ref[n]
            num -= n

    return roman

print(intToRoman(3749))
print(intToRoman(58))
print(intToRoman(1994))
