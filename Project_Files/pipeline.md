# Potential File Pipeline

    One way that this project may be able to utilize a pipeline structure is as follows:
    
1. Invisible XML for some baseline tagging (maybe a root element and wrapped scenes)
2. XSLT using regular expressions to continue markup
3. After markup, convert the full XML to a readable, formatted HTML (maybe including a CSS file) view
4. XSLT to pull out some of that specific marked up data (ex. dialogue frequencies, 4th wall breaks, scene length visuals, etc.) and convert to SVG that will then go back into the site
