START = \
"""
Assalomu alaykum 
"""
age = \
"""
yoshingizni kiriting
"""

name = \
"""
6235
Ismingizni kiriting❗️
""" 

phone = \
"""
ILTIMOS telefon raqamingizni yozib yuboring yoki pasatdagi telefon raqam yuborish tugmasini bosing
"""
kurslar = \
"""
Qaysi kursni tanlamoqchisiz!
""" 
field = \
"""
Arizangiz qabul qilinishi uchun tasdiqlash tugmasini bosing 
"""


def check(**kwargs):
    application = ''

    application += f"MA'LUMOT:\n"
    application += f"Telefon:{kwargs['phone']}\n"
    application += f"ism:{kwargs['name']}\n"
    application +=f"yosh:{kwargs['age']}\n"
    application +=f"kurslar:{kwargs['course']}\n"


    return application

