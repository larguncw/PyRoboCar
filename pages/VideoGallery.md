<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset='utf-8' />
    <meta name="description" content="Youtube video gallery plugin for jquery >= 1.9" />
    <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="https://raw.github.com/clanceyp/youtube-video-gallery/master/jquery.youtubevideogallery.js"></script>
    <link rel="stylesheet" href="https://raw.github.com/clanceyp/youtube-video-gallery/master/youtube-video-gallery.css" type="text/css"/>
    <!--[if lt IE 9]>
    <link href="https://raw.github.com/clanceyp/youtube-video-gallery/master/youtube-video-gallery-legacy-ie.css" type="text/css" rel="stylesheet"/>
    <![endif]-->
    <title>Youtube video gallery for jquery</title>

    <style>
        body {
            font-family: sans-serif;
            font-size: 68%;
        }
        iframe {
            height: 400px;
            width: 100%;
        }
        pre,
        body.loaded textarea {
            display:none;
        }
        body.loaded pre {
            background-color: #BAFFBA;
            border: 0 none;
            border-left: 4px solid #2e8b57;
            display: inline-block;
            font-size: 1.1em;
            margin: 0 0 8px 0;
            padding: 8px 30px 8px 12px;
        }
        th {
            text-align: left;
        }
        tr.header th {
            background-color: #2e8b57;
            color: white;
            font-size: 1.2em;
            padding: 4px 20px 4px 8px;
        }
        td, th {
            padding: 4px 8px 4px 8px;
        }
        tr:nth-of-type(odd) {
            background-color: #BAFFBA;
        }
    </style>
</head>
<body>
<h1>Youtube gallery - a jQuery plugin</h1>
<p>
    Released under the
    <a href="http://www.opensource.org/licenses/mit-license.php">MIT License</a>.
    Source on <a href="https://github.com/clanceyp/youtube-video-gallery">Github</a>.<br>
    Compatible with: jQuery 1.9.1+
</p>
<h2>Overview</h2>
<p>Converts a list of Youtube links into a gallery. It displays the video player in a lightbox or just
    plain links if required. It can also use the
    <a href="http://www.jacklmoore.com/colorbox/">colorbox</a> or
    <a href="http://fancyapps.com/fancybox/">fancybox</a>
    plugin to display the video players nicely.
</p>
<h2>Features</h2>
<ul>
    <li>Supports Youtube links</li>
    <li>Lightweight: 4KB of JavaScript (less than 1KBs gzipped)</li>
    <li>Unobtrusive, requires no changes to existing HTML.</li>
    <li>CSS can be restyled</li>
    <li>Many configurable options</li>
</ul>
<h2>Demo</h2>
<iframe src="about/index-default.html" title="Default example"></iframe>
<iframe src="about/index-fancybox.html" title="Fancybox integration example"></iframe>
<iframe src="about/index-colorbox.html" title="Colorbox integration example"></iframe>
<iframe src="about/index-simple.html" title="Simple example"></iframe>
<h2>Usage</h2>
<p>intro</p>
<pre id="pre-example-01"></pre>
<textarea id="example-01"><!DOCTYPE html>
<html>
<head>
    <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="jquery.youtubevideogallery.js"></script>
    <link rel="stylesheet" href="youtube-video-gallery.css" type="text/css" rel="stylesheet">
    <link rel="stylesheet" href="test/test.css" type="text/css" rel="stylesheet">
    <!--[if IE lt 9]>
    <link href="youtube-video-gallery-legacy-ie.css" type="text/css" rel="stylesheet"/>
    <![endif]-->
    <title></title>
</head>
<body>
    <h1>Default display</h1>

    <ul class="youtube-video-gallery">
        <li><a href="http://www.youtube.com/watch?v=UCOC1YwNwZw">Call me gordie</a></li>
        <li><a href="http://www.youtube.com/watch?v=CjgT8Af1kGc">Bad scooting</a></li>
        <li><a href="http://www.youtube.com/watch?v=4psVnsYlBok">Good scooting</a></li>
        <li><a href="http://www.youtube.com/watch?v=05Cgtg_N4eI">Knitting</a></li>
        <li><a href="http://www.youtube.com/watch?v=xPr4g7o46DY">Sunrise yoga</a></li>
        <li><a href="http://www.youtube.com/watch?v=pocEg6a6ZpM">YUI Roundtable</a></li>
        <li><a href="http://www.youtube.com/watch?v=ishBOmjHoXE">Sporting moments</a></li>
        <li><a href="http://www.youtube.com/watch?v=j_OyHUqIIOU">Big red balloon</a></li>
        <li><a href="http://www.youtube.com/watch?v=_VZg1k1mpmw">Tango!</a></li>
    </ul>

    <script>
        $(document).ready(function(){
            $("ul.youtube-video-gallery").youtubeVideoGallery(  );
        });
    </script>
</body>
</html></textarea>

