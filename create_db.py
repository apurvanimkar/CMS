#from database import Base,engine
#from models import User,Category,Post,Media_Library,Comments

from database import Base,engine
from models import User
print("Creating database ....")
Base.metadata.create_all(engine)


