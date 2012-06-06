<?php
$uri = rtrim($_SERVER['REQUEST_URI'], '/');

if ($uri == '/feeds' || $uri == '/feed') {
    $loc = 'http://feeds.feedburner.com/javorove-listky';

} elseif ($uri == '/comments/feed' || $uri == '/comments/feeds') {
    $loc = 'http://javorove-listky.disqus.com/latest.rss';

} elseif (!$uri) {
    $loc = rtrim('http://honzajavorek.cz');

} else {
    $loc = 'http://honzajavorek.cz/blog' . $uri;
}

header('HTTP/1.1 301 Moved Permanently');
header('Location: ' . $loc);

echo $loc;