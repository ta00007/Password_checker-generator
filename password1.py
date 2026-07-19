COMMON_PASSWORDS = [
    "123456", "123456789", "qwerty", "password", "12345", "12345678",
    "111111", "1234567", "sunshine", "qwerty123", "iloveyou", "princess",
    "admin", "welcome", "666666", "abc123", "football", "123123",
    "monkey", "654321", "!@#$%^&*", "charlie", "aa123456", "donald",
    "password1", "qwerty1", "123321", "qwertyuiop", "654123", "666666",
    "121212", "bailey", "freedom", "shadow", "passw0rd", "master",
    "jessica", "michael", "ashley", "qazwsx", "trustno1", "jennifer",
    "letmein", "michelle", "dragon", "baseball", "hunter", "buster",
    "1234", "123456a", "soccer", "hockey", "killer", "george",
    "sexy", "andrew", "charlie1", "superman", "asshole", "fuckyou",
    "1qaz2wsx", "batman", "test", "pass", "flower", "hello",
    "amanda", "loveme", "hello123", "starwars", "666666", "121212",
    "biteme", "matthew", "access", "yankees", "987654321", "dallas",
    "austin", "thunder", "taylor", "matrix", "mobilemail", "mom",
    "monitor", "monitoring", "montana", "moon", "moscow", "changeme",
    "12341234", "welcome1", "login", "admin123", "root", "toor",
    "pass1234", "zaq1zaq1", "password123", "1q2w3e4r", "1q2w3e",
    "aaaaaa", "abcd1234", "google", "iloveyou1"
]

LOWER = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']

UPPER = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

DIGITS = ['0','1','2','3','4','5','6','7','8','9']

SPECIAL_CHARACTER = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-',
                     '.','/',':',';','<','=','>','?','@','[','\\',']',
                     '^','_','`','{','|','}','~']


# for 10 billion password attempts per second
def time(total_possible_password):
    seconds = total_possible_password / 10000000000
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    return f"{seconds:,.0f} seconds, {minutes:,.0f} minutes, {hours:,.0f} hours, {days:,.0f} days, {years:,.0f} years"

# for 100 billion password attempts per second
def time1(total_possible_password):
    seconds = total_possible_password / 100000000000
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    return f"{seconds:,.0f} seconds, {minutes:,.0f} minutes, {hours:,.0f} hours, {days:,.0f} days, {years:,.0f} years"

# for 1 trillion password attempts per second
def time2(total_possible_password):
    seconds = total_possible_password / 1000000000000
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    return f"{seconds:,.0f} seconds, {minutes:,.0f} minutes, {hours:,.0f} hours, {days:,.0f} days, {years:,.0f} years"

# for 100 trillion password attempts per second
def time3(total_possible_password):
    seconds = total_possible_password / 100000000000000
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    return f"{seconds:,.0f} seconds, {minutes:,.0f} minutes, {hours:,.0f} hours, {days:,.0f} days, {years:,.0f} years"


def password_strength(password):
    if password in COMMON_PASSWORDS:
        return "This password is TOO WEAK"

    posibility = 0
    if any(c in LOWER for c in password):
        posibility += 26
    if any(c in UPPER for c in password):
        posibility += 26
    if any(c in DIGITS for c in password):
        posibility += 10
    if any(c in SPECIAL_CHARACTER for c in password):
        posibility += 32

    length = len(password)
    total_possible_password = posibility ** length

    t0 = time(total_possible_password)
    t1 = time1(total_possible_password)
    t2 = time2(total_possible_password)
    t3 = time3(total_possible_password)

    if total_possible_password >= 26339361174458854765907679379456:
        label = "TOO Strong (Never be BROKEN)"
    elif total_possible_password > 367666387654882241806336:
        label = "Strong (Can be broken but takes a long time)"
    elif total_possible_password > 10000000000000000000000:
        label = "Moderate (Can be broken but takes a moderate time)"
    else:
        label = "Weak (Can be broken easily)"

    return f"{label} - \n for 10 billion password attempts per second: \n{t0} \n\n for 1 trillion password attempts per second: \n{t1} \n\n for 100 trillion password attempts per second: \n{t2} \n\n for 1 quadrillion password attempts per second: \n{t3}"


def create_password(length):
    import random
    characters = LOWER + UPPER + DIGITS + SPECIAL_CHARACTER
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    while True:
        password = input("Enter the password: ")
        print(password_strength(password))
        print("Do you want to check another password? (y/n)")
        choice = input().lower()
        if choice != 'y':
            break

    print("If you want then I can create a strong password for you. Do you want me to create a strong password? (y/n)")
    if input().lower() == 'y':
        length = int(input("Enter the length of the password: "))
        print(f"Your strong password is: {create_password(length)}")


if __name__ == "__main__":
    main()