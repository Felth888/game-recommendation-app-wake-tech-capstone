from App.models.userModels import User

def test_new_user():
    """

    GIVEN a User model
    WHEN a new User is created
    THEN check the username, email, password, and birthdate fields are defined correctly
    """

    user = User(user_name='bob', email='bob@gmail.com', birthdate='2000-12-22')
    user.set_password('password_to_hash')
    assert user.user_name == 'bob'
    assert user.email == 'bob@gmail.com'
    assert user.password != 'password_to_hash'
    assert user.birthdate == '2000-12-22'