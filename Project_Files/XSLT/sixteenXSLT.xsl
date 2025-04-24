<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
 xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs math xd"
    version="3.0">
    <xsl:template match="/">
        
<!--  Sixteen Candles Output XSLT - EL -->
        <html>
            <head>
                <title><xsl:value-of select="root/scriptInfo/title"/></title>
                <style>
                    body {
                    font-family: 'Georgia', sans-serif;
                    margin: 20px;
                    line-height: 1.5;
                    background-color: #B0B89F;
                    }
                    h1, h2 {
                    text-align: center;
                    color: #FF5733;
                    }
                    
                    .narration {
                    white-space: pre-wrap;
                    font-style: italic;
                    color: #1D4E89;
                    margin: 20px 20px;
                    }
                    
                    .dialogue {
                    white-space: pre-wrap;
                    margin-left: 20em;
                    margin-right: 10em;
                    color: #9B1B30;
                    }
                    
                    .scene-heading {
                    text-transform: uppercase;
                    font-weight: bold;
                    margin: 20px;
                    }
                    
                    hr {
                    border-top: 2px solid #D3D3D3;
                    margin: 20px;
                    }
                    
                    .toc {
                    font-size: 10.5px;
                    color: black;
                    }

                </style>
            </head>
            <nav>
                
            </nav>
            <body>
                <h1><u><xsl:value-of select="root/scriptInfo/title"/> (1984)</u></h1>
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
                        <li>Molly Ringwald as <a href="#scene5">Samantha</a></li>
                        <li>Anthony Michael Hall as <a href="#scene23">Geek</a></li>
                        <li>Justin Henry as <a href="#scene72">Mike Baker</a></li>
                        <li>Michael Schoeffling as <a href="#scene1">Jake</a></li>
                        <li>Haviland Morris as <a href="#scene1">Caroline</a></li>
                        <li>Gedde Watanabe as <a href="#scene1">Long Duk Dong</a></li>
                        <li>Blanche Baker as <a href="#scene1">Ginny</a></li>
                    </ul>
                </div>
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