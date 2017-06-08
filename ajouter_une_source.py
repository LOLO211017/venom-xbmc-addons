#-*- coding: utf-8 -*-
#Venom.
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.config import cConfig
from resources.lib.util import cUtil
import re

#Ce site a des probleme en http/1.1 >> incomplete read error
import httplib
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

SITE_IDENTIFIER = 'adkami_old'
SITE_NAME = 'ADKami.old'
SITE_DESC = 'Bienvenue sur ADKami un site Animés (Manga)& Séries en streaming.'

URL_MAIN = 'http://www.adkami.com/'

ANIM_ANIMS = (URL_MAIN + 'video?recherche=&version=0&type2=0', 'showMovies')
ANIM_VFS = (URL_MAIN + 'video?recherche=&version=1&type2=0', 'showMovies')
ANIM_VOSTFRS = (URL_MAIN + 'video?recherche=&version=2&type2=0', 'showMovies')

SERIE_SERIES = (URL_MAIN + 'video?recherche=&version=0&type2=1', 'showMovies')
SERIE_VFS = (URL_MAIN + 'video?recherche=&version=1&type2=1', 'showMovies')
SERIE_VOSTFRS = (URL_MAIN + 'video?recherche=&version=2&type2=1', 'showMovies')

MANGA_MANGAS = (URL_MAIN + 'video?recherche=&version=0&type2=3', 'showMovies')
MANGA_VFS = (URL_MAIN + 'video?recherche=&version=1&type2=3', 'showMovies')
MANGA_VOSTFRS = (URL_MAIN + 'video?recherche=&version=2&type2=3', 'showMovies')

