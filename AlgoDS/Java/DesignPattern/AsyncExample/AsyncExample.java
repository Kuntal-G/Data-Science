/**
* Basic Java Async example with Completable future
* @author Kuntal
*/

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class AsyncExample {
	
	private static String greet(String name){
		
		return "hello"+name;
	}
	
	
	public static void main(String[] args) throws InterruptedException, ExecutionException {
		
		//CompletableFuture<Void> future = CompletableFuture.runAsync(new BlockTask());
		
		//System.out.println(future.get());
		
		CompletableFuture<String> future = CompletableFuture.supplyAsync(new AsyncTask());
		
		CompletableFuture<String> greetingFuture = future.thenApply(new Test());
		
		System.out.println(greetingFuture.get());
				
	}

}
