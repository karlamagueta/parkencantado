import os

DB_NAME = "test.db"
os.environ["PARK_database__path"] = DB_NAME


def delete_testing_database_if_exists():
    if os.path.exists(DB_NAME):
        os.unlink(DB_NAME)


def pytest_sessionstart(session):
    """Delete test database before all tests starts running"""
    delete_testing_database_if_exists()


def pytest_sessionfinish(session, exitstatus):
    """Delete test database after test run if exit successfully
    in case of error, db is kept for debugging.
    """
    if exitstatus == 0:
        delete_testing_database_if_exists()

