/**
 * Foodlog. See https://github.com/honzajavorek/foodlog.
 */

var errors = [];

function error(details) {
    if (!$('#foodlog_error').text()) {
        message = 'Chyba!';
        if (details) {
            message += ' <small><code>' + details + '</code></small>';
        }
        $('#foodlog_error').html('<p>' + message + '</p>');
    }
    errors.push('error: ' + details || 'unknown');
}

function url() {
    if (window.location.hostname.match(/localhost|127\.0\.0\.1/)) {
        return 'http://0.0.0.0:5000';
    }
    return 'http://calm-citadel-5083.herokuapp.com';
}

function refresh() {
    var success = false;

    $.getJSON(url(), function(data) {
        success = !data.error;

        if (data.error) {
            error(data.error);

        } else {
            $ul = $('<ul>');
            for (var i in data.food) {
                item = data.food[i];
                content = item.eaten_at_formatted + ' <strong>' + item.name + '</strong>';
                $ul.append($('<li>').html(content));
            }
            $('#foodlog_list').empty().append($ul);
        }
    });

    setTimeout(function() {
        if (!success) {
            error();
        }
    }, 5000);
}

$(document).ready(function() {
    $('#foodlog_form').attr('action', url() + '/add');

    $(this).ajaxError(function(event, xhr, settings, e) {
        error(e);
    });

    $('#foodlog_form').submit(function(event) {
        if (!errors.length) {
            $.post($(this).attr('action'), $(this).serialize(), function(data) {
                $('#name').val('');
                refresh();
            });
            event.preventDefault();
        }
    });

    refresh();
});
