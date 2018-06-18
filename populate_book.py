from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import User, Genre, Base, BookItem

engine = create_engine('sqlite:///new_book_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
# the first user
User1 = User(name="Kiran Ch", email="chigurupatikiran97@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png')
session.add(User1)
session.commit()

# Poetry Books
genre1 = Genre(user_id=1, name="Poetry", description = "Poetry is an art form in which human language is used for its aesthetic qualities in addition to, or instead of, its notional and semantic content.")

session.add(genre1)
session.commit()

book = BookItem(user_id=1, name="Where the Sidewalk Ends", description="Children\'s poetry collection written and illustrated by Shel Silverstein. Published by Harper and Row Publishers.",
                     type = "eBook", price="$2.50", author="Shel Silverstein", genre=genre1)

session.add(book)
session.commit()


book1 = BookItem(user_id=1, name="Leaves of Grass", description="The seminal work of one of the most influential writers of the nineteenth century.",
                     type="hardCopy",price="$3.50", author="Walt Whitman", genre=genre1)

session.add(book1)
session.commit()

book2 = BookItem(user_id=1, name="Howl and Other Poems", description="The single most influential poetic work of the post-World War II era, with over 900,000 copies now in print.",
                     type="hardCopy",price="$5.50", author="Allen Ginsberg", genre=genre1)

session.add(book2)
session.commit()

book3 = BookItem(user_id=1, name="Ariel", description="The beloved poet\'s brilliant, provoking, and always moving poems, including Ariel",
                     type = "eBook",price="$3.50", author="Sylvia Plath", genre=genre1)

session.add(book3)
session.commit()


# Fantasy books
genre2 = Genre(user_id=1, name="Fantasy", description="Fantasy is a genre of fiction set in a fictional universe, often, but not always, without any locations, events, or people referencing the real world.")

session.add(genre2)
session.commit()
book4 = BookItem(user_id=1, name="The Chronicles of Narnia", description="Journeys to the end of the world, fantastic creatures, and epic battles between good and evil",
                     type="hardCopy",price="$3.50", author="C.S. Lewis ", genre=genre2)

session.add(book4)
session.commit()

book5 = BookItem(user_id=1, name="The Final Empire", description="In a world where ash falls from the sky, and mist dominates the night, an evil cloaks the land and stifles all life.",
                     type = "eBook",price="$5.50", author="Brandon Sanderson", genre=genre2)

session.add(book5)
session.commit()

# Horror books
genre3 = Genre(user_id=1, name="Horror", description="Horror is a genre of fiction which is intended to, or has the capacity to frighten, scare, disgust, or startle its readers or viewers by inducing feelings of horror and terror. ")

session.add(genre3)
session.commit()
book6 = BookItem(user_id=1, name="Into the Drowning Deep", description="Seven years ago, the Atargatis set off on a voyage to the Mariana Trench to film a mockumentary bringing to life ancient sea creatures of legend.",
                     type="hardCopy",price="$7.50", author="Mira Grant", genre=genre3)

session.add(book6)
session.commit()
book7= BookItem(user_id=1, name="Regression", description="Plagued by ghastly waking nightmares, Adrian reluctantly agrees to past life regression hypnotherapy. ",
                     type = "eBook",price="$6.50", author="Cullen Bunn", genre=genre3)

session.add(book7)
session.commit()

print "DB is populated"
