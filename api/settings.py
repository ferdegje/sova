__author__ = 'jeanmarie'

from models.people import people
from models.accounts import accounts
from models.spaceships import spaceships

DOMAIN = {
    'people': people,
    'accounts': accounts,
    'spaceships': spaceships
}

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']