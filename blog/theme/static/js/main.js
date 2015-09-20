/**
 * Main JavaScript.
 */

$(document).ready(function() {

    if ($.fn.tipsy) {
        $('img[title]').tipsy({
            'opacity': 1,
            'gravity': 's'
        });
        $('a[title]').tipsy({
            'opacity': 1,
            'gravity': 'n'
        });
    }

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
