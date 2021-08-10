<?php
// connect to FTP server
$ftp_server = "server308.com";
$ftp_conn = ftp_connect($ftp_server) or die("Could not connect to $ftp_server");

// login
if (@ftp_login($ftp_conn, 'joinsoca', 'vF<^aPt]!%B{+!779b#h'))
  {
    echo "Connection established.";
    echo ftp_pwd($ftp_conn);
    $filesdirectory= ftp_nlist($ftp_conn, '.');

echo "$filesdirectory";
  }
else
  {
  echo "Couldn't establish a connection.";
  }

ftp_close($ftp_conn);
?>