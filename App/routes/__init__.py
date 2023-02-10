from flask import Blueprint


def init_app(app):
    from . import loginPage, newAccount, searchPage

    app.register_blueprint(loginPage.bp)
    app.register_blueprint(searchPage.bp)
    app.register_blueprint(newAccount.bp)
    