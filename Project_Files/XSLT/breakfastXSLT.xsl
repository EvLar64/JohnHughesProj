<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
 xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs math xd"
    version="3.0">
    <xsl:template match="/">
        
<!--  Breakfast Club Output XSLT - EL -->
        <html>
            <head>
                
                <title><xsl:value-of select="root/scriptInfo/title"/></title>
                <style>
                    body {
                    font-family: 'Tahoma', serif;
                    margin: 20px;
                    line-height: 1.5;
                    background-color: #89CFF0;
                    }
                    h1, h2 {
                    text-align: center;
                    color: #B7410E;
                    }
                    
                    .narration {
                    font-style: italic;
                    color: 	purple;
                    margin: 20px 20px;
                    }
                    
                    .dialogue {
                    white-space: pre-wrap;
                    margin-left: 20em;
                    margin-right: 10em;
                    }
                    
                    .scene-heading {
                    text-transform: uppercase;
                    font-weight: bold;
                    margin: 20px;
                    }
                    
                    hr {
                    border-top: 2px solid gold;
                    margin: 20px;
                    }
                    
                    .toc {
                    font-size: 14px;
                    color: #B7410E;
                    }
                    .quote {
                    font-size: 18px;
                    color: #B7410E;
                    margin-left: 15em;
                    margin-right: 15em;
                    }
                    

                </style>
            </head>
            <nav>
                
            </nav>
            <body>
                <h1><u><xsl:value-of select="root/scriptInfo/title"/> (1985)</u></h1>
                <h2>Written and Directed by <a href="https://www.imdb.com/name/nm0000455/?ref_=nv_sr_srsg_0_tt_0_nm_8_in_0_q_john%2520hughes"><xsl:value-of select="root/scriptInfo/dir" /></a></h2>
                
                <div class="toc">
                    <h4><i>Scene Finder</i>:</h4>
                    <strong><div class="scene-string">
                        <xsl:for-each select="root/script/scene">
                            <xsl:variable name="sceneNumber" select="position()"/><a href="#scene{$sceneNumber}"><xsl:value-of select="$sceneNumber"/> | </a>
                        </xsl:for-each>
                    </div></strong>
                </div>
                
                <div class="cast-list">
                    <h4><i>Cast List (and links to first scenes)</i>:</h4>
                    <ul>
                        <li>Emilio Estevez as <a href="#scene4">Andrew Clark</a></li>
                        <li>Paul Gleason as <a href="#scene6">Richard Vernon</a></li>
                        <li>Anthony Michael Hall as <a href="#scene1">Brian Johnson</a></li>
                        <li>John Kapelos as <a href="#scene13">Carl</a></li>
                        <li>Judd Nelson as <a href="#scene6">John Bender</a></li>
                        <li>Molly Ringwald as <a href="#scene2">Claire Standish</a></li>
                        <li>Ally Sheedy as a <a href="#scene13">Allison Reynolds</a></li>
                    </ul>
                </div>
                
                <strong><div class="quote">
                    <xsl:apply-templates select="root/scriptInfo/quote"/>
                </div></strong>
                
                <div>
                    <xsl:apply-templates select="root/script/scene"/>
                </div>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="scene">
        <xsl:variable name="sceneNumber" select="position()"/>
        <div class="scene">
            <p class="scene-heading" id="scene{$sceneNumber}">SCENE <xsl:value-of select="$sceneNumber"/><a href="#top">^</a>
            </p>
            <xsl:apply-templates select="*" />
            <hr/>
        </div>
    </xsl:template>
    
    <xsl:template match="narr">
        <p class="narration"><xsl:value-of select="normalize-space()"/></p>
    </xsl:template>
    
    <xsl:template match="d">
        <p class="dialogue">
            <xsl:value-of select="."/>
        </p>
    </xsl:template>
   
    <xsl:template match="desc">
        <span class="description"> <xsl:value-of select="normalize-space()"/></span>
    </xsl:template>
    
    <xsl:template match="text()">
        <xsl:value-of select="normalize-space()"/>
    </xsl:template>
</xsl:stylesheet>