<?php
  session_start();
?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
    <link rel="stylesheet" href="style1.css">
  </head>
  <body>
    <header>
      <div class="container">
        <a class="header-logo" href="#">
          <img src="img/avatar-512.png" alt="logo">
        </a>

        <nav class="nav-header-main">

            <ul>
              <li> <a href="#">Home</a> </li>
              <li> <a href="#">News</a></li>
              <li> <a href="#">About Us</a></li>
              <li> <a href="#">Contact</a></li>
            </ul>


          <div class="header-login">
            <?php
            if (isset($_SESSION['userId'])) {
              echo '<form class="form-login" action="includes/logout.inc.php" method="post">
                      <button class="btn" type="submit" name="logout-submit">Logout</button>
                    </form>';
            }
            else {
              echo '<form class="form-login" action="includes/login.inc.php" method="post">
                      <input type="text" name="mailuid" placeholder="Username/E-mail..">
                      <input type="password" name="pwd" placeholder="password..">
                      <button class="btn" type="submit" name="login-submit">Login</button>
                      <button class="btn1"><a href="signup.php">Signup</a></button>
                    </form>';
            }
             ?>



          </div>
        </nav>
      </div>
    </header>
    <main>
    <div class="wrapper">
      <section id="login">
        <h1>Signup</h1>
        <?php
          if (isset($_GET["eror"])) {
            if ($_GET["eror"] == "emptyfields") {
              echo '<p class="signuperor"> Fill in all fields! </p>';
            }
            else if ($_GET["eror"] == "invaliduidmail" ) {
              echo '<p class="signuperor"> Invalid username and e-mail! </p>';
            }
            else if ($_GET["eror"] == "invaliduid") {
              echo '<p class="signuperor"> Invalid username</p>';
            }
            else if ($_GET["eror"] == "invalidmail") {
              echo '<p class="signuperor"> Invalid e-mail</p>';
            }
            else if ($_GET["eror"] == "passwordcheck") {
              echo '<p class="signuperor"> Your passwords do not match</p>';
            }
            else if ($_GET["eror"] == "usertaken") {
              echo '<p class="signuperor"> Username is already taken</p>';
            }
          }
          // else if ($_GET["Signup"] == "success") {
          //   echo '<p class="signupsuccess">Signup successful</p>';
          // }
        ?>
        <form class="form-signup" action="includes/signup.inc.php" method="post">
            <div class="form-group">
              <input type="text" name="uid" value="" placeholder="Username">
            </div>
            <div class="form-group">

              <input type="text" name="mail" value="" placeholder="E-mail">
            </div>
            <div class="form-group">

              <input type="password" name="pwd" value="" placeholder="password">
            </div>
            <div class="form-group">

              <input type="password" name="pwd-repeat" value="" placeholder="repeat-password">
            </div>
              <button class="button" type="submit" name="signup-submit">Signup</button>

        </form>
      </section>
    </div>

  </main>

  </body>
</html>
