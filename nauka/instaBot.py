from instapy import InstaPy
from instapy import smart_run
# import instaBot


my_username = "fotograf.koszalin"
my_password = "haslomaslo2"

session = InstaPy(username = my_username, password = my_password, headless_browser = False)

with smart_run(session):
    session.set_relationship_bounds(enabled = True,
                                    delimit_by_numbers=True,
                                    max_followers=200,
                                    min_followers=50,
                                    min_following=50)

session.set_do_follow(True, percentage=100)
session.like_by_tags(['polskadziewczyna','polishgirl'], amount = 20)


