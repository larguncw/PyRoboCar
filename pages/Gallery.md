
<html>
<head>
<style>
div.gallery {
  border: 1px solid #ccc;
}

div.gallery:hover {
  border: 1px solid #777;
}

div.gallery img {
  width: 100%;
  height: auto;
}

div.desc {
  padding: 15px;
  text-align: center;
}

* {
  box-sizing: border-box;
}

.responsive {
  padding: 0 6px;
  float: left;
  width: 24.99999%;
}

@media only screen and (max-width: 700px) {
  .responsive {
    width: 49.99999%;
    margin: 6px 0;
  }
}

@media only screen and (max-width: 500px) {
  .responsive {
    width: 100%;
  }
}

.clearfix:after {
  content: "";
  display: table;
  clear: both;
}
</style>
</head>
<body>

<h2>Image Gallery</h2>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/PiCar.jpeg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/PiCar.jpeg" alt="PyRoboCar" width="600" height="400">
    </a>
    <div class="desc">PyRoboCar</div>
  </div>
</div>


<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/car_on_track.png">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/car_on_track.png" alt="PyRoboCar on Track" width="600" height="400" class="rotateimg90">
    </a>
    <div class="desc">PyRoboCar on the Track</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/r5CwHJUNQjy8JNZcbJfMPw.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/r5CwHJUNQjy8JNZcbJfMPw.jpg" alt="Tracks" width="600" height="400">
    </a>
    <div class="desc">PyRoboCar Labeled Lane Lines</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20200130_100403170.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20200130_100403170.jpg" alt="Mountains" width="600" height="400">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20200130_100952378.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20200130_100952378.jpg" alt="Mountains" width="600" height="400">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20200206_101943082.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20200206_101943082.jpg" alt="Mountains" width="600" height="400">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201012_095239980.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201012_095239980.jpg" alt="Mountains" width="600" height="400">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201021_095124645.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201021_095124645.jpg" alt="Mountains" width="600" height="400">
    </a>
    <div class="desc">Add a description of the image here</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201021_100222005.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201021_100222005.jpg" alt="Tracks" width="600" height="400">
    </a>
    <div class="desc">PyRoboCar Labeled Lane Lines</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201021_101113596.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/IMG_20201021_101113596.jpg" alt="Tracks" width="600" height="400">
    </a>
    <div class="desc">PyRoboCar Labeled Lane Lines</div>
  </div>
</div>

<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://larguncw.github.io/PyRoboCar/pages/images/finished car 1.jpg">
      <img src="https://larguncw.github.io/PyRoboCar/pages/images/finished car 1.jpg" alt="Tracks" width="600" height="400">
    </a>
    <div class="desc">PyRoboCar Labeled Lane Lines</div>
  </div>
</div>


<div class="clearfix"></div>

<div style="padding:6px;">
  <p>This example use media queries to re-arrange the images on different screen sizes: for screens larger than 700px wide, it will show four images side by side, for screens smaller than 700px, it will show two images side by side. For screens smaller than 500px, the images will stack vertically (100%).</p>
  <p>You will learn more about media queries and responsive web design later in our CSS Tutorial.</p>
</div>

</body>
</html>
