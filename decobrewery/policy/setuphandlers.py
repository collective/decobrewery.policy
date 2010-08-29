from Products.CMFCore.utils import getToolByName
from plone.dexterity.utils import createContent
from transaction import commit

def setup_site_content(site, logger):
    ''' Add a site-content folder and an agreement page '''
    wf_tool = getToolByName(site, 'portal_workflow')
    if 'beers' not in site:
        # create site contents folder
        page = createContent("plone.page")
        page.id = 'beers'
        #page.title = u'Beer Crate'
        site._setObject('beers', page)
        commit()
        logger.info('Created Beers folder')
    else:
        logger.info('Beers folder already exists, not creating it')
        page = site['beers']
        
    if 'leffe-blond' not in page:
        beer = createContent("decobrewery.beer")
        beer.id = 'leffe-blond'
        #beer.title = u'Leffe Blond'
        page._setObject('leffe-blond', beer)
        commit()
        logger.info('created Leffe Blond beer')
    else:
        logger.info('Leffe Blond beer already exists, not creating it')


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('decobrewery.policy_various.txt') is None:
        return

    # Add additional setup code here
    site = context.getSite()
    logger = context.getLogger('decobrewery.policy')
    logger.info('Skipping site content creation for now')
    # skip for now since createContent doesn't work too well
    #setup_site_content(site, logger)