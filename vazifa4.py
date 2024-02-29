# 1-masala
# Shunday kod yozingki. dasturad while operatoridan foydalaning.
# Har safar while aylanganida ism so`rasin va salom bersin.
# agar ism o`rniga stop kiritsa dastru to`xtasin

# while True:
#     ism=input('Ismingiz nima: ')
#     print(f'Assalomu alaykum {ism}')
#     if ism=='stop':
#         break

# 2-masala
# Shunday kod yozingki. dasturda while yoki for operatoridan foydalaning.
# Dasturda bitta raqam kiritishni so`rang va shu raqamgacha bo`lgan  3ta juft sonini print qiling

son=int(input('Sonni kiriting: '))
sonn=[]
son_n=[]
if son%2==0:
    for i in range(0, son,2):
        sonn.append(i)
    print(sonn[::-1][0],sonn[::-1][1],sonn[::-1][2])
elif son%2==1:
    for i in range(1, son+1,2):
        natija=(i-1)
        son_n.append(natija)
    print(son_n[::-1][0],son_n[::-1][1],son_n[::-1][2])

# 3-masala
# Shunday kod yozingki. dasturda for operatoridan foydalaning.
# Dasturda ism kiritishni so`rang va shu ismdagi birinchi 3ta undosh harfni print qiling
# ism = input('ism kiriting:')
# unlilar = 'aeiou'
# data=[]
# for i in ism:
#     if i not in unlilar:
#         data.append(i)
#
# print(data[:3])

# 4-misol
# Shunday kod yozingki. dasturda for operatoridan foydalaning.
# Dasturda ism kiritishni so`rang va shu ismdagi unlilarni faqat bitta nusxada chop eting

# ism = input('ism kiriting:')
# unlilar = 'aeiou'
# data=[]
# for i in ism:
#     if i  in unlilar:
#         data.append(i)
#
# print(data)

# 5-misol
# Shunday kod yozingki. dasturda for operatoridan foydalaning.
# Dasturda ism kiritishni so`rang va shu ismdagi undoshlarni faqat bitta nusxada chop eting

# ism = input('ism kiriting:')
# unlilar = 'aeiou'
# data=[]
# for i in ism:
#     if i not in unlilar:
#         data.append(i)
#
# print(data)

# 6-misol
# Shunday kod yozingki. dasturda for operatoridan foydalaning.
# Dasturda ism kiritishni so`rang va shu ismdagi barcha harflarni faqat bitta nusxada chop eting

# ism = input('ism kiriting:')
# data=[]
# for i in ism:
#     data.append(i)
# print(data)















