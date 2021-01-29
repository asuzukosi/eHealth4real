import re

# Input validators to validate user input


# Validate username with regular expressions
def validate_username(txt):
    if len(txt) < 5:
        return "Length of username should be at least 5 characters"

    val = re.search("\s", txt)

    if not val:
        val = re.match("^[a-zA-Z]", txt)
        if val:
            val = re.search("[0-9]", txt)
            if val:
                return True
            else:

                return "Username should have at least one number"

        else:

            return "User name should start with alphabet"

    else:

        return "Username should not have whitespaces"


# Validate password with regular expressions
def validate_password(txt):
    if len(txt) < 8:
        return "Length of password should be at least 8 characters"

    val = re.search("\s", txt)

    if not val:
        val = re.search("[a-zA-Z]", txt)
        if val:
            val = re.search("[0-9]", txt)
            if val:
                return True
            else:

                return "Password should have at least one number"

        else:

            return "Password should contain alphabets"

    else:

        return "Password should not have whitespaces"


# Validate name with regular expressions
def validate_name(txt):

    val = re.search("\s", txt)

    if not val:
        val = re.search('[0-9]', txt)

        if not val:
            val = re.match('^[A-Z]', txt)
            if val:
                return True
            else:
                return "firstname and lastname must begin with uppercase"

        else:
            return "firstname and lastname should not contain any number"

    else:

        return "firstname and lastname should not have whitespaces"


# Validate all inputs at once
def validate_all(username, password, firstname, lastname):
    errors = set()

    if validate_username(username) != True:
        errors.add(validate_username(username))

    if validate_password(password) != True:
        errors.add(validate_password(password))

    if validate_name(firstname) != True:
        errors.add(validate_name(firstname))

    if validate_name(lastname) != True:
        errors.add(validate_name(lastname))

    if len(errors) == 0:
        return True

    else:
        return errors


print(validate_all("kiosi34", "howa6123", "kosi", "asuzu"))
