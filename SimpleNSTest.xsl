<?xml version="1.0" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <h1>Found books</h1>
            <xsl:apply-templates/>
        </html>
    </xsl:template>


    <xsl:template match="body/catalog/author">
        <xsl:apply-templates select="name"/>
        <xsl:apply-templates select="book"/>
    </xsl:template>

    <xsl:template match="name">
        Author:
        <span style="color:#FF4500">
            <xsl:value-of select="."/>
        </span>
        <br/>
    </xsl:template>


    <xsl:template match="book">
        <ul>
            <li>
                Book title:
                <span style="color:#000080">
                    <xsl:value-of select="title"/>
                </span>
                | was soled -
                <span style="color:#000080">
                    <xsl:value-of select="purchased"/>
                </span>
                <br/>
            </li>
        </ul>
    </xsl:template>


    <xsl:template match="title">
        <ul>
            <li>
                <span style="color:#000080">
                    <xsl:value-of select="."/>
                </span>
                <br/>
            </li>
        </ul>
    </xsl:template>
</xsl:stylesheet>