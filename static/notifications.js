$(document).ready(function() {
    function fetchNotifications() {
        $.ajax({
            url: '/get_notifications/',  // URL to fetch notifications
            type: 'GET',
            success: function(data) {
                $('#notification-list').html(data);
            }
        });
    }

    setInterval(fetchNotifications, 5000); // Example: Fetch every 5 seconds
});
