from flask import Flask

app = Flask(__name__)

rss_content = '''
<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
    <channel>
        <copyright>Copyright 1998 - 2024 DPG Media B.V.</copyright>
        <pubDate>Fri, 24 May 2024 17:22:00 GMT</pubDate>
        <lastBuildDate>Fri, 24 May 2024 17:22:00 GMT</lastBuildDate>
        <docs>https://tweakers.net/reviews/76</docs>
        <description>Tweakers is de grootste hardwaresite en techcommunity van Nederland.</description>
        <image>
            <link>https://tweakers.net/</link>
            <title>Tweakers</title>
            <url>https://tweakers.net/g/if/logo.gif</url>
            <description>Tweakers</description>
        </image>
        <language>nl-nl</language>
        <link>https://tweakers.net/</link>
        <title>Tweakers Mixed RSS Feed</title>
        <webMaster>gathering@tweakers.net</webMaster>
        <xhtml:meta content="noindex" name="robots" xmlns:xhtml="http://www.w3.org/1999/xhtml"/>
        <item>
            <title>'Nvidia keurt Samsung HBM's voorlopig af vanwege hitteproblemen'</title>
            <link>https://tweakers.net/nieuws/222326/nvidia-keurt-samsung-hbms-voorlopig-af-vanwege-hitteproblemen.html</link>
            <description>Nvidia heeft de nieuwste HBM-chips van Samsung voorlopig afgekeurd, schrijft Reuters op basis van interne bronnen. De fabrikant wil de chips gebruiken voor zijn AI-gpu's, maar er zouden problemen zijn met oververhitting en stroomverbruik.</description>
            <author>Loïs Franx</author>
            <category>Nieuws / Computers / Geheugen intern</category>
            <comments>https://tweakers.net/nieuws/222326/nvidia-keurt-samsung-hbms-voorlopig-af-vanwege-hitteproblemen.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222326</guid>
            <pubDate>Fri, 24 May 2024 16:15:00 GMT</pubDate>
        </item>
        <item>
            <title>NOS en NRC: bunq-klanten vaak het slachtoffer van phishing</title>
            <link>https://tweakers.net/nieuws/222324/nos-en-nrc-bunq-klanten-vaak-het-slachtoffer-van-phishing.html</link>
            <description>Oplichters hebben het vaker gemunt op klanten van bunq, doordat er bepaalde beveiligingsmaatregelen ontbreken die andere banken wel hebben. Dat blijkt uit onderzoek van de NOS en NRC. Ook worden de getroffen klanten niet gecompenseerd.</description>
            <author>Loïs Franx</author>
            <category>Nieuws / IT Pro / Economie en maatschappij</category>
            <comments>https://tweakers.net/nieuws/222324/nos-en-nrc-bunq-klanten-vaak-het-slachtoffer-van-phishing.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222324</guid>
            <pubDate>Fri, 24 May 2024 15:20:00 GMT</pubDate>
        </item>
        <item>
            <title>Netflix-abonnees bekeken 90 miljard uur aan films en series in tweede helft 2023</title>
            <link>https://tweakers.net/nieuws/222322/netflix-abonnees-bekeken-90-miljard-uur-aan-films-en-series-in-tweede-helft-2023.html</link>
            <description>Netflix heeft donderdag een overzicht met kijkcijfers gedeeld. Daaruit blijkt onder meer dat Netflix-abonnees gezamenlijk ruim 90 miljard uur hebben besteed aan het kijken naar films en series in de tweede helft van 2023. Over heel 2023 komt het neer op 183 miljard uur.</description>
            <author>Loïs Franx</author>
            <category>Nieuws / Beeld en geluid / Televisies</category>
            <comments>https://tweakers.net/nieuws/222322/netflix-abonnees-bekeken-90-miljard-uur-aan-films-en-series-in-tweede-helft-2023.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222322</guid>
            <pubDate>Fri, 24 May 2024 13:49:50 GMT</pubDate>
        </item>
        <item>
            <title>SwitchBot komt met universele smarthomeafstandsbediening met Matter-support</title>
            <link>https://tweakers.net/nieuws/222314/switchbot-komt-met-universele-smarthomeafstandsbediening-met-matter-support.html</link>
            <description>Domoticafabrikant SwitchBot komt dat later dit jaar met een universele afstandsbediening voor smarthomeapparaten en televisies. Die heeft een scherm met programmeerbare knoppen en Matter-ondersteuning. Ook brengt het bedrijf nieuwe camera's met hogere resoluties uit.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Beeld en geluid / Smarthome</category>
            <comments>https://tweakers.net/nieuws/222314/switchbot-komt-met-universele-smarthomeafstandsbediening-met-matter-support.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222314</guid>
            <pubDate>Fri, 24 May 2024 13:25:00 GMT</pubDate>
        </item>
        <item>
            <title>G.Skill brengt volgende week goud- en zilverkleurige Trident Z5 Royals uit</title>
            <link>https://tweakers.net/nieuws/222310/g-punt-skill-brengt-volgende-week-goud-en-zilverkleurige-trident-z5-royals-uit.html</link>
            <description>G.Skill begint volgende week met de verkoop van de Trident Z5 Royal-geheugenmodules. Het bedrijf teasede die vorig jaar al op de Computex. Het gaat om DDR5-8400-modules met zilver- en goudkleurige bedekking die uitkomen in kits van maximaal 96GB.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Computers / Geheugen intern</category>
            <comments>https://tweakers.net/nieuws/222310/g-punt-skill-brengt-volgende-week-goud-en-zilverkleurige-trident-z5-royals-uit.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222310</guid>
            <pubDate>Fri, 24 May 2024 13:00:27 GMT</pubDate>
        </item>
        <item>
            <title>Belgisch Kamerlid Liekens is 'maandenlang bespioneerd via haar apparaten'</title>
            <link>https://tweakers.net/nieuws/222318/belgisch-kamerlid-liekens-is-maandenlang-bespioneerd-via-haar-apparaten.html</link>
            <description>Open VLD-Kamerlid Goedele Liekens is naar eigen zeggen 'maandenlang bespioneerd'. De politicus schrijft in een bericht op socialemediaplatform X dat ze onder meer 'plots geen toegang meer had tot haar Dropbox'.</description>
            <author>Loïs Franx</author>
            <category>Nieuws / Computers / Beveiliging en antivirus</category>
            <comments>https://tweakers.net/nieuws/222318/belgisch-kamerlid-liekens-is-maandenlang-bespioneerd-via-haar-apparaten.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222318</guid>
            <pubDate>Fri, 24 May 2024 12:54:21 GMT</pubDate>
        </item>
        <item>
            <title>Hond achter dogememe en dogecoin overleden</title>
            <link>https://tweakers.net/geek/222312/hond-achter-dogememe-en-dogecoin-overleden.html</link>
            <description>Kabosu, de hond die wereldberoemd is geworden door de dogememe en de cryptocurrency dogecoin, is vrijdag overleden. De shiba inu leed al langere tijd aan leukemie. Haar baasje schat dat Kabosu 18 jaar oud is geworden.</description>
            <author>Loïs Franx</author>
            <category>.Geek / IT Pro / Websites en community's</category>
            <comments>https://tweakers.net/geek/222312/hond-achter-dogememe-en-dogecoin-overleden.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/geek/222312</guid>
            <pubDate>Fri, 24 May 2024 12:15:16 GMT</pubDate>
        </item>
        <item>
            <title>Foxit Reader 2024.2.2</title>
            <link>https://tweakers.net/downloads/68770/foxit-reader-202422.html</link>
            <description>Foxit Software heeft versie 2024.2.2 van Foxit PDF Reader uitgebracht, een alternatief voor Adobe Reader. Met dit gratis programma kunnen pdf-documenten bekeken, ingevuld en ondertekend worden. Voor het bewerken van pdf-documenten heeft Foxit Software het betaalde Foxit PDF Editor (voorheen PhantomPDF) in huis, vergelijkbaar met Acrobat Pro DC. Gebruik je de interne updatefunctie, vergeet dan niet het vinkje weg te halen voor het downloaden en installeren van PDF Editor. In deze uitgave zijn de volgende verbeteringen aangebracht: Issues Addressed</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68770/foxit-reader-202422.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68770</guid>
            <pubDate>Fri, 24 May 2024 12:09:02 GMT</pubDate>
        </item>
        <item>
            <title>Acer onthult nieuwe lijn Vero-laserprojectors vanaf 1600 euro</title>
            <link>https://tweakers.net/nieuws/222306/acer-onthult-nieuwe-lijn-vero-laserprojectors-vanaf-1600-euro.html</link>
            <description>Acer heeft woensdag een nieuwe lijn Vero-laserprojectors onthuld: de Acer Vero HL6810 en de Acer Vero HL6810ATV. Beide zijn 4k-uhd-projectors en hebben een helderheid van 4000 lumen.  De HL6810 krijgt een adviesprijs van 1600 euro en de HL6810ATV kost 1700 euro.</description>
            <author>Loïs Franx</author>
            <category>Nieuws / Beeld en geluid / Beamers</category>
            <comments>https://tweakers.net/nieuws/222306/acer-onthult-nieuwe-lijn-vero-laserprojectors-vanaf-1600-euro.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222306</guid>
            <pubDate>Fri, 24 May 2024 11:26:33 GMT</pubDate>
        </item>
        <item>
            <title>MSI toont moederbord voor desktops dat gebruikmaakt van compact CAMM2-geheugen</title>
            <link>https://tweakers.net/nieuws/222304/msi-toont-moederbord-voor-desktops-dat-gebruikmaakt-van-compact-camm2-geheugen.html</link>
            <description>MSI heeft een moederbord voor desktops getoond met plek voor CAMM2-geheugenmodules. Het is het eerste desktopmoederbord dat wordt uitgebracht waar ondersteuning op zit voor die nieuwe standaard, die een alternatief moet bieden voor vastgesoldeerd geheugen.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Computers / Moederborden</category>
            <comments>https://tweakers.net/nieuws/222304/msi-toont-moederbord-voor-desktops-dat-gebruikmaakt-van-compact-camm2-geheugen.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222304</guid>
            <pubDate>Fri, 24 May 2024 11:17:50 GMT</pubDate>
        </item>
        <item>
            <title>Atari neemt 'oude rivaal' Intellivision over</title>
            <link>https://tweakers.net/nieuws/222302/atari-neemt-oude-rivaal-intellivision-over.html</link>
            <description>Atari heeft consolemaker Intellivision gekocht. Daarmee krijgt de gamemaker de rechten van 200 games van dat bedrijf in handen. Intellivision blijft werken aan de Amico-console, die onder een Atari-licentie wordt uitgebracht.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Gaming / Consoles</category>
            <comments>https://tweakers.net/nieuws/222302/atari-neemt-oude-rivaal-intellivision-over.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222302</guid>
            <pubDate>Fri, 24 May 2024 09:57:12 GMT</pubDate>
        </item>
        <item>
            <title>Amazon gaat 15,7 miljard euro investeren in AWS-infrastructuur in Spanje</title>
            <link>https://tweakers.net/nieuws/222300/amazon-gaat-15-komma-7-miljard-euro-investeren-in-aws-infrastructuur-in-spanje.html</link>
            <description>Amazon gaat 15,7 miljard euro investeren in zijn AWS-infrastructuur in Spanje. Het bedrijf gaat daarmee de datacenters in de regio Aragón, die sinds eind 2022 operationeel zijn, flink uitbreiden. Een onbekend deel van het bedrag moet naar duurzaamheidscompensatie gaan.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / IT Pro / Internettoegang</category>
            <comments>https://tweakers.net/nieuws/222300/amazon-gaat-15-komma-7-miljard-euro-investeren-in-aws-infrastructuur-in-spanje.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222300</guid>
            <pubDate>Fri, 24 May 2024 09:23:34 GMT</pubDate>
        </item>
        <item>
            <title>Waterschap Drents Overijsselse Delta had portaal met bsn's op openbaar staan</title>
            <link>https://tweakers.net/nieuws/222296/waterschap-drents-overijsselse-delta-had-portaal-met-bsns-op-openbaar-staan.html</link>
            <description>Een online portaal van het waterschap Drents Overijsselse Delta met daarin onder andere burgerservicenummers van inwoners in het gebied was tijdelijke openbaar. Het waterschap heeft de portaal weer afgeschermd en zegt een melding bij de AP te hebben gemaakt.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / IT Pro / Privacy</category>
            <comments>https://tweakers.net/nieuws/222296/waterschap-drents-overijsselse-delta-had-portaal-met-bsns-op-openbaar-staan.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222296</guid>
            <pubDate>Fri, 24 May 2024 09:06:25 GMT</pubDate>
        </item>
        <item>
            <title>Apple: verwijderde foto's die weer opdoken werden niet gesynct via iCloud Photos</title>
            <link>https://tweakers.net/nieuws/222294/apple-verwijderde-fotos-die-weer-opdoken-werden-niet-gesynct-via-icloud-photos.html</link>
            <description>Apple heeft een mogelijke verklaring gegeven over waarom verwijderde foto's plotseling weer konden opduiken op apparaten. Het bedrijf zegt in een statement dat dit waarschijnlijk gebeurt als een corrupte database naar een nieuw apparaat wordt overgezet.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Computers / Beveiliging en antivirus</category>
            <comments>https://tweakers.net/nieuws/222294/apple-verwijderde-fotos-die-weer-opdoken-werden-niet-gesynct-via-icloud-photos.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222294</guid>
            <pubDate>Fri, 24 May 2024 08:43:16 GMT</pubDate>
        </item>
        <item>
            <title>Affinity Suite 2.5.0</title>
            <link>https://tweakers.net/downloads/68768/affinity-suite-250.html</link>
            <description>Serif heeft versie 2.5.0 van de Affinity Suite uitgebracht. De Affinity Suite bestaat uit de programma's Photo, Designer en Publisher, en kan worden beschouwd als de tegenhanger van bijvoorbeeld Photoshop, Illustrator en InDesign van Adobe. De software is beschikbaar voor Windows, macOS en iOS, en wordt regelmatig met korting aangeboden. Verder betreft het een eenmalige aanschaf, want Serif doet niet aan abonnementen. Of dat zo blijft nu Serif door Canva is overgenomen is nog niet helemaal duidelijk. De belangrijkste veranderingen die in versie 2.5.0 zijn aangebracht zijn hieronder voor je op een rijtje gezet: Announcing version 2.5.0 updates for the Affinity Suite on all platforms.</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68768/affinity-suite-250.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68768</guid>
            <pubDate>Fri, 24 May 2024 08:41:21 GMT</pubDate>
        </item>
        <item>
            <title>Universal USB Installer 2.0.2.3</title>
            <link>https://tweakers.net/downloads/68766/universal-usb-installer-2023.html</link>
            <description>Versie 2.0.2.3 van Universal USB Installer is uitgekomen. Met dit Windows-programma kunnen de installatie-iso's van een groot aantal Linux-distributies op een USB-stick geplaatst worden. Daardoor hoeven ze niet meer eerst op een cd of dvd gebrand te worden; de installatie kan vanaf de zelfstartende USB-stick worden uitgevoerd. Ondersteuning is aanwezig voor een groot aantal distributies, van de bekendste tot enkele zeer obscure. Ook kan een gedeelte van de USB-stick als persistent storage worden ingericht, waarin wijzigingen en persoonlijke bestanden opgeslagen kunnen worden, wat normaal gesproken niet mogelijk is bij een live-cd. De changelog voor deze uitgave kan hieronder worden gevonden: Changes in version 2.0.2.3:</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68766/universal-usb-installer-2023.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68766</guid>
            <pubDate>Fri, 24 May 2024 07:32:01 GMT</pubDate>
        </item>
        <item>
            <title>Gelekte specificaties van ROG Ally X tonen twee keer zo grote accu en meer ram</title>
            <link>https://tweakers.net/nieuws/222292/gelekte-specificaties-van-rog-ally-x-tonen-twee-keer-zo-grote-accu-en-meer-ram.html</link>
            <description>De accu van de nieuwe ROG Ally X wordt naar verluidt twee keer zo groot als die van het eerste model. De nieuwe handheld zou een 80Wh-accu krijgen, een verdubbeling van de 40Wh-capaciteit die het eerste model had.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Gaming / Consoles</category>
            <comments>https://tweakers.net/nieuws/222292/gelekte-specificaties-van-rog-ally-x-tonen-twee-keer-zo-grote-accu-en-meer-ram.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222292</guid>
            <pubDate>Fri, 24 May 2024 07:29:36 GMT</pubDate>
        </item>
        <item>
            <title>Microsoft brengt Windows 11 IoT Enterprise LTSC 2024 uit</title>
            <link>https://tweakers.net/nieuws/222288/microsoft-brengt-windows-11-iot-enterprise-ltsc-2024-uit.html</link>
            <description>Microsoft heeft een nieuwe lts-release van Windows 11 IoT Enterprise uitgebracht die op meer apparaten kan worden geïnstalleerd. Het aantal packages dat kan worden verwijderd, neemt toe, waardoor het systeem aantrekkelijker wordt voor kleine apparaten.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Computers / Besturingssystemen</category>
            <comments>https://tweakers.net/nieuws/222288/microsoft-brengt-windows-11-iot-enterprise-ltsc-2024-uit.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222288</guid>
            <pubDate>Fri, 24 May 2024 06:43:01 GMT</pubDate>
        </item>
        <item>
            <title>Meta gaat AI vanaf eind juni ook op data van Europeanen trainen</title>
            <link>https://tweakers.net/nieuws/222240/meta-gaat-ai-vanaf-eind-juni-ook-op-data-van-europeanen-trainen.html</link>
            <description>Meta lijkt zijn AI-systemen ook op data van Europese gebruikers te gaan trainen. Dat gebeurt vanaf eind juni, blijkt uit mails die verschillende gebruikers hebben ontvangen. Meta zegt daarvoor een 'gerechtvaardigd belang' te hebben.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / IT Pro / Privacy</category>
            <comments>https://tweakers.net/nieuws/222240/meta-gaat-ai-vanaf-eind-juni-ook-op-data-van-europeanen-trainen.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222240</guid>
            <pubDate>Fri, 24 May 2024 05:58:47 GMT</pubDate>
        </item>
        <item>
            <title>Calibre 7.11</title>
            <link>https://tweakers.net/downloads/68764/calibre-711.html</link>
            <description>Versie 7.11 van Calibre is uitgekomen. Dit opensource-e-bookbeheerprogramma is haast onmisbaar voor elke e-readerbezitter. Het is beschikbaar voor Windows, Linux en macOS en kan onder meer alle relevante informatie en omslagafbeeldingen opzoeken, e-boeken bewerken en converteren om ze zo geschikt te maken voor de diverse soorten e-readers. Verder kan het programma kranten, tijdschriften en nieuwsartikelen op basis van rss-feeds omzetten in e-bookformaat en kunnen met Calibre boeken worden aangeschaft bij de bekende webwinkels. In versie 7.0 is de mogelijkheid om notities toe te voegen aan bijvoorbeeld auteurs en series, en is ondersteuning voor EPUB-audioboeken toegevoegd. Ook kunnen er extra bestanden aan boeken worden toegevoegd, zoals bijvoorbeeld alternatieve omslagafbeelding en heeft Calibre nu een eigen prullenbak, die gebruikt kan worden in plaats van die in het besturingssysteem. In deze update zijn verder nog de volgende veranderingen en verbeteringen aangebracht: New features</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68764/calibre-711.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68764</guid>
            <pubDate>Fri, 24 May 2024 05:28:54 GMT</pubDate>
        </item>
        <item>
            <title>Kabinet wil centraal loket om bedrijven voor cyberdreiging te waarschuwen</title>
            <link>https://tweakers.net/nieuws/222252/kabinet-wil-centraal-loket-om-bedrijven-voor-cyberdreiging-te-waarschuwen.html</link>
            <description>De Nederlandse overheid wil meer bedrijven kunnen waarschuwen voor digitale dreigingen. Daarom wordt het huidige netwerk van waarschuwingsorganisaties uitgebreid en opnieuw georganiseerd. Het nieuwe Cyberweerbaarheidsnetwerk komt onder leiding van de NCTV te staan.</description>
            <author>Tijs Hofmans</author>
            <category>Nieuws / Computers / Beveiliging en antivirus</category>
            <comments>https://tweakers.net/nieuws/222252/kabinet-wil-centraal-loket-om-bedrijven-voor-cyberdreiging-te-waarschuwen.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222252</guid>
            <pubDate>Fri, 24 May 2024 05:25:12 GMT</pubDate>
        </item>
        <item>
            <title>Apple iPad Pro (2024) en iPad Air (2024) - Ultralicht of zwaargewicht</title>
            <link>https://tweakers.net/reviews/12098/apple-ipad-pro-2024-en-ipad-air-2024-ultralicht-of-zwaargewicht.html</link>
            <description>Apple brengt twee nieuwe iPads uit. De iPad Pro is dunner dan ooit en heeft een dubbellaagsoledscherm, de iPad Air verschijnt voor het eerst in twee formaten.</description>
            <author>Friso Weijers</author>
            <category>Review / Tablets en telefoons / Tablets</category>
            <comments>https://tweakers.net/reviews/12098/6/apple-ipad-pro-2024-en-ipad-air-2024-ultralicht-of-zwaargewicht-conclusie.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/reviews/12098</guid>
            <pubDate>Fri, 24 May 2024 04:00:00 GMT</pubDate>
        </item>
        <item>
            <title>AdGuard Home 0.107.50</title>
            <link>https://tweakers.net/downloads/68758/adguard-home-010750.html</link>
            <description>AdGuard Home versie 0.107.50 is uitgekomen. Met deze software kan er thuis een dns-server worden opgezet om zo onder meer advertenties en malware te blokkeren op het hele netwerk, waardoor dat niet langer op elk individueel apparaat nodig is. Het is daarmee dus vergelijkbaar met Pi-hole. AdGuard Home werkt op een machine met Windows, macOS, Linux of FreeBSD, is ook in staat om tegen phishing te beschermen en heeft parental control. Op ons eigen forum kan over het programma worden gediscussieerd. Deze uitgave moet het probleem verhelpen dat de vorige uitgave voor een aantal mensen de boel helemaal stuk maakte. AdGuard Home v0.107.50</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68758/adguard-home-010750.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68758</guid>
            <pubDate>Thu, 23 May 2024 20:40:05 GMT</pubDate>
        </item>
        <item>
            <title>The Bat! 11.2</title>
            <link>https://tweakers.net/downloads/68762/the-bat-112.html</link>
            <description>Versie 11.1 van de ruim twintig jaar oude e-mailclient The Bat! is uitgekomen. Het programma heeft alles wat je van een moderne e-mailclient mag verwachten, zoals het automatisch kunnen sorteren, beantwoorden of doorsturen van e-mail en het met vertraging kunnen versturen van e-mails. Er zijn diverse e-mailthema's, waarbij ook van macro's gebruikgemaakt kan worden. In deze uitgave is onder meer de optie toegevoegd om te kiezen met welke applicatie een bijlage moet worden geopend. De complete changelog ziet er als volgt uit: New features</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68762/the-bat-112.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68762</guid>
            <pubDate>Thu, 23 May 2024 20:34:16 GMT</pubDate>
        </item>
        <item>
            <title>AddComm getroffen door ransomware, leverde aanslagen van waterschapsbelasting</title>
            <link>https://tweakers.net/nieuws/222286/addcomm-getroffen-door-ransomware-leverde-aanslagen-van-waterschapsbelasting.html</link>
            <description>Het Nederlandse klantencommunicatiebedrijf AddComm is getroffen door een ransomwareaanval. Een van de klanten van dit bedrijf is het waterschap Hoogheemraadschap Hollands Noorderkwartier, dat mogelijk indirect door de cyberaanval getroffen is.</description>
            <author>Yannick Spinner</author>
            <category>Nieuws / Computers / Beveiliging en antivirus</category>
            <comments>https://tweakers.net/nieuws/222286/addcomm-getroffen-door-ransomware-leverde-aanslagen-van-waterschapsbelasting.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222286</guid>
            <pubDate>Thu, 23 May 2024 19:06:50 GMT</pubDate>
        </item>
        <item>
            <title>Spotify Car Thing is vanaf 9 december niet meer te gebruiken</title>
            <link>https://tweakers.net/nieuws/222284/spotify-car-thing-is-vanaf-9-december-niet-meer-te-gebruiken.html</link>
            <description>Spotify meldt dat de Car Thing-gadget vanaf 9 december niet meer te gebruiken is. Het bedrijf stopte in 2022 al met de productie van het apparaatje en bracht het nooit officieel in de Benelux uit.</description>
            <author>Yannick Spinner</author>
            <category>Nieuws / Beeld en geluid / Gadgets</category>
            <comments>https://tweakers.net/nieuws/222284/spotify-car-thing-is-vanaf-9-december-niet-meer-te-gebruiken.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222284</guid>
            <pubDate>Thu, 23 May 2024 18:35:50 GMT</pubDate>
        </item>
        <item>
            <title>Delta Energie gaat terugleverkosten bij zonnepaneeleigenaren in rekening brengen</title>
            <link>https://tweakers.net/nieuws/222280/delta-energie-gaat-terugleverkosten-bij-zonnepaneeleigenaren-in-rekening-brengen.html</link>
            <description>Delta Energie gaat terugleverkosten in rekening brengen bij klanten met zonnepanelen. Bij een teruglevering van tenminste 100kWh stroom op jaarbasis wordt een vast bedrag gerekend. De energieleverancier verlaagt de reguliere stroomprijs met vier eurocent.</description>
            <author>Yannick Spinner</author>
            <category>Nieuws / IT Pro / Economie en maatschappij</category>
            <comments>https://tweakers.net/nieuws/222280/delta-energie-gaat-terugleverkosten-bij-zonnepaneeleigenaren-in-rekening-brengen.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222280</guid>
            <pubDate>Thu, 23 May 2024 17:27:08 GMT</pubDate>
        </item>
        <item>
            <title>iFixit en Samsung stoppen samenwerking voor reserveonderdelen</title>
            <link>https://tweakers.net/nieuws/222278/ifixit-en-samsung-stoppen-samenwerking-voor-reserveonderdelen.html</link>
            <description>iFixit en Samsung werken binnenkort niet meer samen met de verkoop van officiële reserveonderdelen en de ontwikkeling van reparatiehandleidingen voor Samsung-smartphones. Volgens iFixit lijkt Samsung 'niet geïnteresseerd' te zijn in een verdere samenwerking.</description>
            <author>Yannick Spinner</author>
            <category>Nieuws / Tablets en telefoons / Smartphones</category>
            <comments>https://tweakers.net/nieuws/222278/ifixit-en-samsung-stoppen-samenwerking-voor-reserveonderdelen.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222278</guid>
            <pubDate>Thu, 23 May 2024 16:04:52 GMT</pubDate>
        </item>
        <item>
            <title>Gemeente Eindhoven getroffen door datalek, bsn burgers kort intern inzichtelijk</title>
            <link>https://tweakers.net/nieuws/222276/gemeente-eindhoven-getroffen-door-datalek-bsn-burgers-kort-intern-inzichtelijk.html</link>
            <description>De gemeente Eindhoven meldt een datalek waarbij de burgerservicenummers van bijna alle burgers van de gemeente 'enkele uren' inzichtelijk waren. Het gaat om een intern datalek waarbij de gegevens dus alleen voor ambtenaren in te zien waren.</description>
            <author>Yannick Spinner</author>
            <category>Nieuws / IT Pro / Economie en maatschappij</category>
            <comments>https://tweakers.net/nieuws/222276/gemeente-eindhoven-getroffen-door-datalek-bsn-burgers-kort-intern-inzichtelijk.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222276</guid>
            <pubDate>Thu, 23 May 2024 15:33:07 GMT</pubDate>
        </item>
        <item>
            <title>Xiaomi kondigt POCO F6 en F6 Pro aan</title>
            <link>https://tweakers.net/nieuws/222274/xiaomi-kondigt-poco-f6-en-f6-pro-aan.html</link>
            <description>Xiaomi heeft de POCO F6 en F6 Pro aangekondigd. De F6 komt per direct uit voor 450 euro, de Pro-versie heeft prijzen vanaf 580 euro. De telefoons volgen de F5 en F5 Pro van vorig jaar op.</description>
            <author>Arnoud Wokke</author>
            <category>Nieuws / Tablets en telefoons / Smartphones</category>
            <comments>https://tweakers.net/nieuws/222274/xiaomi-kondigt-poco-f6-en-f6-pro-aan.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222274</guid>
            <pubDate>Thu, 23 May 2024 15:07:12 GMT</pubDate>
        </item>
        <item>
            <title>Activision kondigt Call of Duty: Black Ops 6 aan</title>
            <link>https://tweakers.net/nieuws/222272/activision-kondigt-call-of-duty-black-ops-6-aan.html</link>
            <description>Activision Blizzard kondigt Call of Duty: Black Ops 6 aan. Naast een teaser op X en een teaserwebsite zijn er weinig details over de komende game bekend.</description>
            <author>Yannick Spinner</author>
            <category>Nieuws / Gaming / Games</category>
            <comments>https://tweakers.net/nieuws/222272/activision-kondigt-call-of-duty-black-ops-6-aan.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222272</guid>
            <pubDate>Thu, 23 May 2024 14:40:44 GMT</pubDate>
        </item>
        <item>
            <title>Nederlandse Tweede Kamer vindt dat terugleveren stroom geen geld mag kosten</title>
            <link>https://tweakers.net/nieuws/222270/nederlandse-tweede-kamer-vindt-dat-terugleveren-stroom-geen-geld-mag-kosten.html</link>
            <description>De Nederlandse Tweede Kamer wil dat het terugleveren van stroom door particulieren op een moment dat er veel aanbod is, geen geld kost. Energieleveranciers mogen wel een terugleververgoeding blijven vragen.</description>
            <author>Arnoud Wokke</author>
            <category>Nieuws / IT Pro / Politiek en recht</category>
            <comments>https://tweakers.net/nieuws/222270/nederlandse-tweede-kamer-vindt-dat-terugleveren-stroom-geen-geld-mag-kosten.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222270</guid>
            <pubDate>Thu, 23 May 2024 14:10:08 GMT</pubDate>
        </item>
        <item>
            <title>Win kaarten: meet-and-greet met Federico Faggin in het HomeComputerMuseum</title>
            <link>https://tweakers.net/reviews/12118/win-kaarten-meet-and-greet-met-federico-faggin-in-het-homecomputermuseum.html</link>
            <description>Op 8 juni krijgt het HomeComputerMuseum hoog bezoek van niemand minder dan Federico Faggin. In samenwerking met eigenaar WHiZZi geven wij vier kaarten weg.</description>
            <author>Saskia Schoonebeek</author>
            <category>.Community / IT Pro / Websites en community's</category>
            <comments>https://tweakers.net/reviews/12118/win-kaarten-meet-and-greet-met-federico-faggin-in-het-homecomputermuseum.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/reviews/12118</guid>
            <pubDate>Thu, 23 May 2024 13:15:00 GMT</pubDate>
        </item>
        <item>
            <title>Previewversie AMD Anti-Lag 2 is nu beschikbaar in Counter-Strike 2</title>
            <link>https://tweakers.net/nieuws/222262/previewversie-amd-anti-lag-2-is-nu-beschikbaar-in-counter-strike-2.html</link>
            <description>AMD heeft een testversie van Radeon Anti-Lag 2 uitgebracht. De latentieverlagende technologie moet, in tegenstelling tot zijn voorgangers, per game geïmplementeerd worden. Counter-Strike 2 is het eerste spel dat de feature ondersteunt.</description>
            <author>Idriz Velghe</author>
            <category>Nieuws / Computers / Videokaarten</category>
            <comments>https://tweakers.net/nieuws/222262/previewversie-amd-anti-lag-2-is-nu-beschikbaar-in-counter-strike-2.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222262</guid>
            <pubDate>Thu, 23 May 2024 13:13:00 GMT</pubDate>
        </item>
        <item>
            <title>CCleaner 6.24</title>
            <link>https://tweakers.net/downloads/68754/ccleaner-624.html</link>
            <description>Piriform heeft versie 6.24 van CCleaner uitgebracht. Met dit programma kunnen diverse onderdelen van Windows worden opgeschoond. Hierbij valt te denken aan tijdelijke Windows- en internetbestanden, maar ook aan overbodige rommel van een groot aantal andere programma's, waaronder Windows Media Player, Google Toolbar, Microsoft Office, Photoshop, WinRAR en ga zo maar door. Bovendien is het aantal programma's waarvan CCleaner de rommel kan opruimen, eenvoudig uit te breiden met het programma CCEnhancer. Naast opruimen kan CCleaner ook fouten in het register en in snelkoppelingen verhelpen, en de lijst met programma's die starten met Windows aanpassen, en is het mogelijk om cookies te beheren. Vanaf deze versie kan ook de algehele conditie van de computer worden getest. Naast een gratis uitvoering is er ook een pro-versie, die onder meer een automatische-updatefunctie biedt. In deze release zijn de volgende veranderingen en verbeteringen aangebracht: Taking the hassle out of PC maintenance</description>
            <author>Bart van Klaveren</author>
            <category>Software-update / Software</category>
            <comments>https://tweakers.net/downloads/68754/ccleaner-624.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/downloads/68754</guid>
            <pubDate>Thu, 23 May 2024 13:12:53 GMT</pubDate>
        </item>
        <item>
            <title>Gerucht: Xiaomi werkt aan nieuwe soc voor smartphones onder codenaam Ring</title>
            <link>https://tweakers.net/nieuws/222268/gerucht-xiaomi-werkt-aan-nieuwe-soc-voor-smartphones-onder-codenaam-ring.html</link>
            <description>Xiaomi zou werken aan een nieuwe soc voor smartphones onder de codenaam Ring. De prestaties zouden volgens geruchten in de buurt moeten liggen van de Snapdragon 8 Gen 2 van vorig jaar. Xiaomi maakte al eens een mobiele soc.</description>
            <author>Arnoud Wokke</author>
            <category>Nieuws / Computers / Processors</category>
            <comments>https://tweakers.net/nieuws/222268/gerucht-xiaomi-werkt-aan-nieuwe-soc-voor-smartphones-onder-codenaam-ring.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222268</guid>
            <pubDate>Thu, 23 May 2024 12:23:52 GMT</pubDate>
        </item>
        <item>
            <title>Meta Ray-Ban-bril krijgt functie om foto's rechtstreeks op Instagram te zetten</title>
            <link>https://tweakers.net/nieuws/222266/meta-ray-ban-bril-krijgt-functie-om-fotos-rechtstreeks-op-instagram-te-zetten.html</link>
            <description>De bril van Meta en Ray-Ban krijgt de functie om foto's rechtstreeks te plaatsen als Instagram-story, zonder dat gebruikers hun telefoon hoeven te pakken. Dat kon tot nu toe niet.</description>
            <author>Arnoud Wokke</author>
            <category>Nieuws / Gaming / VR-brillen</category>
            <comments>https://tweakers.net/nieuws/222266/meta-ray-ban-bril-krijgt-functie-om-fotos-rechtstreeks-op-instagram-te-zetten.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222266</guid>
            <pubDate>Thu, 23 May 2024 12:09:34 GMT</pubDate>
        </item>
        <item>
            <title>Antec en Ayaneo brengen handheld uit met Ryzen 7 7840U en uitschuifbaar scherm</title>
            <link>https://tweakers.net/nieuws/222256/antec-en-ayaneo-brengen-handheld-uit-met-ryzen-7-7840u-en-uitschuifbaar-scherm.html</link>
            <description>Antec heeft met de Core HS zijn eerste gaminghandheld onthuld. Het gaat om een omgedoopte versie van de Ayaneo Slide. Beide consoles combineren een AMD Ryzen 7 7840U-processor met een uitschuifbaar scherm dat een toetsenbord bedekt.</description>
            <author>Idriz Velghe</author>
            <category>Nieuws / Gaming / Consoles</category>
            <comments>https://tweakers.net/nieuws/222256/antec-en-ayaneo-brengen-handheld-uit-met-ryzen-7-7840u-en-uitschuifbaar-scherm.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222256</guid>
            <pubDate>Thu, 23 May 2024 12:06:17 GMT</pubDate>
        </item>
        <item>
            <title>OpenAI sluit deal met News Corp voor gebruik artikelen WSJ in ChatGPT</title>
            <link>https://tweakers.net/nieuws/222264/openai-sluit-deal-met-news-corp-voor-gebruik-artikelen-wsj-in-chatgpt.html</link>
            <description>OpenAI heeft een deal gesloten met News Corp voor het gebruik van content en expertise van haar media in diensten zoals ChatGPT. Daardoor heeft OpenAI nu toestemming om antwoorden te genereren op basis van artikelen van onder meer The Wall Street Journal.</description>
            <author>Arnoud Wokke</author>
            <category>Nieuws / IT Pro / Bedrijfsnieuws</category>
            <comments>https://tweakers.net/nieuws/222264/openai-sluit-deal-met-news-corp-voor-gebruik-artikelen-wsj-in-chatgpt.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222264</guid>
            <pubDate>Thu, 23 May 2024 11:56:19 GMT</pubDate>
        </item>
        <item>
            <title>GlobalFoundries verliest derde plek op chipmakersmarkt aan Chinese concurrent</title>
            <link>https://tweakers.net/nieuws/222260/globalfoundries-verliest-derde-plek-op-chipmakersmarkt-aan-chinese-concurrent.html</link>
            <description>AMD-spin-off GlobalFoundries is volgens analistenbureau Counterpoint Research zijn derde plek op de markt voor chipfabricage kwijt aan het Chinese SMIC. Het marktaandeel van GlobalFoundries slonk. TSMC blijft met afstand marktleider.</description>
            <author>Arnoud Wokke</author>
            <category>Nieuws / Computers / Processors</category>
            <comments>https://tweakers.net/nieuws/222260/globalfoundries-verliest-derde-plek-op-chipmakersmarkt-aan-chinese-concurrent.html#reacties</comments>
            <guid isPermaLink="false">https://tweakers.net/nieuws/222260</guid>
            <pubDate>Thu, 23 May 2024 11:48:19 GMT</pubDate>
        </item>
    </channel>
</rss>
'''
#
# '''
# <?xml version="1.0" encoding="utf-8"?>
# <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/"
# xmlns:media="http://search.yahoo.com/mrss/"><channel><title>NU - Algemeen</title>
# <link>https://www.nu.nl/algemeen</link><description>Het laatste nieuws het eerst op NU.nl</description>
# <atom:link href="https://www.nu.nl/rss/Algemeen" rel="self"/><language>nl-nl</language><copyright>Copyright © 2024, NU</copyright>
# <lastBuildDate>Fri, 24 May 2024 18:29:08 +0200</lastBuildDate><ttl>60</ttl>
# <atom:logo>https://www.nu.nl/assets/favicon/nu_logo.svg</atom:logo>
# <item><title>Neerslag zorgde voor vroege en drukke avondspits, files nemen nu weer af</title><link>https://www.nu.nl/binnenland/6314191/neerslag-zorgde-voor-vroege-en-drukke-avondspits-files-nemen-nu-weer-af.html</link><description>Het was vrijdag vanwege het slechte weer al vroeg druk op de Nederlandse wegen. Op het hoogtepunt stond ruim 800 kilometer file. Het aantal files neemt inmiddels weer af.</description><pubDate>Fri, 24 May 2024 18:29:08 +0200</pubDate><guid isPermaLink="false">article-6314191</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/kswxrrha9zaw_sqr256/2365/7/4473/4473/neerslag-zorgde-voor-vroege-en-drukke-avondspits-files-nemen-nu-weer-af.jpg"/><category>binnenland</category><dc:rights>copyright photo: ANP</dc:rights></item>
# <item><title>Super Size Me-regisseur Morgan Spurlock (53) overleden aan kanker</title><link>https://www.nu.nl/film/6314189/super-size-me-regisseur-morgan-spurlock-53-overleden-aan-kanker.html</link><description>De Amerikaanse documentairemaker Morgan Spurlock is op 53-jarige leeftijd overleden aan kanker. Hij brak in 2004 wereldwijd door met zijn film &lt;em&gt;Super Size Me&lt;/em&gt;, waarin hij een maand lang elke dag drie maaltijden van McDonald's at.</description><pubDate>Fri, 24 May 2024 18:07:49 +0200</pubDate><guid isPermaLink="false">article-6314189</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/in8x1z4axihc_sqr256/171/0/685/685/super-size-me-regisseur-morgan-spurlock-53-overleden-aan-kanker.jpg"/><category>film</category><dc:rights>copyright photo: Getty Images</dc:rights>
# </item><item><title>Verstappen wacht nog even met Le Mans: 'Wel benaderd door teams'</title><link>https://www.nu.nl/formule-1/6314107/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.html</link><description>Vroeg of laat verschijnt Max Verstappen aan de start van de 24 uur van Le Mans. Hij is al benaderd door teams, maar houdt de boot nog even af. Deelname tijdens zijn Formule 1-loopbaan sluit de 26-jarige Verstappen niet uit.</description><pubDate>Fri, 24 May 2024 11:18:53 +0200</pubDate><guid isPermaLink="false">article-6314107</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/ks5xb3cao78c_sqr256/120/0/3912/3912/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.jpg"/><category>formule-1</category><dc:rights>copyright photo: Getty</dc:rights>
# </item></channel></rss>
# '''


