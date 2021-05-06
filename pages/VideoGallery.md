<div id="video-gallery">
  <a href="https://www.youtube.com/watch?v=meBbDqAXago" data-poster="video-poster1.jpg" >
      <img src="img/thumb1.jpg" />
  </a>
  <a href="https://vimeo.com/1084537" data-poster="video-poster2.jpg">
      <img src="img/thumb2.jpg" />
  </a>
  ...
</div>

$('#video-gallery').lightGallery(); 

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
