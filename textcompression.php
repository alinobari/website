<?php
$js_var = "No File Chosen";

$name = $_FILES['file']['name'];
$tmp_name = $_FILES['file']['tmp_name'];

$location = 'uploads/';
if(move_uploaded_file($tmp_name, $location.$name)) {
  //echo "Uploaded ";
} else {
  //echo "didn't work ";
}

$temp = explode('.', $name);
//extension of the file
$ext  = array_pop($temp);
//name of the file
$sname = implode('.', $temp);

$ext_match = "txt";

//if a text file
if ($ext == $ext_match) {

  //run python code
  exec("python3 ./python/encode/mtfencode.py ./uploads/$name");

  //add .mtf to the file
  $sname .= ".mtf";

  //sleep(3);
  $file = "./uploads/$sname";

  // Quick check to verify that the file exists
  while (!file_exists($file) ) {
    sleep(1);
  }

  if (file_exists($file) ) {
    // Force the download
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($file).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($file));
    readfile($file);
    //delete
    unlink($file);
    exit;
  }

}

$ext_match = "mtf";

//if a mtf file
if ($ext == $ext_match) {

  //run python code
  exec("python3 ./python/decode/mtfdecode.py ./uploads/$name");

  //add .mtf to the file
  $sname .= ".txt";

  //sleep(3);
  $file = "./uploads/$sname";

  // Quick check to verify that the file exists
  while (!file_exists($file) ) {
    sleep(1);
  }

  if (file_exists($file) ) {
    // Force the download
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($file).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($file));
    readfile($file);
    //delete
    unlink($file);
    exit;
  }

}
//exit;
?> 


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
 <!--   <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1"> -->
    <title>Ali Nobari - Text Compression</title>
    <link rel='stylesheet prefetch' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css'>
    <link rel="stylesheet prefetch" href="css/bootstrap.min.css" >
    <link rel='stylesheet prefetch' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css'>
    <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700'>

    <link rel="stylesheet prefetch" type="text/css" href="css/style.css">
    <link rel="stylesheet prefetch" type="text/css" href="css/style-textcompression.css">
 <!--    Bootstrap 
    <link href="css/bootstrap.min.css" rel="stylesheet"> -->

    <!-- onclick='javascript:GetFileName()'-->
    
    <script type='text/javascript'>

     //to display the name of the file when Choose File is clicked
      function GetFileName(){
        // Get your file input (by it's id)
        var fileInput = document.getElementById('fileupload');
        // Use a regular expression to pull the file name only
        var fileName = fileInput.value.split(/(\\|\/)/g).pop();
        // Alert the file name (example)
        //alert(fileName);
        document.getElementById("textbox").value = fileName;
      }

      //to display the name of the file when Choose File is clicked
      function Execution(){
        var string = "txt"
        var fileInput = document.getElementById('fileupload');
        var fileName = fileInput.value.split(/(\\|\/)/g).pop();

        var re = /(?:\.([^.]+))?$/;
        var ext = re.exec(fileName)[1];

        if (ext == string) {
          document.getElementById("textbox2").value = "Compressed, Encrypted";
        } else {
          document.getElementById("textbox2").value = "Decompressed, Decrypted";
        }
      }
    </script>
  </head>
  <body>
 

  <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="index.html">Ali Nobari</a>     
      </div>

      <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav navbar-right fixed-right">
          <li><a ></a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Projects 
              <b class="caret"></b></a>
                <ul class="dropdown-menu">
                  <li><a href="textcompression.php">Text Compression</a></li>
                </ul>
            </li>
        </ul>
      </div>
    </div>
  </nav>
 
 
  <body data-spy="scroll" data-target="#navbar-example">

  <div class="wrapper" >

    <nav class="nav__wrapper" id="navbar-example">
      <ul class="nav navv">

        <li role="presentation" class="active">
          <a href="#section1">
            <span class="nav__counter">01</span>
            <h3 class="nav__title">Text Compression</h3>
            <p class="nav__body"></p>
          </a>
        </li>


      </ul>
    </nav>

    <section class="section section1" id="section1">

      <ul class="submit">
        <form action="textcompression.php" method="POST" enctype="multipart/form-data">
          <input type="file" name="file" id="fileupload" value="No File Chosen" onchange='javascript:GetFileName()'>
          <label id="fileupload-replaced" for="fileupload">Choose File</label>

          <input type="submit" value="Submit" id="filesubmit">
          <label id="filesubmit-replaced" for="filesubmit" onclick='javascript:Execution()'>Submit File</label>
        </form>


        <div class="box">
          <input type="text" value="No File Chosen" id="textbox">
          <input type="text" id="textbox2">
        </div>

 
        <div>
        <tr>
        <div class="col-sm-12" align="center">
        <a id="insta" href="txt/input.txt" align>sample</a>
        </div>
        </tr>
        </div>

      </ul>
    </section>

      <div class="footer" id="footer">
      <div class="col-sm-4" align="center">
        <img src="image/instagram.png" width="20" height="20">
        <a id="insta" href="https://www.instagram.com/ali_nobari/">ali_nobari</a>
      </div> 
      <div class="col-sm-4" align="center">
                <p>Website by Ali Nobari</p>
      </div>
      <div class="col-sm-4" align="center">
        <img src="image/UVictoria_logo.png" width="25" height="30">
        <a id="insta">alinobar@uvic.ca</a>
      </div>
  <div>







  </div>
  
</body>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
  <!--<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"></script> --> 
  <script src="js/index.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
    
  </body>
</html>
