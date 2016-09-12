<?php
session_start();
unset($_SESSION['password']);
unset($_SESSION['user_name']);
session_destroy();
#echo "Click here to redirect";
header("Location:final.html");
?>