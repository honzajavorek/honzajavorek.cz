/**
 * Main JavaScript.
 */

$(document).ready(function() {

    if ($('.article').length) {
        // poem styling
        $('#content article > p > br').closest('p').addClass('poem');

        // anchors
        $('h1, h2, h3, h4', '.article').filter('[id]').each(function() {
            var $heading = $(this);
            var $a = $('<a>', {'href': '#' + $heading.attr('id'), text: '#'});
            $a.appendTo($heading);
            $a.wrap($('<small>', {'class': 'anchor'}));
        });

        // disqus
        var check_disqus = setInterval(function() {
            $reactionsHeader = $('.dsq-h3-reactions', '#dsq-content');
            var disqus_ready = $('#dsq-reply').get(0) != null;
            if (disqus_ready) {
                clearInterval(check_disqus); // remove timer

                // prepare context for lookup
                $disqus = $('#dsq-content');

                // my changes
                $('.dsq-h3-reactions', $disqus).text('Reakce');

                // display comments
                $('.article hr').show();
                $('#comments_inner').show();
                $('#comments').removeClass('loading');
            }
        }, 100);
    }

});