URL_SEARCH = (URL_MAIN + 'video?recherche=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

def load():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_ANIMS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_ANIMS[1], 'Animés', 'animes.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_VFS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_VFS[1], 'Animés (VF)', 'animes_vf.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_VOSTFRS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_VOSTFRS[1], 'Animés (VOSTFR)', 'animes_vostfr.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('type2', 0)
    oOutputParameterHandler.addParameter('title', 'Animés')
    oGui.addDir(SITE_IDENTIFIER, 'showLang', 'Animés (A-Z)', 'animes_az.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('type2', 0)
    oOutputParameterHandler.addParameter('title', 'Animés')
    oGui.addDir(SITE_IDENTIFIER, 'showLangGenre', 'Animés (Genres)', 'animes_genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VFS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VFS[1], 'Séries (VF)', 'series_vf.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFRS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFRS[1], 'Séries (VOSTFR)', 'series_vostfr.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('type2', 1)
    oOutputParameterHandler.addParameter('title', 'Séries')
    oGui.addDir(SITE_IDENTIFIER, 'showLang', 'Séries (A-Z)', 'series_az.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('type2', 1)
    oOutputParameterHandler.addParameter('title', 'Séries')
    oGui.addDir(SITE_IDENTIFIER, 'showLangGenre', 'Séries (Genres)', 'series_genres.png', oOutputParameterHandler)
	
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MANGA_MANGAS[0])
    oGui.addDir(SITE_IDENTIFIER, MANGA_MANGAS[1], 'Mangas', 'animes.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MANGA_VFS[0])
    oGui.addDir(SITE_IDENTIFIER, MANGA_VFS[1], 'Mangas (VF)', 'vf.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MANGA_VOSTFRS[0])
    oGui.addDir(SITE_IDENTIFIER, MANGA_VOSTFRS[1], 'Mangas (VOSTFR)', 'vostfr.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('type2', 3)
    oOutputParameterHandler.addParameter('title', 'Mangas')
    oGui.addDir(SITE_IDENTIFIER, 'showLang', 'Mangas (A-Z)', 'az.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('type2', 3)
    oOutputParameterHandler.addParameter('title', 'Mangas')
    oGui.addDir(SITE_IDENTIFIER, 'showLangGenre', 'Mangas (Genres)', 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def showLang():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sType2 = oInputParameterHandler.getValue('type2')
    sTitle = oInputParameterHandler.getValue('title')
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('version', 0)
    oOutputParameterHandler.addParameter('type2', sType2)
    oGui.addDir(SITE_IDENTIFIER, 'showAZ', sTitle + ' A-Z', 'lang.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('version', 1)
    oOutputParameterHandler.addParameter('type2', sType2)
    oGui.addDir(SITE_IDENTIFIER, 'showAZ', sTitle + ' A-Z VF', 'vf.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('version', 2)
    oOutputParameterHandler.addParameter('type2', sType2)
    oGui.addDir(SITE_IDENTIFIER, 'showAZ', sTitle + ' A-Z VOSTFR', 'vostfr.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()

def showLangGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sType2 = oInputParameterHandler.getValue('type2')
    sTitle = oInputParameterHandler.getValue('title')
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('version', 0)
    oOutputParameterHandler.addParameter('type2', sType2)
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', sTitle + ' Genres', 'lang.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('version', 1)
    oOutputParameterHandler.addParameter('type2', sType2)
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', sTitle + ' Genre VF', 'vf.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oOutputParameterHandler.addParameter('version', 2)
    oOutputParameterHandler.addParameter('type2', sType2)
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', sTitle + ' Genre VOSTFR', 'vostfr.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()

def showAZ():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sVersion = oInputParameterHandler.getValue('version')
    sType2 = oInputParameterHandler.getValue('type2')
    
    sUrl = URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&type2=' + str(sType2) + '#123'
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('AZ', '123')
    oGui.addDir(SITE_IDENTIFIER, 'showMoviesAZ', '123', 'az.png', oOutputParameterHandler)
    for i in string.ascii_uppercase:
        sUrl = URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&type2=' + str(sType2) + '#' + i
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('AZ', i)
        oGui.addDir(SITE_IDENTIFIER, 'showMoviesAZ', i, 'az.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()

def showMoviesAZ():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sAZ = oInputParameterHandler.getValue('AZ')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = '</li><li><a href="([^<]+)">.+?<span class="bold">(.+?)</span>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            if len(sAZ)>0 and aEntry[1].upper()[0] == sAZ:

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
                oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[1]))
                oGui.addTV(SITE_IDENTIFIER, 'showEpisode', aEntry[1], '', '', '', oOutputParameterHandler)
        
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sVersion = oInputParameterHandler.getValue('version')
    sType2 = oInputParameterHandler.getValue('type2')

    liste = []
    liste.append( ['Action',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=1&type2=' + str(sType2)] )
    liste.append( ['Aventure',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=2&type2=' + str(sType2)] )
    liste.append( ['Amour & Amitié',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=3&type2=' + str(sType2)] )
    liste.append( ['Combat',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=4&type2=' + str(sType2)] )
    liste.append( ['Comédie',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=5&type2=' + str(sType2)] )
    liste.append( ['Contes & Récits',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=6&type2=' + str(sType2)] )
    liste.append( ['Cyber & Mecha',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=7&type2=' + str(sType2)] )
    liste.append( ['Dark Fantasy',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=8&type2=' + str(sType2)] )
    liste.append( ['Drame',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=9&type2=' + str(sType2)] )
    liste.append( ['Ecchi',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=10&type2=' + str(sType2)] )
    liste.append( ['Éducatif',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=11&type2=' + str(sType2)] )
    liste.append( ['Énigme & Policier',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=12&type2=' + str(sType2)] )
    liste.append( ['Épique & Héroique',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=13&type2=' + str(sType2)] )
    liste.append( ['Espace & Sci-Fiction',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=14&type2=' + str(sType2)] )
    liste.append( ['Familial & Jeunesse',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=15&type2=' + str(sType2)] )
    liste.append( ['Fantastique & Mythe',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=16&type2=' + str(sType2)] )
    liste.append( ['Hentai',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=17&type2=' + str(sType2)] )
    liste.append( ['Historique',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=18&type2=' + str(sType2)] )
    liste.append( ['Horreur',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=19&type2=' + str(sType2)] )
    liste.append( ['Magical Girl',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=20&type2=' + str(sType2)] )
    liste.append( ['Musical',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=21&type2=' + str(sType2)] )
    liste.append( ['Psychologique',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=22&type2=' + str(sType2)] )
    liste.append( ['Sport',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=23&type2=' + str(sType2)] )
    liste.append( ['Tranche de vie',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=24&type2=' + str(sType2)] )
    liste.append( ['Shôjo-Ai',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=25&type2=' + str(sType2)] )
    liste.append( ['Shônen-Ai',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=26&type2=' + str(sType2)] )
    liste.append( ['Yaoi /BL',URL_MAIN + 'video?recherche=&version=' + str(sVersion) + '&genre3=27&type2=' + str(sType2)] )

    for sTitle,sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = '<li><a href="([^<]+)">.+?<span class="bold">(.+?)</span></p>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[1]))
            if 'type2=1' in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showEpisode', aEntry[1], 'series.png', '', '', oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'showEpisode', aEntry[1], 'animes.png', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    if not sSearch:
        oGui.setEndOfDirectory()

def showEpisode():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    sThumb = ''
    sComm = ''
    
    #info anime
    try:
        oParser = cParser()
        sPattern = '<img src="([^<]+)" alt="[^<]+" id="image_manga".+?/>.+?<th.+?><p>(.+?)</p></th>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            sThumb = aResult[1][0][0]
            sComm = aResult[1][0][1]
    except:
        pass
    
    oParser = cParser()
    sPattern = 'line-height:200px;font-size:26px;text-align:center;">L.anime est licencié<.p>'
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        dialog = cConfig().createDialog(SITE_NAME)
        cConfig().updateDialog(dialog, 1)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
        oGui.addDir(SITE_IDENTIFIER, 'showEpisode', '[COLOR red]'+'Animé licencié'+'[/COLOR]', 'host.png', oOutputParameterHandler)
        
        cConfig().finishDialog(dialog)
    
    else:
        
        #sPattern = '<li style.+?>(.+?)</li>|<li title=""><a href="([^<]+)">([^<]+)</a></li>'
        sPattern = '<li style.+?>(.+?)<.li>|<li title="[^>]*?"><a href="(http:\/\/www.adkami.com.+?)".*?>([^<]+)<.a><.li>'
        
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            total = len(aResult[1])
            dialog = cConfig().createDialog(SITE_NAME)
            for aEntry in aResult[1]:
                cConfig().updateDialog(dialog, total)
                if dialog.iscanceled():
                    break
                
                if aEntry[0]:
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
                    oGui.addDir(SITE_IDENTIFIER, 'showEpisode', '[COLOR red]'+str(aEntry[0])+'[/COLOR]', 'films.png', oOutputParameterHandler)
                else:
                    sTitle = sMovieTitle + ' ' + aEntry[2]
                    sTitle = re.sub(' vf',' [VF]',sTitle,re.IGNORECASE)
                    sTitle = re.sub(' vostfr',' [VOSTFR]',sTitle,re.IGNORECASE)
                    sDisplayTitle = cUtil().DecoTitle(sTitle)
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oGui.addTV(SITE_IDENTIFIER, 'showHosters', sDisplayTitle , 'films.png',sThumb, sComm, oOutputParameterHandler)
           
            cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '</div><iframe.+?src="(.+?)"|<a rel="nofollow" target="_back" href="([^"]+)" [^<>]+">[^<>]+Redirection<\/a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            if (aEntry[0]):
                sHosterUrl = str(aEntry[0])
            else:
                sHosterUrl = str(aEntry[1])
                
            oHoster = cHosterGui().checkHoster(sHosterUrl)
        
            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, '')
    
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
