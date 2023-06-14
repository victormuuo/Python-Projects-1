def Slicer():
    print("Welcome to the email slicer")
    print("")

    email_input=input("Input you email address: ")

    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split('.')

    print("Username:",username)
    print("Domain:",domain)
    print("Extension:",extension)
while True:    
    Slicer()