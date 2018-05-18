<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
<?php
include("menu.php")
?>
</head>
<body>
<form action='contactus.php' method="post">
<p>Вы можете оставить отзыв о выставке, заполнив форму:</p> <p>Вам понравилась выставка?</p>
<p><input type="radio" name="areyou"/> Да</p>
<p><input type="radio" name="areyou"/> Нет</p>
<p> Комментарий </p>
<p><textarea rows="10" cols="40"></textarea></p>

<p><input type="reset"></p>
<p><input type="submit"></p>
  
<input type="hidden" value="klimmail.ru@mail.ru"/>

</form>

</body>
</html>