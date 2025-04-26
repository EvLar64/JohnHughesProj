<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:output method="text" indent="no"/>
    <xsl:variable name="tab" as="xs:string">
        <xsl:text>&#x9;</xsl:text>
    </xsl:variable>
    
    <xsl:variable name="newline" as="xs:string">
        <xsl:text>&#10;</xsl:text>
    </xsl:variable>
    
    <xsl:template match="/">
        <xsl:text>char</xsl:text>
        <xsl:value-of select="$tab"/>
        <xsl:text>desc</xsl:text>
        <xsl:value-of select="$tab"/>
        <xsl:text>sceneNum</xsl:text>
        <xsl:value-of select="$tab"/>
        <xsl:text>sceneMarker</xsl:text>
        <xsl:value-of select="$newline"/>
        
        <xsl:apply-templates select="descendant::scene"/>
        
    </xsl:template>
    <xsl:template match="scene">
        <xsl:variable name="currentScene" as="element()" select="current()"/>
        <xsl:variable name="sceneNum" as="xs:string" 
            select="text()[1] ! normalize-space()"/>
        
        <xsl:for-each select="descendant::desc">
            
            <xsl:value-of select="current() ! normalize-space()"/>
            <xsl:value-of select="$tab"/>
            <xsl:value-of select="../@who"/>
            <xsl:value-of select="$tab"/>
            <xsl:value-of select="$sceneNum"/>
            <xsl:value-of select="$tab"/>
            <xsl:text>scene</xsl:text>
            <xsl:value-of select="$newline"/>
            
        </xsl:for-each>
    </xsl:template>
    
</xsl:stylesheet>