<?php
        $begStr = "2017-12-28";
    $endStr = "2018-10-29";
    $dayStamp = strtotime($endStr) - strtotime($begStr);
    echo "相差".($dayStamp / 24 / 60 / 60).'天';
?>