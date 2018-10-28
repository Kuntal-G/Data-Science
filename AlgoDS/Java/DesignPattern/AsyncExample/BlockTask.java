import java.util.concurrent.TimeUnit;

public class BlockTask implements Runnable{
	
	
	public void run() {
        // Simulate a long-running Job
        try {
            TimeUnit.SECONDS.sleep(5);
        } catch (InterruptedException e) {
            throw new IllegalStateException(e);
        }
        System.out.println("I'll run in a separate thread than the main thread.");
    }

}
