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
        $('.article_content > p > br').closest('p').addClass('poem');

        // anchors
        $('h1, h2, h3, h4', '.article').filter('[id]').each(function() {
            var $heading = $(this);
            var $a = $('<a>', {'href': '#' + $heading.attr('id'), text: '#'});
            $a.appendTo($heading);
            $a.wrap($('<small>', {'class': 'anchor'}));
        });
    }

});

if ($('#disqus_thread').length) {
    // disqus loading
    var check_disqus = setInterval(function() {
        var disqus_ready = $('#disqus_thread').height() > 100;
        if (disqus_ready) {
            clearInterval(check_disqus); // remove timer
            $('html').addClass('ready');
        }
    }, 100);
}
