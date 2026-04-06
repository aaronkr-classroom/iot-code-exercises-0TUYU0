# 5_func.py

def return_info(name, phone, address, email):
    contact_info = f"연락처:\t{phone}\n이메일:\t{email}"
    return f"이 름:\t{name}\n{contact_info}\n주 소:\t{address}"

def print_info(name, phone, address, email = ""):
    contact_info = f"연락처:\t{phone}\n이메일:\t{email}"
    print(f"이 름:\t{name}\n{contact_info}\n주 소:\t{address}")
    
print_info("Aaron", "010-1234-5678", "CheongJu")
print()

person = return_info(email="asdf1234@gmail.com", phone="010-1234-5678",
                     address="CheongJu", name="Aaron")

print(person)