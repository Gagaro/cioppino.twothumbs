from plone.indexer.decorator import indexer
from interfaces import ILoveThumbsDontYou
import rate


@indexer(ILoveThumbsDontYou)
def positive_ratings(object, **kw):
    return rate.getTotalPositiveRatings(object)
