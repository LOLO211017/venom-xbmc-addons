#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
# Razorex.TmpName
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.config import cConfig
from resources.lib.parser import cParser

#from resources.lib.util import cUtil #outils pouvant etre utiles

import xbmc

SITE_IDENTIFIER = 'streamzzz_com'
SITE_NAME = 'Streamzzz'
SITE_DESC = 'Séries VF & VOSTFR en streaming.'

URL_MAIN = 'http://streamzzz.online/'

URL_SEARCH = (URL_MAIN + '?s=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

SERIE_NEWS = (URL_MAIN + 'episodes/', 'showMovies')
SERIE_SERIES = (URL_MAIN + 'tvshows/', 'showMovies')
SERIE_VIEWS = (URL_MAIN + 'trending/', 'showMovies')
SERIE_NOTES = (URL_MAIN + 'ratings/', 'showMovies')
SERIE_LIST = (True, 'showList')
SERIE_ANNEES = (True, 'showAnnees')
SERIE_GENRES = (True, 'showGenres')

def load():
    oGui = cGui()
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'series_news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries', 'series.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VIEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VIEWS[1], 'Séries (Les plus vues)', 'series_views.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NOTES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NOTES[1], 'Séries (Les mieux notés)', 'series_notes.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_LIST[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_LIST[1], 'Séries (Liste)', 'series_az.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_ANNEES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_ANNEES[1], 'Séries (Par Années)', 'series_annnes.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'series_genres.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def showGenres():#recup les genres et la quantites sur le site
    oGui = cGui()
    oParser = cParser()
    
    oRequestHandler = cRequestHandler(URL_MAIN)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<li class="cat-item cat-item.+?"><a href="([^<]+)" >([^<]+)</a>.+?<i>([^<]+)</i>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sTitle = aEntry[1] + ' (' + (aEntry[2]) + ')'
            sUrl = aEntry[0]
        
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showList():
    oGui = cGui()
	
    liste = []
    liste.append( ['09',URL_MAIN + '?letter=true&s=title-09'] )
    liste.append( ['A',URL_MAIN + '?letter=true&s=title-a'] )
    liste.append( ['B',URL_MAIN + '?letter=true&s=title-b'] )
    liste.append( ['C',URL_MAIN + '?letter=true&s=title-c'] )
    liste.append( ['D',URL_MAIN + '?letter=true&s=title-d'] )
    liste.append( ['E',URL_MAIN + '?letter=true&s=title-e'] )
    liste.append( ['F',URL_MAIN + '?letter=true&s=title-f'] )
    liste.append( ['G',URL_MAIN + '?letter=true&s=title-g'] )
    liste.append( ['H',URL_MAIN + '?letter=true&s=title-h'] )
    liste.append( ['I',URL_MAIN + '?letter=true&s=title-i'] )
    liste.append( ['J',URL_MAIN + '?letter=true&s=title-j'] )
    liste.append( ['K',URL_MAIN + '?letter=true&s=title-k'] )
    liste.append( ['L',URL_MAIN + '?letter=true&s=title-l'] )
    liste.append( ['M',URL_MAIN + '?letter=true&s=title-m'] )
    liste.append( ['N',URL_MAIN + '?letter=true&s=title-n'] )
    liste.append( ['O',URL_MAIN + '?letter=true&s=title-o'] )
    liste.append( ['P',URL_MAIN + '?letter=true&s=title-p'] )
    liste.append( ['Q',URL_MAIN + '?letter=true&s=title-q'] )
    liste.append( ['R',URL_MAIN + '?letter=true&s=title-r'] )
    liste.append( ['S',URL_MAIN + '?letter=true&s=title-s'] )
    liste.append( ['T',URL_MAIN + '?letter=true&s=title-t'] )
    liste.append( ['U',URL_MAIN + '?letter=true&s=title-u'] )
    liste.append( ['V',URL_MAIN + '?letter=true&s=title-v'] )
    liste.append( ['W',URL_MAIN + '?letter=true&s=title-w'] )
    liste.append( ['X',URL_MAIN + '?letter=true&s=title-x'] )
    liste.append( ['Y',URL_MAIN + '?letter=true&s=title-y'] )
    liste.append( ['Z',URL_MAIN + '?letter=true&s=title-z'] )

    for sTitle,sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Lettre [COLOR coral]' + sTitle + '[/COLOR]', 'series_az.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showAnnees():#recuperer automatiquement
    oGui = cGui()
    
    sStart = '<ul class="year scrolling">'
    sEnd = '</div>	<div class="content">'
	
    oParser = cParser()
    
    oRequestHandler = cRequestHandler(URL_MAIN)
    sHtmlContent = oRequestHandler.request()

    sHtmlContent = oParser.abParse(sHtmlContent,sStart,sEnd)

    sPattern = '<li><a href="([^"]+)">(.+?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sUrl = aEntry[0]
            sTitle = aEntry[1]
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sUrl = sSearch
        sPattern = '<div class="result-item">.+?<img src="([^"]+)" alt="(.+?)".+?<a href="([^"]+)">'
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        if '/episodes/' in sUrl:
            sPattern = '<div class="poster"><img src="([^"]+)" alt="(.+?)".+?<a href="([^"]+)">'
        else:
            sPattern = '<div class="poster">.+?<img src="([^"]+)" alt="(.+?)".+?<a href="([^"]+)">'


    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)

        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            
            #L'array affiche vos info dans l'orde de sPattern en commencant a 0
            sTitle = str(aEntry[1])
            sUrl2 = str(aEntry[2])
            sThumb = str(aEntry[0])
            SResume = ''

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
            oOutputParameterHandler.addParameter('sThumbnail',sThumb )

            if '/tvshows/' or '/genre/' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showSerieSaisons', sTitle,'', sThumb, SResume, oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, SResume, oOutputParameterHandler)
                
        cConfig().finishDialog(dialog)

        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    sPattern = '<div class="pagination">.+?<a href="(.+?)".+?/>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        return aResult[1][0]

    return False

def showSerieSaisons():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="numerando">([ 0-9x]+)<\/div>.+?<a href="([^<]+)">(.+?)<\/a>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])

        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            
            sUrl2 = str(aEntry[1])
            sSXXEXX = str(aEntry[0]).replace(' ','').split('x')
            sTitle = "saison " + sSXXEXX[0]  + 'episode' + sSXXEXX[1] + ' ' + str(aEntry[2])
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
            oOutputParameterHandler.addParameter('sThumbnail',sThumb )

            oGui.addTV(SITE_IDENTIFIER, 'showLinks', sTitle,'', sThumb, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showLinks():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumbnail')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<a class="link_a" href="([^"]+)".+?>.+?<img src=".+?">(.+?)</td><td>(.+?)</td><td>(.+?)</td>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])

        dialog = cConfig().createDialog(SITE_NAME)

        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)

            sTitle = sMovieTitle + ' [' + str(aEntry[2]) + '/' + str(aEntry[3]) + '] ' + '[COLOR violet]' + str(aEntry[1]) + '[/COLOR]'
            sUrl2 = str(aEntry[0])

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle',sMovieTitle)
            oOutputParameterHandler.addParameter('sThumbnail',sThumb )

            oGui.addTV(SITE_IDENTIFIER, 'seriesHosters', sTitle,'', sThumb, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def seriesHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="boton reloading"><a href="([^"]+)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    cConfig().log(str(sUrl))
    cConfig().log(str(aResult))
    
    if (aResult[0] == True):
        for aEntry in aResult[1]:

            sHosterUrl = str(aEntry)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
                
    oGui.setEndOfDirectory()
