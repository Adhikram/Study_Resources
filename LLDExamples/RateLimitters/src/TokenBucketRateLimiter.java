import java.util.concurrent.TimeUnit;

public class TokenBucketRateLimiter {
    private final long capacity;
    private double tokens;
    private long lastRefillTimestamp;
    private final double refillRate;

    public TokenBucketRateLimiter(long capacity, long refillInterval, TimeUnit timeUnit) {
        this.capacity = capacity;
        this.tokens = capacity;
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
        double tokensToAdd = elapsedTime * refillRate;
        tokens = Math.min(capacity, tokens + tokensToAdd);
        lastRefillTimestamp = currentTime;
    }

    public static void main(String[] args) throws InterruptedException {
        TokenBucketRateLimiter rateLimiter = new TokenBucketRateLimiter(3, 10, TimeUnit.SECONDS);

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
