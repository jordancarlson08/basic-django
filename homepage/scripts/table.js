$(function() {

    var container = $('#table_container');

    $('#prev_page_button').off('click.page').on('click.page', function() {
        var page = parseInt(container.data('page'));
        container.data('page', Math.max(0, page - 1));
        container.trigger('table_refresh');

    });

    $('#next_page_button').off('click.page').on('click.page', function() {
        var page = parseInt(container.data('page'));
        container.data('page', page + 1);
        container.trigger('table_refresh');
    });

    //handle table refresh
    container.on('table_refresh', function() {
        $.ajax({
            url: '/homepage/table.get_table/' + container.data('page')
        }).success(function(data) {
                container.html(data);
        }); //ajax

    }).trigger('table_refresh');

}); // ready