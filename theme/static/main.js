/**
 * Main JavaScript.
 */

// ToDo rewrite this to Python

$(document).ready(function() {
    if ($('.article').length) {
        // poem styling
        $('.article-content > p > br').closest('p').addClass('poem');

        // anchors
        $('h1, h2, h3, h4', '.article').filter('[id]').each(function() {
            var $heading = $(this);
            var $a = $('<a>', {'href': '#' + $heading.attr('id'), text: '#'});
            $a.appendTo($heading);
            $a.wrap($('<small>', {'class': 'anchor'}));
        });
    }
});
