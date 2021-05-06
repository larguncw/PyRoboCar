<article class="video">
  <figure>
    <a class="fancybox fancybox.iframe" href="http://www.youtube.com/embed/paG__3FBLzI">
    <img class="videoThumb" src="http://i1.ytimg.com/vi/paG__3FBLzI/mqdefault.jpg"></a>
  </figure>
  <h2 class="videoTitle">Mesopotamia</h2>
</article>

<article class="video">
  <figure>
    <a class="fancybox fancybox.iframe" href="http://www.youtube.com/embed/paG__3FBLzI">
    <img class="videoThumb" src="http://i1.ytimg.com/vi/paG__3FBLzI/mqdefault.jpg"></a>
  </figure>
  <h2 class="videoTitle">Mesopotamia</h2>
</article>

<article class="video">
  <figure>
    <a class="fancybox fancybox.iframe" href="http://www.youtube.com/embed/paG__3FBLzI">
    <img class="videoThumb" src="http://i1.ytimg.com/vi/paG__3FBLzI/mqdefault.jpg"></a>
  </figure>
  <h2 class="videoTitle">Mesopotamia</h2>
</article>

<article class="video">
  <figure>
    <a class="fancybox fancybox.iframe" href="http://www.youtube.com/embed/paG__3FBLzI">
    <img class="videoThumb" src="http://i1.ytimg.com/vi/paG__3FBLzI/mqdefault.jpg"></a>
  </figure>
  <h2 class="videoTitle">Mesopotamia</h2>
</article>

<article class="video">
  <figure>
    <a class="fancybox fancybox.iframe" href="http://www.youtube.com/embed/paG__3FBLzI">
    <img class="videoThumb" src="http://i1.ytimg.com/vi/paG__3FBLzI/mqdefault.jpg"></a>
  </figure>
  <h2 class="videoTitle">Mesopotamia</h2>
</article>

<article class="video">
  <figure>
    <a class="fancybox fancybox.iframe" href="http://www.youtube.com/embed/paG__3FBLzI">
    <img class="videoThumb" src="http://i1.ytimg.com/vi/paG__3FBLzI/mqdefault.jpg"></a>
  </figure>
  <h2 class="videoTitle">Mesopotamia</h2>
</article>

<html>
<head>
<style>
  img {
  max-width: 100%;
  height: auto;
}

/* 
This is the starting grid for each video with thumbnails 4 across for the largest screen size.
It's important to use percentages or there may be gaps on the right side of the page. 
*/

.video {
  background: #fff;
  padding-bottom: 20px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
  width: 23%; /* Thumbnails 4 across */
  margin: 1%;
  float: left;
}

/* 
These styles keep the height of each video thumbnail consistent between YouTube and Vimeo. 
Each can have thumbnail sizes that vary by 1px and are likely break your layout. 
*/

.video figure {
  height: 0;
  padding-bottom: 56.25%;
  overflow: hidden;
}

.video figure a {
  display: block;
  margin: 0;
  padding: 0;
  border: none;
  line-height: 0;
}

/* Media Queries - This is the responsive grid. */

@media (max-width: 1024px) {
  .video {
    width: 31.333%; /* Thumbnails 3 across */
  }
}

@media (max-width: 600px) {
  .video {
    width: 48%; /* Thumbnails 2 across */
  }
}

@media (max-width: 360px) {
  .video {
    display: block;
    width: 96%; /* Single column view. */
    margin: 2%; /* The smaller the screen, the smaller the percentage actually is. */
    float: none;
  }
}

/* These are my preferred rollover styles. */

.video img {
  width: 100%;
  opacity: 1;
}

.video img:hover, .video img:active, .video img:focus {
  opacity: 0.75;
}

</style>
</head>
<body>


<script
  src="http://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>

<script>js/jquery.fancybox.min.js</script>

<script>
  $(document).ready(function() {
    $('.fancybox').fancybox({
      padding   	: 0,
      maxWidth  	: '100%',
      maxHeight 	: '100%',
      width   		: 560,
      height    	: 315,
      autoSize  	: true,
      closeClick  : true,
      openEffect  : 'elastic',
      closeEffect : 'elastic'
    });
  });
</script>

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
