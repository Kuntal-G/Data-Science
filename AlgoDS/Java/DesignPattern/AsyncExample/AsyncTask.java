import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;

public class AsyncTask implements Supplier<String>{

	@Override
	public String get() {
		try {
			
            TimeUnit.SECONDS.sleep(5);
        } catch (InterruptedException e) {
            throw new IllegalStateException(e);
        }
		
        return "Result of the asynchronous computation";
    }
	

}
