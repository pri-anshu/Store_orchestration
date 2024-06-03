class new_user:
    def new_user(z):
        a = {}
        print("System--> Adding new store admin")

        print("System--> Enter the new username:")
        new_username = input("{}--> ".format(z))

        print("System--> Password for new user:")
        new_password = input("{}--> ".format(z))

        a[new_username] = new_password
        return a
