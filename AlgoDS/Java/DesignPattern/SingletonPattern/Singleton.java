/**
 * Singleton Pattern in Java
 *  @author Kuntal
 */

import java.io.Serializable;

public class Singleton implements Serializable, Cloneable{
	

	private static final long serialVersionUID = 1L;
	
	private volatile static Singleton IS_INSTANCE;
	
	// private constructor
    private Singleton() {}

	
	
	public static Singleton getInstance(){
		
		if(IS_INSTANCE==null){
			
			synchronized(Singleton.class){
				if(IS_INSTANCE==null){
					IS_INSTANCE=new Singleton();
				}
				
			}
			
			
		}
		return IS_INSTANCE;
		
		
	}
	
	// method for preventing the singleton class to be serialized/deserialized.
	protected Object readResolve() {
        return IS_INSTANCE;
    }
	
	// method for preventing the singleton class to be cloned.
	protected Object clone() throws CloneNotSupportedException {
	    throw new CloneNotSupportedException(); 
	}
	
	private void testHello(){
		System.out.println("Hello method");
	}
	
	
	public static void main(String[] args) {
		
		Singleton test = Singleton.getInstance();
		test.testHello();
		
		try {
			Singleton test2 = (Singleton)test.clone();
        } catch (CloneNotSupportedException e) {
            // TODO Auto-generated catch block
            System.out.println(e);
        }
		
		

		
	}

}
