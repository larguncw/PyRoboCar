
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
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Call me gordie</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Bad scooting</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Good scooting</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Knitting</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Sunrise yoga</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">YUI Roundtable</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Sporting moments</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Big red balloon</a></li>
        <li><a href="https://www.youtube.com/watch?v=kJzs-8Fz3pI&ab_channel=KrishnaOjha">Tango!</a></li>
    </ul>

    <script>
        $(document).ready(function(){
            $("ul.youtube-video-gallery").youtubeVideoGallery(  );
        });
    </script>
</body>
</html></textarea>




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
