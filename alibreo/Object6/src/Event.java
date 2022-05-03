import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;

public class Event {
    private String subject;
    private LocalDateTime from;
    private Duration duration;

    public Event(String subject, LocalDateTime from, Duration duration) {
        this.subject = subject;
        this.from = from;
        this.duration = duration;
    }

    public boolean isSatisfied(RecurringSchedule schedule) {
        if (from.getDayOfWeek() != schedule.getDayOfWeek() ||
                !from.toLocalTime().equals(schedule.getFrom()) ||
                !duration.equals(schedule.getDuration())
        ) {
            reschedue(schedule);
            return false;
        }
        return true;
    }

    private void reschedue(RecurringSchedule schedule) {
        from = LocalDateTime.of(from.toLocalDate().plusDays(dyasDistance(schedule)), schedule.getFrom());
        duration = schedule.getDuration();
    }

    private long dyasDistance(RecurringSchedule schedule) {
        return schedule.getDayOfWeek().getValue() - from.getDayOfWeek().getValue();
    }
}
