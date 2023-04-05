def cleanUser(user):
    userClean = user.replace('_',' ')
    userClean = userClean.title()
    return userClean