rss_updated_content = '''
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" 
xmlns:media="http://search.yahoo.com/mrss/"><channel><title>NU - Algemeen</title>
<link>https://www.nu.nl/algemeen</link><description>Het laatste nieuws het eerst op NU.nl</description>
<atom:link href="https://www.nu.nl/rss/Algemeen" rel="self"/><language>nl-nl</language><copyright>Copyright © 2024, NU</copyright>
<lastBuildDate>Fri, 24 May 2024 18:29:08 +0200</lastBuildDate><ttl>60</ttl>
<atom:logo>https://www.nu.nl/assets/favicon/nu_logo.svg</atom:logo>
<item><title>New item was added to the feed</title><link>https://www.nu.nl/binnenland/6314191/neerslag-zorgde-voor-vroege-en-drukke-avondspits-files-nemen-nu-weer-af.html</link><description>Het was vrijdag vanwege het slechte weer al vroeg druk op de Nederlandse wegen. Op het hoogtepunt stond ruim 800 kilometer file. Het aantal files neemt inmiddels weer af.</description><pubDate>Fri, 24 May 2024 18:29:08 +0200</pubDate><guid isPermaLink="false">article-6314191</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/kswxrrha9zaw_sqr256/2365/7/4473/4473/neerslag-zorgde-voor-vroege-en-drukke-avondspits-files-nemen-nu-weer-af.jpg"/><category>binnenland</category><dc:rights>copyright photo: ANP</dc:rights></item>
<item><title>Neerslag zorgde voor vroege en drukke avondspits, files nemen nu weer af</title><link>https://www.nu.nl/binnenland/6314191/neerslag-zorgde-voor-vroege-en-drukke-avondspits-files-nemen-nu-weer-af.html</link><description>Het was vrijdag vanwege het slechte weer al vroeg druk op de Nederlandse wegen. Op het hoogtepunt stond ruim 800 kilometer file. Het aantal files neemt inmiddels weer af.</description><pubDate>Fri, 24 May 2024 18:29:08 +0200</pubDate><guid isPermaLink="false">article-6314191</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/kswxrrha9zaw_sqr256/2365/7/4473/4473/neerslag-zorgde-voor-vroege-en-drukke-avondspits-files-nemen-nu-weer-af.jpg"/><category>binnenland</category><dc:rights>copyright photo: ANP</dc:rights></item>
<item><title>Super Size Me-regisseur Morgan Spurlock (53) overleden aan kanker</title><link>https://www.nu.nl/film/6314189/super-size-me-regisseur-morgan-spurlock-53-overleden-aan-kanker.html</link><description>De Amerikaanse documentairemaker Morgan Spurlock is op 53-jarige leeftijd overleden aan kanker. Hij brak in 2004 wereldwijd door met zijn film &lt;em&gt;Super Size Me&lt;/em&gt;, waarin hij een maand lang elke dag drie maaltijden van McDonald's at.</description><pubDate>Fri, 24 May 2024 18:07:49 +0200</pubDate><guid isPermaLink="false">article-6314189</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/in8x1z4axihc_sqr256/171/0/685/685/super-size-me-regisseur-morgan-spurlock-53-overleden-aan-kanker.jpg"/><category>film</category><dc:rights>copyright photo: Getty Images</dc:rights></item>
<item><title>Verstappen wacht nog even met Le Mans: 'Wel benaderd door teams'</title><link>https://www.nu.nl/formule-1/6314107/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.html</link><description>Vroeg of laat verschijnt Max Verstappen aan de start van de 24 uur van Le Mans. Hij is al benaderd door teams, maar houdt de boot nog even af. Deelname tijdens zijn Formule 1-loopbaan sluit de 26-jarige Verstappen niet uit.</description><pubDate>Fri, 24 May 2024 11:18:53 +0200</pubDate><guid isPermaLink="false">article-6314107</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/ks5xb3cao78c_sqr256/120/0/3912/3912/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.jpg"/><category>formule-1</category><dc:rights>copyright photo: Getty</dc:rights></item>
<item><title>Verstappen wacht nog even met Le Mans: 'Wel benaderd door teams'</title><link>https://www.nu.nl/formule-1/6314107/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.html</link><description>Vroeg of laat verschijnt Max Verstappen aan de start van de 24 uur van Le Mans. Hij is al benaderd door teams, maar houdt de boot nog even af. Deelname tijdens zijn Formule 1-loopbaan sluit de 26-jarige Verstappen niet uit.</description><pubDate>Fri, 24 May 2024 11:18:53 +0200</pubDate><guid isPermaLink="false">article-6314107</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/ks5xb3cao78c_sqr256/120/0/3912/3912/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.jpg"/><category>formule-1</category><dc:rights>copyright photo: Getty</dc:rights></item>
<item><title>Verstappen wacht nog even met Le Mans: 'Wel benaderd door teams'</title><link>https://www.nu.nl/formule-1/6314107/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.html</link><description>Vroeg of laat verschijnt Max Verstappen aan de start van de 24 uur van Le Mans. Hij is al benaderd door teams, maar houdt de boot nog even af. Deelname tijdens zijn Formule 1-loopbaan sluit de 26-jarige Verstappen niet uit.</description><pubDate>Fri, 24 May 2024 11:18:53 +0200</pubDate><guid isPermaLink="false">article-6314107</guid><enclosure length="0" type="image/jpeg" url="https://images.nu.nl/m/ks5xb3cao78c_sqr256/120/0/3912/3912/verstappen-wacht-nog-even-met-le-mans-wel-benaderd-door-teams.jpg"/><category>formule-1</category><dc:rights>copyright photo: Getty</dc:rights></item>
</channel></rss>
'''


@app.route("/rss-feed", methods=["GET"])
def get_rss_feed():
    return rss_content, 200, {"Content-Type": "text/xml; charset=utf-8"}


@app.route("/update-feed", methods=["GET"])
def add_item():
    global rss_content
    rss = rss_updated_content
    return rss, 200, {"Content-Type": "text/mrss; charset=utf-8"}


@app.route("/ping")
def ping():
    return "PONG", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")

