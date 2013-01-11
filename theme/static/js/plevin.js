/**
 * Plevin schedules.
 */

var dayMap = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle'];


function getWeekday() {
    var n = new Date().getDay(); // 0 is Sunday, 6 is Saturday
    if (n === 0) {
        return 6;
    }
    return n - 1;
}


function ajaxSettingsFactory(url, xpath, callback) {
    var query = 'SELECT * FROM html WHERE url="' + url +
        '" AND xpath="' + xpath + '"';
    return {
        'url': 'http://query.yahooapis.com/v1/public/yql',
        'dataType': 'xml',
        'success': callback,
        'async': true,
        'data': {
            'q': query,
            'format': 'xml'
        }
    };
}


function scrapeRubin(callback) {
    var url = 'http://restauracerubin.cz/obedova-menu/';
    var xpath = '//*[@id=\'content\']';
    $.ajax(ajaxSettingsFactory(url, xpath, function(response) {
        var $html = $(response);

        var week = [];
        var days = [];

        $('.menu_table', $html).each(function(i) {
            var $table = $(this);
            var isWeek = (i === 0);
            var day = [];

            $('tr', $table).each(function() {
                var $tr = $(this);
                var dish = {
                    'quantity': $('.quantity', $tr).text(),
                    'label': $('.label', $tr).text(),
                    'price': $('.price_label', $tr).text()
                };
                if (isWeek) {
                    week.push(dish);
                } else {
                    day.push(dish);
                }
            });

            if (!isWeek) {
                days.push(day);
            }
        });

        callback(week, days);
    }));
}


function scrapeRubinSkrz(callback) {
    var url = 'http://skrz.cz/firmy/restaurace-rubin/nabidky';
    var xpath = '//*[@id=\'merchantdetail-deallist\']';
    $.ajax(ajaxSettingsFactory(url, xpath, function(response) {
        var $html = $(response);

        var offers = [];

        $('.object-deal', $html).each(function(i) {
            var $offer = $(this);

            if ($('.left-time', $offer).text().indexOf('skončila') !== -1) {
                return true; // skipping not active offers
            }

            offers.push({
                'label': $('h3', $offer).text(),
                'price': $('.price', $offer).text(),
                'url': $('.text-more a', $offer).attr('href')
            });
        });

        callback(offers);
        refreshAnchor();
    }));
}


function constructDish(day, isSoup, isWeek) {
    var $dish = $('<tr />', {'class': 'dish'});

    if (isSoup) {
        $dish.addClass('soup');
    }
    if (isWeek) {
        $dish.addClass('week_dish');
    }

    $('<td />', {'text': day.quantity, 'class': 'quantity'}).appendTo($dish);
    $('<td />', {'text': day.label}).appendTo($dish);
    $('<td />', {'text': day.price, 'class': 'price'}).appendTo($dish);

    return $dish;
}


function refreshAnchor() {
    var hash = window.location.hash.substring(1);
    document.getElementById(hash).scrollIntoView(hash);
}


$(document).ready(function() {

    // standard schedules
    var weekday = getWeekday();
    var $schedules = $('.schedule');

    $('.schedule').each(function() {
        var $table = $(this);
        $('tr', $table).eq(weekday).addClass('today');

        $table.addClass('collapsed');
        $table.attr('title', 'celý týden');

        $table.click(function() {
            var $table = $(this);
            $table.removeClass('collapsed');
            $table.removeAttr('title');
        });
    });

    // rubin
    scrapeRubin(function(week, days) {
        var $menu = $('#menu');
        $menu.empty();

        $.each(days, function(dayNumber, day) {
            if (dayNumber >= 5) {
                return false; // only Monday to Friday
            }
            if (dayNumber < weekday) {
                return true; // yesterday's food? for what?
            }

            // prepare day
            var $title = $('<h3 />', {'text': dayMap[dayNumber]});
            var $day = $('<table />', {'class': 'dishes'});

            if (dayNumber === weekday) {
                $day.addClass('today');
            }

            // iterate over days
            $.each(day, function(dishNumber, day) {
                constructDish(day, dishNumber === 0).appendTo($day);
            });
            $.each(week, function(dishNumber, day) {
                constructDish(day, false, true).appendTo($day);
            });

            // append day to menu
            $title.appendTo($menu);
            $day.appendTo($menu);
        });

        // final refinements and simplified UI
        if (!$menu.children().length) {
            $('<p />', {'text': 'Dnes žádné menu není.', 'class': 'placeholder'}).appendTo($menu);

        } else {
            $menu.addClass('collapsed');
            $menu.attr('title', 'celý týden');

            $menu.click(function() {
                var $menu = $(this);
                $menu.removeClass('collapsed');
                $menu.removeAttr('title');
            });
        }
    });

    // rubin discount offers
    scrapeRubinSkrz(function(offers) {
        var $offers = $('#offers');
        $offers.empty();

        var $dishes = $('<table />', {'class': 'dishes'});
        $.each(offers, function(offerNumber, dish) {
            var $dish = $('<tr />', {'class': 'dish'});
            $('<td />', {'text': dish.label}).appendTo($dish);
            $('<td />', {'text': dish.price, 'class': 'price'}).appendTo($dish);

            var $linkCell = $('<td />', {'class': 'link'}).appendTo($dish);
            $('<a />', {'href': dish.url, 'text': 'Koupit'}).appendTo($linkCell);

            $dish.appendTo($dishes);
        });

        // final refinements
        if (!$dishes.children().length) {
            $('<p />', {'text': 'Žádné slevy nejsou.', 'class': 'placeholder'}).appendTo($menu);

        } else {
            $dishes.appendTo($offers);
        }
    });
});
