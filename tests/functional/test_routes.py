from App import create_app

def test_search_page():
    """

    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Play This" in response.data
        # assert b"Search page is working!" in response.data




# blueprint for tests
def test_search_with_fixture(test_client):
# test_client.get to grab route
    response = test_client.get('/')
    # status code for success is 200
    assert response.status_code == 200
    # just a simple search for text in the response, we can get more in depth however
    assert b"Play This" in response.data