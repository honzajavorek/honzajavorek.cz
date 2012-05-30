<?php
$uri = $_SERVER['REQUEST_URI'];

if ($uri == '/feeds/') {
    $loc = 'http://feeds.feedburner.com/javorove-listky';

} elseif ($uri == '/') {
    $loc = rtrim('http://honzajavorek.cz');

} elseif ($uri == '/comments/feed/') {
    $loc = 'http://javorove-listky.disqus.com/latest.rss';

} else {
    $loc = rtrim('http://honzajavorek.cz/blog' . $uri, '/');
}

header('HTTP/1.1 301 Moved Permanently');
header('Location: ' . $loc);

echo $loc;