from flask import Blueprint


def init_app(app):
    from . import loginPage, newAccount, searchPage, userProfile, recommendationPage, gameLibrary, userWishlist, updatePassword

    app.register_blueprint(loginPage.bp)
    app.register_blueprint(searchPage.bp)
    app.register_blueprint(newAccount.bp)
    app.register_blueprint(userProfile.bp)
    app.register_blueprint(recommendationPage.bp)
    app.register_blueprint(gameLibrary.bp)
    app.register_blueprint(userWishlist.bp)
    app.register_blueprint(updatePassword.bp)
