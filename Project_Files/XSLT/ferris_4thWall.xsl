<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns="http://www.w3.org/2000/svg"
    exclude-result-prefixes="xs math"
    version="3.0">

    <xsl:output method="xml" indent="yes"/>
    
    <xsl:variable name="totalLines" select="count(/script/scene/d)"/>
    
    <xsl:template match="/root">
        <svg width="200vw" height="110vw" xmlns="http://www.w3.org/2000/svg">
            
            <rect width="50%" height="50%" fill="#c8f8a7"/>
            
            <g transform="translate(220,250)">
            
            <line x1="50" y1="100" x2="950" y2="100" stroke="black" stroke-width="2"/>
            
            <text x="500" y="30" font-size="16" fill="black" font-family="Verdana" font-weight="bold" text-anchor="middle">
                Timeline of 4th-Wall-Breaking Lines Within "Ferris Bueller's Day Off"
            </text>
                <text x="20" y="75" font-size="13" fill="black" font-family="Verdana" font-weight="bold" text-anchor="middle">
                    Start
                </text>
                <text x="975" y="75" font-size="13" fill="black" font-family="Verdana" font-weight="bold" text-anchor="middle">
                    End
                </text>
                <text x="400" y="140" font-size="11" fill="black" font-family="Verdana" font-weight="bold" text-anchor="middle">
                    39 Lines of Dialogue Directed Towards the Camera
                </text>
                <text x="380" y="160" font-size="11" fill="black" font-family="Verdana" font-weight="bold" text-anchor="middle">
                    298 Total Ferris Lines
                </text>
                <text x="380" y="180" font-size="11" fill="black" font-family="Verdana" font-weight="bold" text-anchor="middle">
                    = 13.09%
                </text>
            </g>
            
            <xsl:variable name="totalLines" select="count(script/scene/d)"/>
            
            <xsl:for-each select="script/scene/d">
                <xsl:variable name="fourthWall" select="position()"/>
                
                <xsl:variable name="x" select="50 + (($fourthWall - 1) * 900 div $totalLines)"/>
                
                <g transform="translate(220,250)"><line x1="{$x}" y1="100" x2="{$x}" y2="70" stroke="lightgray" stroke-width="2"/></g>
                
                <xsl:if test="@wall='true'">
                    <g transform="translate(220,250)"><line x1="{$x}" y1="100" x2="{$x}" y2="50" stroke="red" stroke-width="2"/></g>
                </xsl:if>
            </xsl:for-each>
            
            <image href="https://images.fineartamerica.com/images/artworkimages/medium/3/ferris-bueller-save-ferris-american-button-handsley-nguyen-transparent.png" x="225" y="150" width="200" height="150"/>
            <g transform="rotate(11)"><image href="https://automedia.revsinstitute.org/wp-content/uploads/2021/02/ferris-sm1.png" x="1100" y="-50" width="200" height="150"/>
            </g>
            
        </svg>
    </xsl:template>
</xsl:stylesheet>