<h2>Settings</h2>
<table id="table">
    <tbody>

    <tr class="header">
        <th>Property</th>
        <th>Supported values</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
    <tr>
        <th scope="row">apiFallbackUrl</th>
        <td></td>
        <td></td>
        <td>Fallback URL, used in conjunction with apiUrl.</td>
    </tr>
    <tr>
        <th scope="row">apiUrl</th>
        <td></td>
        <td></td>
        <td>Generate youtube gallery form youtube API URL (must be json format, see <a href="https://developers.google.com/youtube/2.0/reference">API docs</a>)</td>
    </tr>
    <tr>
        <th scope="row">assetFolder</th>
        <td></td>
        <td></td>
        <td>The folder where the play button graphic is located</td>
    </tr>
    <tr>
        <th scope="row">fancybox</th>
        <td></td>
        <td></td>
        <td>If you are using the fancybox plugin, you can pass in the fancybox settings. See <a href="http://fancyapps.com/fancybox/">fancybox</a> for more info.</td>
    </tr>
    <tr>
        <th scope="row">forceLegacyIE</th>
        <td></td>
        <td>false</td>
        <td>By default the plugin will not try to use a lightbox for IE6 or IE7 due to lack of support in Youtube.</td>
    </tr>
    <tr>
        <th scope="row">iframeTemplate</th>
        <td></td>
        <td>&lt;iframe title="Youtube video player" id="youtube-videogallery-iframe" style="height:{options.innerHeight}px;width:{options.innerWidth}px;" frameborder="0" src="about:blank"&gt;&lt;/iframe&gt;</td>
        <td></td>
    </tr>
    <tr>
        <th scope="row">innerHeight</th>
        <td></td>
        <td>344</td>
        <td>Height of the video, if using a lightbox</td>
    </tr>
    <tr>
        <th scope="row">innerWidth</th>
        <td></td>
        <td>425</td>
        <td>Width of the video, if using a lightbox</td>
    </tr>
    <tr>
        <th scope="row">newWindow</th>
        <td></td>
        <td>(opens in a new window)</td>
        <td>Message to append to links if not using a lightbox</td>
    </tr>
    <tr>
        <th scope="row">playButton</th>
        <td></td>
        <td>play-button-red@40.png</td>
        <td>The name of the play button image which should be in the folder specified by the assetFolder propertie</td>
    </tr>
    <tr>
        <th scope="row">plugin</th>
        <td>colorbox<br/>fancybox<br/>self<br/>none</td>
        <td>self</td>
        <td>
            The default setting creates a basic lightbox. <br/>
            Use <a href="http://www.jacklmoore.com/colorbox/">colorbox</a> to create a nice, customisable lightbox.
            <br/>
            Set to 'none' to preserve the direct links to youtube.
        </td>
    </tr>
    <tr>
        <th scope="row">style</th>
        <td></td>
        <td>compact</td>
        <td>Different display options.</td>
    </tr>
    <tr>
        <th scope="row">title</th>
        <td>default<br/>full<br/>none</td>
        <td>default</td>
        <td>Determines how the titles are shown, set to 'none' to hide, 'full' display the full title. Default truncates title to one line line</td>
    </tr>
    <tr>
        <th scope="row">videos</th>
        <td></td>
        <td></td>
        <td>Array of objects containing id and title. Use if you want to create a gallery from JSON</td>
    </tr>
    <tr>
        <th scope="row">urlEmbed</th>
        <td></td>
        <td>http://www.youtube.com/embed/$id</td>
        <td>Link to youtube embed url</td>
    </tr>
    <tr>
        <th scope="row">urlImg</th>
        <td></td>
        <td>http://img.youtube.com/vi/$id/0.jpg</td>
        <td>Link used to create the gallery image. To use bespoke images
        put them on your server and use the video ID in the URL.</td>
    </tr>
    <tr>
        <th scope="row">urlLink</th>
        <td></td>
        <td>http://www.youtube.com/watch?v=$id</td>
        <td>Default youtube link url</td>
    </tr></tbody>
</table>





<script>
    $(document).ready(function(){
        $('textarea').each(function(i, el){
            $('#pre-'+ $(el).attr('id')).html(
               $(el).val().replace(/</g,'&lt;')
            )
        })
        $('body').addClass('loaded');
    })
</script>
</body>
</html>


<style type="text/css">
#submit {
 background-color: #008080;
 padding: .5em;
 -moz-border-radius: 5px;
 -webkit-border-radius: 5px;
 border-radius: 6px;
 color: #fff;
 align: center;
 font-size: 20px;
 text-decoration: none;
 border: none;
}
#submit:hover {
 border: none;
 background: orange;
 box-shadow: 0px 0px 1px #777;
}
</style>

<form>
<input id='submit' type="BUTTON" value="Picture Gallery" onclick="window.location.href='https://larguncw.github.io/PyRoboCar/pages/Gallery'">
</form>

<form>
<input id='submit' style="position: relative; left: 750px; bottom: 0px;" type="BUTTON" value="Homepage" onclick="window.location.href='https://larguncw.github.io/PyRoboCar/'">
</form>
