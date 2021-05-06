<html>
<head>

<?php
$arr_video_ids = array(
    'https://www.youtube.com/watch?v=Pzv_lUp3iOQ',
    'https://www.youtube.com/watch?v=zRtU8dpTEXg',
    'https://www.youtube.com/watch?v=EfSfLyeREMc',
    'https://www.youtube.com/watch?v=C-nypyy4pLg',
    'https://www.youtube.com/watch?v=OJpMT3odXtQ',
    'https://www.youtube.com/watch?v=WBnzOyBVwdg',
);
 
function getYouTubeThumbnailImage($video_id) {
    return "http://i3.ytimg.com/vi/$video_id/hqdefault.jpg";
}
 
function extractVideoID($url){
    $regExp = "/^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*/";
    preg_match($regExp, $url, $video);
    return $video[7];
}
?>

</head>
<body>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.css" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.min.css" />
<div class="container">
    <h3 class="text-center">My Video Gallery</h3>
    <div class="row">
        <?php foreach ($arr_video_ids as $video) { ?>
            <?php
            $video_id = extractVideoID($video);
            $video_thumbnail = getYouTubeThumbnailImage($video_id);
            ?>
            <div class="col-md-4">
                <div class="pb-2">
                    <a data-fancybox="video-gallery" href="<?php echo $video; ?>">
                        <img src="<?php echo $video_thumbnail; ?>" class="img-thumbnail" />
                    </a>
                </div>
            </div>
        <?php } ?>
    </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/js/bootstrap.min.js"></script>


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
