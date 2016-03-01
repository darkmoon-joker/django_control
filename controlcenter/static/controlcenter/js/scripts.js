window.$ = django.jQuery;
window.jQuery = $;

(function($){
    // On DOM load
    $(function(){
        // GRID
        var msnry = new Masonry('.controlcenter__masonry__offset', {
            itemSelector: '.controlcenter__masonry__block',
            columnWidth: '.controlcenter__masonry__block--sizer',
            percentPosition: true,
            transitionDuration: 0
        });

        // TABS
        var tab = 'controlcenter__widget__tab',
            active_tab = tab + '--active';

        $('.' + tab).click(function(e){
            $(this).siblings().removeClass(active_tab).end()
                   .addClass(active_tab);
        });
    });
})(django.jQuery);