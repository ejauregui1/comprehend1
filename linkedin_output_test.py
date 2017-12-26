from linkedin import linkedin
from settings import (CLIENT_ID, CLIENT_SECRET)

RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Open this url in the browser

print (authentication.authorization_url)
application = linkedin.LinkedInApplication(authentication)
