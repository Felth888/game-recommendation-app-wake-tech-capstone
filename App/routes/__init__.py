from flask import Blueprint


def init_app(app):
    from . import loginPage, newAccount, searchPage, userProfile

    app.register_blueprint(loginPage.bp)
    app.register_blueprint(searchPage.bp)
    app.register_blueprint(newAccount.bp)
    app.register_blueprint(userProfile.bp)
    