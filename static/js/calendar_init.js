function fetchBookingsAndRender(calendar) {
    $.ajax({
        url: 'booking/api/bookings',  // URL of the new Flask route
        method: 'GET',
        success: function(data) {
            // Assuming 'data' is an array of booking objects
            data.forEach(function(booking) {
                calendar.addEvent({
                    title: booking.title,
                    start: booking.start,
                    end: booking.end
                });
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error fetching bookings:', textStatus, errorThrown);
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("Setting up modals...");

    $('.modal').on('shown.bs.modal', function() {
        var modal = this;
        console.log("Modal shown:", modal);

        var serviceId = modal.getAttribute('data-service-id');
        console.log("Service ID:", serviceId);

        var calendarEl = document.getElementById('calendar-' + serviceId);
        console.log("Calendar element:", calendarEl);

        if (calendarEl && !calendarEl.classList.contains('initialized')) {
            var lastSelectedEvent = null; // Variable to store the last selected slot

            var calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'timeGridWeek',
                headerToolbar: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'timeGridDay,timeGridWeek'
                },
                events: [
                    { title: 'Meeting', start: new Date() }
                ],
                slotDuration: '00:30:00', // Slot duration set to 30 minutes
                slotLabelInterval: '00:30:00', // Labels for time slots every 30 minutes
                slotMinTime: '08:00:00', // Calendar starts at 8 AM
                slotMaxTime: '17:00:00', // Calendar ends at 5 PM
                weekends: false, // Hide weekends (Saturday and Sunday)
                allDaySlot: false, // Disable all-day slot
                selectable: true, // Allows users to select time slots
                selectMirror: true,
                select: function(selectionInfo) {
                    // Calculate the duration of the selected time slot in minutes
                    var duration = moment(selectionInfo.end).diff(moment(selectionInfo.start), 'minutes');

                    // Check if the duration is exactly 30 minutes
                    if(duration === 30) {
                        // Remove the last selected event if it exists
                        if (lastSelectedEvent) {
                            var lastEvent = calendar.getEventById('selectedSlot');
                            if (lastEvent) {
                                lastEvent.remove();
                            }
                        }

                        // Add the new selected event
                        var newEvent = {
                            id: 'selectedSlot',
                            start: selectionInfo.start,
                            end: selectionInfo.end,
                            title: 'Selected Slot',
                            allDay: selectionInfo.allDay
                        };
                        calendar.addEvent(newEvent);
                        lastSelectedEvent = newEvent;

                        // Optional: Update form or booking details here
                        // For example, you might populate form fields with the selected time slot
                        // ...
                        // Example of creating a form dynamically and appending it to a DOM element
                        var formHtml = `
                            <form action="/book_service/${serviceId}" method="post">
                                <input type="hidden" name="appointment_date" value="${selectionInfo.startStr}" />
                                <input type="hidden" name="appointment_end" value="${selectionInfo.endStr}" />
                                <button type="submit" class="btn btn-primary">Confirm Booking</button>
                            </form>
                        `;

                        var bookingLink = `/booking/confirm_booking?service_id=${serviceId}&start=${selectionInfo.startStr}&end=${selectionInfo.endStr}`;

                    
                        // Append the form to a specific element, e.g., below the calendar
                        document.getElementById('booking-form-container').innerHTML = formHtml;

                        // Create an anchor tag styled as a button
                        var buttonHtml = `
                            <a href="${bookingLink}" class="btn btn-primary">Confirm Booking</a>
                        `;

                        // Append the button to a specific element, e.g., below the calendar
                        document.getElementById('booking-form-container').innerHTML = buttonHtml;
                    } else {
                        alert("Please select a 30-minute time slot.");
                    }
                },                
                eventClick: function(arg) {
                    if (arg.event.id === 'selectedSlot') {
                        arg.event.remove();
                        lastSelectedEvent = null;
                    }
                },
                editable: false,
                // Disable selecting time ranges via clicking and dragging
                selectable: true,

                // Disable editing (moving and resizing) of events
                editable: false,
            });

            calendar.render();
            calendar.updateSize();
            calendarEl.classList.add('initialized');
            fetchBookingsAndRender(calendar);
        }
    });
});
