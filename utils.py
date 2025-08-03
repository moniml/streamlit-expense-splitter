def prompt_user_list():
    names = input("Enter participant names (comma-separated): ")
    return [name.strip() for name in names.split(",")]
