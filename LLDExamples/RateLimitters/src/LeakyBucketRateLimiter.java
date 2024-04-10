import java.util.concurrent.TimeUnit;

public class LeakyBucketRateLimiter {
    private final long capacity;
    private double tokens;
    private long lastRefillTimestamp;
    private final double refillRate;

    public LeakyBucketRateLimiter(long capacity, long refillInterval, TimeUnit timeUnit) {
        this.capacity = capacity;
        this.tokens = 0;
        this.refillRate = (double) capacity / timeUnit.toMillis(refillInterval);
        this.lastRefillTimestamp = System.currentTimeMillis();
    }

    public synchronized boolean tryConsume(long tokens) {
        refillTokens();
        if (this.tokens >= tokens) {
            this.tokens -= tokens;
            return true;
        }
        return false;
    }

    private void refillTokens() {
        long currentTime = System.currentTimeMillis();
        double elapsedTime = (double) (currentTime - lastRefillTimestamp);
        tokens = Math.min(capacity, tokens + (elapsedTime * refillRate));
        lastRefillTimestamp = currentTime;
    }

    public static void main(String[] args) throws InterruptedException {
        LeakyBucketRateLimiter rateLimiter = new LeakyBucketRateLimiter(3, 10, TimeUnit.SECONDS);

        for (int i = 0; i < 20; i++) {
            if (rateLimiter.tryConsume(1)) {
                System.out.println("Request " + (i + 1) + ": Allowed");
            } else {
                System.out.println("Request " + (i + 1) + ": Denied");
            }
            Thread.sleep(200); // Simulating requests coming in
        }
    }
}
